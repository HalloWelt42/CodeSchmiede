const zahlen = [1, 2, 3, 4, 5];
console.log("Summe:", zahlen.reduce((s, x) => s + x, 0));
console.log("Produkt:", zahlen.reduce((p, x) => p * x, 1));
