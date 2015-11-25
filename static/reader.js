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

    $("#like_button").click(function() {
        story_num = $(this).data("story-number");
        $.ajax({
            url:"/ajax/like?s=" + story_num,
            success:function(data) {
                if (data == "1") {
                    $("#like-count").text(parseInt($("#like-count").text()) + 1);
                } else if (data == "2") {
                    alert("이미 추천하셨습니다!");
                } else {
                    alert("추천 기능을 사용할 수 없습니다.")
                }
            }
        })
    })
})

function setFontsize(value) {
    $(".text").css("font-size", value);
}