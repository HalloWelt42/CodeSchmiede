function generalFizzbuzz(n, regeln) {
    if (n <= 0) return [];
    return Array.from({ length: n }, (_, i) => {
        const k = i + 1;
        const wort = regeln
            .filter(([t]) => k % t === 0)
            .map(([, w]) => w)
            .join("");
        return wort || String(k);
    });
}
