function zaehlerBauen(start, schritt) {
  let wert = start - schritt;
  return () => {
    wert += schritt;
    return wert;
  };
}
const fuenfer = zaehlerBauen(10, 5);
console.log(fuenfer(), fuenfer(), fuenfer());
const runter = zaehlerBauen(0, -2);
console.log(runter(), runter(), runter(), runter());
