<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<div>
	<c:set var="a" value="10"/>
	${a}
	<c:out value="100"/>
</div>
<%@ include file="top.jsp" %>

<h1>박명회</h1>
<%
	int a = 10;
	out.print("a = "+a);
	out.print("aa = "+aa);
	String b = "b입니다....";
%>
<div>
	<c:set var="aaa" value="<%=b %>"/>
	${aaa}
</div>
<%@ include file="bottom.jsp" %>

</body>
</html>







