const lager = new Map();
lager.set("Hering", 12);
lager.set("Aal", 3);
console.log("Hering:", lager.get("Hering"));
console.log("Sorten:", lager.size);
console.log("Lachs da:", lager.has("Lachs"));
