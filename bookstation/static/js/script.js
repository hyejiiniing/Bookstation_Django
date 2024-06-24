/* ------------------------------ order.jsp ------------------------------ */
/* 우편번호 검색 */
function sample6_execDaumPostcode() {
    new daum.Postcode({
        oncomplete: function(data) {
            // 팝업에서 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분.

            // 각 주소의 노출 규칙에 따라 주소를 조합한다.
            // 내려오는 변수가 값이 없는 경우엔 공백('')값을 가지므로, 이를 참고하여 분기 한다.
            var addr = ''; // 주소 변수
            var extraAddr = ''; // 참고항목 변수

            // 사용자가 선택한 주소 타입에 따라 해당 주소 값을 가져온다.
            if (data.userSelectedType === 'R') { // 사용자가 도로명 주소를 선택했을 경우
                addr = data.roadAddress;
            } else { // 사용자가 지번 주소를 선택했을 경우(J)
                addr = data.jibunAddress;
            }

            // 우편번호와 주소 정보를 해당 필드에 넣는다.
            document.getElementById('memberAddr1').value = data.zonecode;
            document.getElementById('memberAddr2').value = addr;
            // 상세주소 입력란에 포커스 설정
            document.getElementById('memberAddr3').focus();
        }
    }).open();
}

// 주소 유효성 검사 함수
function validateAddress() {
    const memberAddr1 = $('#memberAddr1').val();
    const memberAddr2 = $('#memberAddr2').val();
    const memberAddr3 = $('#memberAddr3').val();
    if (isEmpty(memberAddr1) || isEmpty(memberAddr2) || isEmpty(memberAddr3)) {
        alert('주소를 완전히 입력하세요.');
        let focusField = isEmpty(memberAddr1) ? 'memberAddr1' : isEmpty(memberAddr2) ? 'memberAddr2' : 'memberAddr3';
        $('#' + focusField).focus(); // 입력 필드에 포커스 설정
        return false; // 주소가 완전히 입력되지 않았으므로 false 반환
    }
    return true; // 주소가 모두 입력되었으므로 true 반환
}

/* 유효성 검사 */ 
$(document).ready(function() {
    // 값이 비어 있는지 확인하는 유틸리티 함수
    function isEmpty(value) {
        return !value || value.trim() === '';
    }

    // 유효성 검사 함수
    function validateOrder() {
        let isValid = true; // 유효성 검사 플래그

        // 이름 유효성 검사
        const orderName = $('#order_name').val();
        if (isEmpty(orderName)) {
            alert('이름을 입력하세요.');
            $('#order_name').focus(); // 입력 필드에 포커스 설정
            isValid = false;
            return isValid;
        }

        // 전화번호 유효성 검사
       const phoneNumber = $('#phone_num').val().replace(/[^0-9]/g, "");
			if (isEmpty(phoneNumber)) {
			    alert('휴대 전화번호를 완전히 입력하세요.');
			    $('#phone_num').focus(); // 해당 입력 필드에 포커스 설정
			    return false;
			}

        // 무통장 입금일 때 유효성 검사
        if ($('#bank-transfer').is(':checked')) {
            // 입금은행 선택 유효성 검사
            const depositBank = $('select[name="bank"]').val();
            if (depositBank === '0') {
                alert('입금은행을 선택하세요.');
                $('select[name="bank"]').focus(); // 선택 박스에 포커스 설정
                isValid = false;
                return isValid;
            }

            // 입금자 유효성 검사
            const depositor = $('#order_name2').val();
            if (isEmpty(depositor)) {
                alert('입금자를 입력하세요.');
                $('#order_name2').focus(); // 입력 필드에 포커스 설정
                isValid = false;
                return isValid;
            }
        }

        // 카드 결제일 때 추가 유효성 검사
        if ($('#card-payment').is(':checked')) {
            // 카드사 선택 유효성 검사
            const cardCompany = $('select[name="card"]').val();
            if (cardCompany === '0') {
                alert('카드사를 선택하세요.');
                $('select[name="card"]').focus(); // 선택 박스에 포커스 설정
                isValid = false;
                return isValid;
            }
        
            // 생년월일 유효성 검사
            const birthYear = $('#birth-year').val().trim();
            const birthMonth = $('#birth-month').val().trim();
            const birthDay = $('#birth-day').val().trim();
            if (isEmpty(birthYear) || isEmpty(birthMonth) || isEmpty(birthDay)) {
                alert('생년월일을 완전히 입력하세요.');
                let focusField = isEmpty(birthYear) ? 'birth-year' : isEmpty(birthMonth) ? 'birth-month' : 'birth-day';
                $('#' + focusField).focus(); // 포커스 설정
                isValid = false;
                return isValid;
            }

            // 카드번호 유효성 검사
            const cardNumbers = ['card1', 'card2', 'card3', 'card4'].map(field => $('#' + field).val().trim());
            if (cardNumbers.some(num => isEmpty(num))) {
                alert('카드번호를 모두 입력하세요.');
                let focusField = cardNumbers.findIndex(num => isEmpty(num));
                $('#' + cardNumbers[focusField]).focus();
                isValid = false;
                return isValid;
            }

            // CVC 유효성 검사
            const cvc = $('#cvc').val().trim();
            if (isEmpty(cvc)) {
                alert('CVC 번호를 입력하세요.');
                $('#cvc').focus(); // 입력 필드에 포커스 설정
                isValid = false;
                return isValid;
            }

            // 카드 유효기간 유효성 검사
            const expMonth = $('#exp-month').val().trim();
            const expYear = $('#exp-year').val().trim();
            if (isEmpty(expMonth) || isEmpty(expYear)) {
                alert('카드 유효기간을 완전히 입력하세요.');
                let focusField = isEmpty(expMonth) ? 'exp-month' : 'exp-year';
                $('#' + focusField).focus();
                isValid = false;
                return isValid;
            }

            // 카드 비밀번호 앞 두 자리 유효성 검사
            const password2Digits = $('#password-2-digits').val().trim();
            if (isEmpty(password2Digits)) {
                alert('카드 비밀번호 앞 두 자리를 입력하세요.');
                $('#password-2-digits').focus(); // 포커스 설정
                isValid = false;
                return isValid;
            }
        }

        return isValid; // 모든 유효성 검사 통과
    }

    $('#order_button').click(function(event) {
        event.preventDefault(); // 기본 동작 방지
        if (validateOrder()) {
            // 모든 유효성 검사 통과 후 모달 창 열기
            $('.modal-backdrop').fadeIn(); 
            $('.modal-order').fadeIn();
        }
    });

    // 모달 닫기 이벤트 처리
    $('.js-hide-modal').click(function() {
        $('.modal-backdrop').fadeOut();
        $('.modal-order').fadeOut();
    });

    // 모달 창 내부 클릭 시 이벤트 전파 방지
    $('.modal-order').on('click', function(e) {
        e.stopPropagation(); // 이벤트 전파 방지
    });

    /* 결제 방법 선택 */
    function togglePaymentMethod() {
        if ($('#card-payment').is(':checked')) {
            $('#payment-method').show(); // 카드 결제 정보 표시
            $('.bank-transfer-info').hide(); // 무통장 입금 정보 숨기기
        } else if ($('#bank-transfer').is(':checked')) {
            $('#payment-method').숨김
            $('.bank-transfer-info').show(); // 무통장 입금 정보 표시
        }
    }

    // 초기 상태에서 토글 설정
    togglePaymentMethod();

    // 결제 방식 라디오 버튼 변경 시 토글 설정
    $('input[name="shipping-method"]').change(function() {
        togglePaymentMethod();
    });
});

