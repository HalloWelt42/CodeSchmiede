function gleichgewicht(arr) {
    const gesamt = arr.reduce((a, x) => a + x, 0);
    let links = 0;
    const out = [];
    for (let i = 0; i < arr.length; i++) {
        const rechts = gesamt - links - arr[i];
        if (links === rechts) out.push(i);
        links += arr[i];
    }
    return out;
}
