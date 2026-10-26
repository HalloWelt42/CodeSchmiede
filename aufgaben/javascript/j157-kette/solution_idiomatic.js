const namen = ["Pia", "Gustav", "Ole", "Paula", "Kim", "Frieda"];
console.log(namen.filter(n => n.length > 3).map(n => n.toUpperCase()).sort().join(", "));
