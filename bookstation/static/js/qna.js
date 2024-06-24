// 삭제 버튼을 눌렀을 때 호출되는 함수
function deleteRow(button) {
    // 버튼이 속한 행을 찾아서 삭제
    var row = button.parentNode.parentNode;
    row.parentNode.removeChild(row);
}