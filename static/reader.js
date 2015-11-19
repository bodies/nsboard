$(function() {
    var cSize = parseInt(getCookie("font-size"));
    if (cSize > 14 && cSize < 22) {
        setFontsize(cSize);
    } else {
        setFontsize(15);
    }

    $("#change-font-size").click(function() {
        curSize = parseInt($(".text").css("font-size"));
        if (curSize < 18) {
            curSize = 18;
        } else if (curSize < 21) {
            curSize = 21;
        } else {
            curSize = 15;
        }
        setFontsize(curSize);
        setCookie("font-size", curSize);
    })
})

function setFontsize(value) {
    $(".text").css("font-size", value);
}