function fizzbuzzListe(n) {
    if (n <= 0) return [];
    return Array.from({ length: n }, (_, i) => {
        const k = i + 1;
        if (k % 15 === 0) return "FizzBuzz";
        if (k % 3 === 0) return "Fizz";
        if (k % 5 === 0) return "Buzz";
        return String(k);
    });
}