/* 결제 방법 선택 */
$(document).ready(function() {
    function togglePaymentMethod() {
        if ($('#card-payment').is(':checked')) {
            $('#payment-method').show(); // 카드 결제 정보 표시
            $('.bank-transfer-info').hide(); // 무통장 입금 정보 숨기기
        } else if ($('#bank-transfer').is(':checked')) {
            $('#payment-method').hide(); // 카드 결제 정보 숨기기
            $('.bank-transfer-info').show(); // 무통장 입금 정보 표시
        }
    }

    // 초기 상태에서 토글 설정
    togglePaymentMethod();

    // 결제 방식 라디오 버튼 변경 시 토글 설정
    $('input[name="payOption1"]').change(function() {
        togglePaymentMethod();
    });
});

// 전화번호 자동 하이픈(-) 넣어주는 코드와 전화번호 길이 제한 함수
$(document).on("keyup", "#phone_num", function() {
    const phoneNumber = $(this).val().replace(/[^0-9]/g, "");
    const formattedNumber = phoneNumber.replace(/(^02|^0505|^1[0-9]{3}|^0[0-9]{2})([0-9]+)?([0-9]{4})$/, "$1-$2-$3" ).replace("--", "-");
    $(this).val(formattedNumber); 
    limitPhoneNumberLength(this);
});

// 전화번호 길이 제한 함수
function limitPhoneNumberLength(inputField){
    const maxLength = 13;
    if(inputField.value.length > maxLength) {
        inputField.value = inputField.value.slice(0, maxLength);	
    }
}

/* 장바구니 삭제 */
function deleteCart(cart_id, member_id) {
            const form = document.createElement('form');
            form.method = 'POST';
            form.action = 'deletecart.do';

            const cartIdField = document.createElement('input');
            cartIdField.type = 'hidden';
            cartIdField.name = 'cart_id';
            cartIdField.value = cart_id;
            form.appendChild(cartIdField);

            const memberIdField = document.createElement('input');
            memberIdField.type = 'hidden';
            memberIdField.name = 'member_id';
            memberIdField.value = member_id;
            form.appendChild(memberIdField);

            document.body.appendChild(form);
            form.submit();
        }
   
   $(document).ready(function() {
            // 페이지가 로드될 때 /cartCount 엔드포인트에 GET 요청을 보냄
            $.ajax({
                url: '/cartCount',
                method: 'GET',
                success: function(data) {
                    // data-notify 속성을 업데이트
                    $('.icon-header-noti').attr('data-notify', data);
                },
                error: function() {
                    console.error('Failed to fetch cart count.');
                }
            });
        });