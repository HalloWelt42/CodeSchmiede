function tau(n) {
    if (n < 1) return 0;
    let z = 0;
    for (let i = 1; i * i <= n; i++) {
        if (n % i === 0) {
            z += (i * i === n) ? 1 : 2;
        }
    }
    return z;
}
