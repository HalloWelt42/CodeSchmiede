function urlEncode(s) {
    return encodeURIComponent(s).replace(
        /[!*'()]/g,
        (c) => '%' + c.charCodeAt(0).toString(16).toUpperCase()
    );
}
