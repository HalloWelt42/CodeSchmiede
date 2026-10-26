class Pinguin {
  constructor(name, alter) {
    this.name = name;
    this.alter = alter;
  }
  vorstellen() {
    return `Ich bin ${this.name} und ${this.alter} Jahre alt.`;
  }
}
const pit = new Pinguin("Pit", 4);
const pia = new Pinguin("Pia", 5);
console.log(pit.vorstellen());
console.log(pia.vorstellen());
