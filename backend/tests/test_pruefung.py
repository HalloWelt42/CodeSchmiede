"""Prüfung über die API: richtig, falsch, Betrugsversuche, JS, SQL, Quiz."""

from .conftest import braucht_sandbox

pytestmark = braucht_sandbox


def submit(client, aid, code):
    antwort = client.post("/api/submissions", json={"aufgabe_id": aid, "code": code})
    assert antwort.status_code == 200, antwort.text
    return antwort.json()


def test_python_richtig(client):
    erg = submit(client, "001-verdoppeln", "def verdoppeln(x):\n    return x * 2\n")
    assert erg["bestanden"]
    assert erg["pruefung"]["versteckt_pass"] == 2
    assert erg["vergleich"][0]["variante"] == "idiomatic"


def test_python_falsch_zeigt_nur_sichtbare(client):
    erg = submit(client, "001-verdoppeln", "def verdoppeln(x):\n    return 4\n")
    assert not erg["bestanden"]
    p = erg["pruefung"]
    assert p["sichtbar"][0]["bestanden"] and p["versteckt_fail"] == 2
    assert "628318" not in str(p)


def test_eq_trick_hilft_nicht(client):
    code = (
        "class Immer:\n"
        "    def __eq__(self, o): return True\n"
        "def verdoppeln(x):\n"
        "    return Immer()\n"
    )
    assert not submit(client, "001-verdoppeln", code)["bestanden"]


def test_gefaelschte_ausgabe_hilft_nicht(client):
    code = (
        "import sys\n"
        "def verdoppeln(x):\n"
        "    return 0\n"
        "print('===CODESCHMIEDE_0000000000000000===' + '{\"aufrufe\": []}')\n"
    )
    assert not submit(client, "001-verdoppeln", code)["bestanden"]


def test_erwartungen_gelangen_nicht_in_die_sandbox(client):
    # Der Nutzercode durchsucht den Quelltext seines Aufrufers nach der Erwartung des versteckten Tests.
    code = (
        "import sys\n"
        "def verdoppeln(x):\n"
        "    quelle = str(sys._getframe(1).f_code.co_consts)\n"
        "    return -1 if '628318' in quelle else 2 * x\n"
    )
    erg = submit(client, "001-verdoppeln", code)
    assert erg["bestanden"], erg  # richtig gerechnet; die Erwartung stand nirgends


def test_tupel_ist_nicht_liste(client):
    erg = submit(client, "002-paar", "def paar(a, b):\n    return (a, b)\n")
    assert not erg["bestanden"]
    assert erg["pruefung"]["sichtbar"][0]["tatsaechlich"] == [1, 2]


def test_syntaxfehler(client):
    erg = submit(client, "001-verdoppeln", "def verdoppeln(x)\n    return x\n")
    assert not erg["bestanden"] and "SyntaxError" in erg["pruefung"]["stderr"]


def test_javascript_mit_versteckten_tests(client):
    erg = submit(client, "003-js-summe", "function summe(xs) { return xs.reduce((a, b) => a + b, 0); }")
    assert erg["bestanden"] and erg["pruefung"]["versteckt_pass"] == 2
    erg = submit(client, "003-js-summe", "const summe = (xs) => 6;")
    assert not erg["bestanden"] and erg["pruefung"]["versteckt_fail"] == 2


def test_sql_richtig(client):
    erg = submit(client, "s006-werte", "SELECT wert FROM z ORDER BY id")
    assert erg["bestanden"] and erg["pruefung"]["versteckt_pass"] == 2


def test_sql_eingetippte_werte_fallen_auf(client):
    code = "SELECT 10 AS wert UNION ALL SELECT 20 UNION ALL SELECT 30 UNION ALL SELECT 40 UNION ALL SELECT 50 UNION ALL SELECT 60"
    erg = submit(client, "s006-werte", code)
    assert erg["pruefung"]["sichtbar"][0]["bestanden"]
    assert not erg["bestanden"] and erg["pruefung"]["versteckt_fail"] == 2


def test_sql_attach_verboten(client):
    erg = submit(client, "s006-werte", "ATTACH DATABASE '/tmp/x.db' AS x")
    assert not erg["bestanden"] and "not authorized" in erg["pruefung"]["stderr"]


def test_sql_endlose_rekursion_bricht_ab(client):
    erg = submit(
        client, "s006-werte",
        "WITH RECURSIVE r(n) AS (SELECT 1 UNION ALL SELECT n + 1 FROM r) SELECT n AS wert FROM r",
    )
    assert not erg["bestanden"]


def test_quiz_verraet_die_antwort_nie(client):
    detail = client.get("/api/aufgaben/004-quiz").json()
    assert "richtig_index" not in detail["extra"]["quiz"]
    erg = submit(client, "004-quiz", "0")
    assert not erg["bestanden"] and "1" not in erg["pruefung"]["stderr"]
    assert submit(client, "004-quiz", "1")["bestanden"]


def test_probelauf(client):
    antwort = client.post(
        "/api/submissions/probelauf",
        json={"aufgabe_id": "003-js-summe", "code": "function summe(xs){ console.log('hi'); return xs.length }", "input": [[1, 2]]},
    ).json()
    assert antwort["rueckgabe"] == 2 and antwort["stdout"].strip() == "hi"


def test_css_nur_im_browser(client):
    assert client.post("/api/submissions", json={"aufgabe_id": "c005-knopf", "code": "b{}"}).status_code == 400
    messung = {"deckung": 0.97, "laufzeit_ms": 1}
    antwort = client.post("/api/submissions/lokal", json={"aufgabe_id": "c005-knopf", "code": "b{}", "messung": messung})
    assert antwort.status_code == 200 and antwort.json()["bestanden"]
    antwort = client.post("/api/submissions/lokal", json={"aufgabe_id": "001-verdoppeln", "code": "x", "messung": messung})
    assert antwort.status_code == 400
    # das Ergebnis entscheidet der Server, ein mitgeschicktes Bestehen gibt es nicht mehr
    antwort = client.post("/api/submissions/lokal", json={"aufgabe_id": "c005-knopf", "code": "b{}", "pruefung": {"bestanden": True}})
    assert antwort.status_code == 422
