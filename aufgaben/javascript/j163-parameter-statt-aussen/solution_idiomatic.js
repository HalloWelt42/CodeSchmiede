function netto(brutto, satz = 19) {
  return brutto / (1 + satz / 100);
}
console.log(`100 Euro brutto sind ${netto(100).toFixed(2)} Euro netto`);
console.log(`100 Euro brutto sind ${netto(100, 7).toFixed(2)} Euro netto`);
