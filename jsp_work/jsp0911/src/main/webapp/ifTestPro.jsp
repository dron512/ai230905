<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" errorPage="error.jsp"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>입력한 값이 10보다 작은지 비교</h1>

<%
	String strNumber = request.getParameter("number");
	int num = Integer.parseInt(strNumber);
%>
<%=num %><br/>
<%
	if(num < 10){
%>
	<%=num %>은 10보다 작습니다.
<%
// 		out.println(num+" 은 10 보다 작습니다.");
	}
%>
</body>
</html>