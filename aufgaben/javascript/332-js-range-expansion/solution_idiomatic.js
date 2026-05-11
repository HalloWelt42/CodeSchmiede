function bereichEntpacken(s) {
    if (!s) return [];
    const out = [];
    for (const stueck of s.split(",")) {
        const idx = stueck.indexOf("-", 1);
        if (idx > 0) {
            const a = parseInt(stueck.slice(0, idx), 10);
            const b = parseInt(stueck.slice(idx + 1), 10);
            for (let i = a; i <= b; i++) out.push(i);
        } else {
            out.push(parseInt(stueck, 10));
        }
    }
    return out;
}
