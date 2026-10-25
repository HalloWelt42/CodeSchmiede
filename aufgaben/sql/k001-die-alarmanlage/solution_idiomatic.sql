SELECT zeit
FROM ereignisse
WHERE ort = 'Vitrine'
  AND art = 'geöffnet'
  AND zeit BETWEEN '2026-03-14 18:00' AND '2026-03-14 23:59';
