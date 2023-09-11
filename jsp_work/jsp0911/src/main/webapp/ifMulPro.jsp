<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="jsp0911.Member" %>
<%
	request.setCharacterEncoding("utf-8");
	String name = request.getParameter("name");
	String local = request.getParameter("local");
	String tel = request.getParameter("tel");
	Member member = new Member(name,local,tel);
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<%=member%>	
</body>
</html>