<%@page import="java.text.SimpleDateFormat"%>
<%@page import="java.util.Date"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" errorPage="error.jsp"%>
<%@ page isErrorPage="true" %>

<%
	Date date = new Date();
	out.println(date);
	out.println("<br/>");
	SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
	String fdate = sdf.format(date);
	out.println(10/0);
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