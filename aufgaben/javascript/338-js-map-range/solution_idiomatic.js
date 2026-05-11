function mapRange(x, a1, a2, b1, b2) {
    if (a1 === a2) return b1;
    const y = b1 + (x - a1) * (b2 - b1) / (a2 - a1);
    return Math.round(y * 10000) / 10000;
}
