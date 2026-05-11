function padovan(n) {
    if (n <= 0) return [];
    const folge = [1, 1, 1];
    while (folge.length < n) {
        folge.push(folge[folge.length - 2] + folge[folge.length - 3]);
    }
    return folge.slice(0, n);
}
