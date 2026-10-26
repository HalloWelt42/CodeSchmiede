const tag = prompt("Tag? ");
const ruhetag = tag === "Montag" || tag === "Dienstag";
console.log("Ruhetag:", ruhetag);
console.log("Geöffnet:", !ruhetag);
