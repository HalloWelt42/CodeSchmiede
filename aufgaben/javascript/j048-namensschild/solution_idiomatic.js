const vorname = "pia";
const nachname = "Pinguin";
const gross = vorname[0].toUpperCase() + vorname.slice(1);
const name = `${gross} ${nachname}`;
console.log(`Name: ${name}`);
console.log(`Kürzel: ${gross[0]}${nachname[0]}`);
console.log(`Zeichen: ${name.length}`);
console.log("=".repeat(name.length));
