<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
	String str = "기본 예제 입니다.";
	request.setAttribute("message", str);
%>

<%=request.getAttribute("message") %>
</body>
</html>