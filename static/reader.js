function text_size_up() {
	currentSize = parseInt($(".text").css("font-size"));
	if (currentSize < 23) {
		$(".text").css("font-size", currentSize + 2);
	}
}

function text_size_down() {
	currentSize = parseInt($(".text").css("font-size"));
	if (currentSize > 13) {
		$(".text").css("font-size", currentSize - 2);
	}
}
