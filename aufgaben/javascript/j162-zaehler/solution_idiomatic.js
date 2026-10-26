function zaehlerBauen() {
  let stand = 0;
  return () => {
    stand++;
    return stand;
  };
}
const klick = zaehlerBauen();
console.log(klick(), klick(), klick());
const neu = zaehlerBauen();
console.log(neu());
