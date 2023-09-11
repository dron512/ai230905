<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<%!
	String name ="홍길동";
	public String getName(){
		return name;
	}
%>
<%
	String hobby ="달리기";
%>
<%=getName() %>
<%=hobby %>
</body>
</html>