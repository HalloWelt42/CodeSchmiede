function zaehleBuchstaben(text) {
    const z = [...text.toLowerCase()].reduce((akk, c) => {
        if (c >= 'a' && c <= 'z') {
            akk[c] = (akk[c] || 0) + 1;
        }
        return akk;
    }, {});
    // Keys alphabetisch -- damit JSON-Vergleich deterministisch ist.
    return Object.fromEntries(Object.entries(z).sort());
}
