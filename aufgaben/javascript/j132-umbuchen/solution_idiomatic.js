const lager = new Map();
lager.set("Hering", 12);
lager.set("Aal", 3);
lager.set("Hering", lager.get("Hering") - 3);
lager.delete("Aal");
console.log(lager);
