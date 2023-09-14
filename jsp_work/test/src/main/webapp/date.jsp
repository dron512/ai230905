<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page isErrorPage="true" %>
<%@ page errorPage="error.jsp" %>
<%@page import="java.text.SimpleDateFormat"%>
<%@page import="java.util.Date"%>

<%
	Date date = new Date();
	out.println(date);
	out.println("<br/>");
	SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
	String fdate = sdf.format(date);
// 	out.println(fdat);
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>date.jsp</h1>
</body>
</html>