function josephus(n, k) {
    if (n <= 0 || k <= 0) return -1;
    let j = 0;
    for (let i = 2; i <= n; i++) {
        j = (j + k) % i;
    }
    return j;
}
