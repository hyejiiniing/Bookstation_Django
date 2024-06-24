// qna_content 글자 최대 범위
function countCharacters() {
    const textarea = document.getElementById('qna_content');
    const charCountSpan = document.getElementById('charCount');
    const maxChars = 1500;
    let charCount = (textarea.value.length)*2;
    
    if (charCount > maxChars) {
        textarea.value = textarea.value.substring(0, maxChars);
        charCount = maxChars;
    }
    charCountSpan.textContent = charCount;
}

// 유효성 검사
function validateForm() {
    var isValid = true;

    // qna_title 유효성 검사
    var title = document.getElementById('qna_title').value;
    var titleError = document.getElementById('titleError');
    if (title.trim() === "") {
        titleError.innerText = "제목을 입력해주세요.";
        isValid = false;
    } else {
        titleError.innerText = "";
    }

    // qna_content 유효성 검사
    var content = document.getElementById('qna_content').value;
    var contentError = document.getElementById('contentError');
    if (content.trim() === "") {
        contentError.innerText = "내용을 입력해주세요.";
        isValid = false;
    } else if (content.length > 1500) {
        contentError.innerText = "내용은 1500자를 초과할 수 없습니다.";
        isValid = false;
    } else {
        contentError.innerText = "";
    }
    return isValid;
}