$(function() {
	// 하루 버튼 
    $("#oneDayBtn").click(function() {
		fetchOrderData(1);
        alert("하루 버튼 클릭됨");
    });

	//일주일 버튼 
    $("#oneWeekBtn").click(function() {
		fetchOrderData(7);
        alert("일주일 버튼 클릭됨");
    });

	//1개월 버튼 
    $("#oneMonthBtn").click(function() {
		fetchOrderData(30);		
        alert("1개월 버튼 클릭됨");
    });

	//3개월 버튼
    $("#threeMonthsBtn").click(function() {
		fetchOrderData(90);		
        alert("3개월 버튼 클릭됨");
        // 3개월 버튼 클릭
    });

    $("#searchBtn").click(function() {
        var fromDate = $("#fromDate").val();
        var toDate = $("#toDate").val();
        fetchOrderData(null, fromDate, toDate);
        alert("검색 버튼 클릭됨: From " + fromDate + " To " + toDate);
        // 검색 버튼 클릭
    });
});

$(document).ready(function() {
    // 검색 버튼 클릭 이벤트 핸들러
    $("#searchBtn").click(function() {
        var fromDate = $("#fromDate").val();
        var toDate = $("#toDate").val();
        fetchOrderData(null, fromDate, toDate);
    });

    // 1개월 버튼 클릭 이벤트 핸들러
    $("#oneMonthBtn").click(function() {
        fetchOrderData(30); // 1개월은 30일로 간주
    });

    // 일주일 버튼 클릭 이벤트 핸들러
    $("#oneWeekBtn").click(function() {
        fetchOrderData(7); // 일주일은 7일
    });

    // 하루 버튼 클릭 이벤트 핸들러
    $("#oneDayBtn").click(function() {
        fetchOrderData(1); // 하루는 1일
    });

    // 3개월 버튼 클릭 이벤트 핸들러
    $("#threeMonthsBtn").click(function() {
        fetchOrderData(90); // 3개월은 90일
    });
});

function fetchOrderData(days, fromDate, toDate) {
    var requestData = {};
    if (days) {
        requestData.days = days;
    } else {
        requestData.fromDate = fromDate;
        requestData.toDate = toDate;
    }

    $.ajax({
        url: '/fetchOrderData', // 서버의 엔드포인트
        type: 'POST',
        data: JSON.stringify(requestData),
        contentType: 'application/json',
        success: function(response) {
            updateOrderTable(response);
        },
        error: function(xhr, status, error) {
            console.error("데이터를 가져오는 중 오류 발생:", error);
        }
    });
}

function updateOrderTable(data) {
    var tableBody = $("#orderTable tbody");
    tableBody.empty();

    data.forEach(function(order) {
        var row = "<tr>" +
            "<td>" + order.orderId + "</td>" +
            "<td>" + order.date + "</td>" +
            "<td>" + order.item + "</td>" +
            "<td>" + order.amount + "</td>" +
            "</tr>";
        tableBody.append(row);
    });
}