// 이용약관 동의에서 필수 항목을 모두 체크시에만 다음 버튼이 활성화
$('.agree').change(function() { // 각 동의 체크박스 변경 시 다음 버튼 상태 업데이트
    updateNextButtonState();
});

$('#allAgree').change(function() { // 전체 동의하기 체크박스 변경 시 다음 버튼 상태 업데이트
    if ($(this).is(':checked')) {
        $('.agree').prop('checked', true);
    } else {
        $('.agree').prop('checked', false);
    }
    updateNextButtonState();
});

function updateNextButtonState() { // 다음 버튼 상태 업데이트 함수
    var required1Checked = $('#required1').is(':checked');
    var required2Checked = $('#required2').is(':checked');
    var required3Checked = $('#required3').is(':checked');

    if (required1Checked && required2Checked && required3Checked) {
        $('#nextbutton').prop('disabled', false);
    } else {
        $('#nextbutton').prop('disabled', true);
    }
}

// 생년월일 0000-00-00형식으로 받아주는 코드
function formatDate(input) {
    var value = $(input).val().replace(/[^\d]/g, '');
    var formattedDate = '';
    if (value.length > 0) {
        var year = value.substring(0, 4);
        var month = value.substring(4, 6);
        var day = value.substring(6, 8);
        formattedDate = year;
        if (month) {
            formattedDate += '-' + month;
            if (day) {
                formattedDate += '-' + day;
            }
        }
    }
    $(input).val(formattedDate);
}

// 전화번호 자동 하이픈(-) 넣어주는 코드
$(document).on("keyup", "#phone", function() {
    $(this).val($(this).val().replace(/[^0-9]/g, "").replace(/(^02|^0505|^1[0-9]{3}|^0[0-9]{2})([0-9]+)?([0-9]{4})$/, "$1-$2-$3" ).replace("--", "-")); 
});
function numberphone(e){
    if(e.value.length>13){
    e.value=e.value.slice(0,13);    
    }
}

// 입력만 하면 다음 버튼 활성화
$(function() {
    $('#userId, #userPwd, #rePwd, #userName, #birth, #userEmail').on('input', function() {
        updateNextButtonState2();
    });

    function updateNextButtonState2() {
        var allFilled = true;

        if ($('#userId').val() === '' || $('#userPwd').val() === '' || $('#rePwd').val() === '' ||
            $('#userName').val() === '' || $('#birth').val() === '' || $('#userEmail').val() === '') {
            allFilled = false;
        }

        if (allFilled) {
            $('#nextbutton2').prop('disabled', false);
        } else {
            $('#nextbutton2').prop('disabled', true);
        }
    }
});

// 비밀번호 변경 버튼 클릭 시 실행될 함수
function changePassword() {
    alert("비밀번호 변경이 완료되었습니다. 로그인해 주세요.");
    return true;
}
