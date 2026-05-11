function potenzmenge(arr) {
    const n = arr.length;
    const out = [];
    for (let m = 0; m < 2 ** n; m++) {
        const subset = [];
        for (let i = 0; i < n; i++) {
            if (m & (1 << i)) subset.push(arr[i]);
        }
        out.push(subset);
    }
    return out.sort((a, b) =>
        a.length - b.length || JSON.stringify(a).localeCompare(JSON.stringify(b))
    );
}
