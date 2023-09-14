<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	String pageName = "out01.jsp";

%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>in01.jsp</h1>
<hr>
<jsp:include page="<%=pageName %>">
	<jsp:param value="10" name="a"/>
	<jsp:param value="20" name="b"/>
</jsp:include>
<hr>
<h1>밑에...</h1>
</body>
</html>