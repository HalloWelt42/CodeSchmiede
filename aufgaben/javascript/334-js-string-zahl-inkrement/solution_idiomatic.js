function inkrement(s) {
    try {
        return (BigInt(s) + 1n).toString();
    } catch {
        return "";
    }
}
