function summeQuadrate(n) {
    if (n <= 0) return 0;
    return Math.floor((n * (n + 1) * (2 * n + 1)) / 6);
}
