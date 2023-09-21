<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="aa.bb.Test" %>
<%@ page import="aa.bb.FreeBoardDAO" %>
<%
    Test test = new Test();
    test.doA();
    FreeBoardDAO dao = new FreeBoardDAO();
    dao.con();
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>a.jsp</h1>
</body>
</html>