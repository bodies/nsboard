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

    $("#font_size_up").click(function() {
        curSize = parseInt($(".text").css("font-size"));
        if (curSize < 21) {
            curSize += 2
            setFontsize(curSize);
            setCookie("font-size", curSize)
         }
         alert("Font size was changed to " + getCookie("font-size"));
    });

    $("#font_size_down").click(function() {
        curSize = parseInt($(".text").css("font-size"));
        if (curSize > 13) {
            curSize -= 2
            setFontsize(curSize);
            setCookie("font-size", curSize);
        }
    });


    /* 추천 시스템 테스트 */
    $("#like_button").click(function() {
        story_num = $(this).data("story-number");
        $.ajax({
            url:'./ajax/like?s=' + story_num,
            success:function(data) {
                if (data == "1") {
                    $(".text").append('<p>추천되었습니다!</p>');
                } else if (data == "2") {
                    alert("이미 추천하셨습니다!")
                } else {
                    alert("잘못된 접근입니다.")
                }

            }
        })
    })

})

function setFontsize(value) {
    $(".text").css("font-size", value);
}

function setCookie(name, value) {
    var date = new Date();
    date.setTime(date.getTime() + 31536000)
    var expires = "; expires=" + date.toGMTString();
    document.cookie = name + "=" + value + expires + "; path=/";
}

function getCookie(name) {
    var search = name + "=";
    var cookie = document.cookie;
    if (cookie.length > 0) {
        startIndex = cookie.indexOf(search);
        if (startIndex != -1) {
            startIndex += name.length;
            endIndex = cookie.indexOf(";", startIndex);
            if (endIndex = -1) endIndex = cookie.length;
            return unescape(cookie.substring(startIndex + 1, endIndex));
        } else {
            return false;
        }
    } else {
        return false;
    }
}