function fischen(name, ms, fische) {
  return new Promise((erfuellen) => {
    setTimeout(() => {
      console.log(`zurück: ${name}`);
      erfuellen(`${name} ${fische}`);
    }, ms);
  });
}
async function ausflug() {
  const fang = await Promise.all([fischen("Pit", 20, 3), fischen("Pia", 5, 5), fischen("Paul", 40, 2)]);
  console.log(`Fang: ${fang.join(", ")}`);
}
ausflug();
