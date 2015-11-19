function setCookie(name, value) {
    var date = new Date();
    date.setTime(date.getTime() + 31536000);
    document.cookie = name + "=" + value + "; expires=" + date.toGMTString + "; path=/";
}

function getCookie(name) {
    var cookie = document.cookie;
    if (cookie.length > 0) {
        startIndex = cookie.indexOf(name + "=");
        if (startIndex != -1) {
            startIndex += name.length;
            endIndex = cookie.indexOf(";", startIndex);
            if (endIndex = -1) endIndex = cookie.length;
            return unescape(cookie.substring(startIndex + 1, endIndex));
        } else { return false; }
    } else { return false; }
}