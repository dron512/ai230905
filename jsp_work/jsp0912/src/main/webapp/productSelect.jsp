<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="jsp0912.Product" %>
<%@ page import="java.util.List"%>
<%@ page import="jsp0912.DBProductManager"%>
<%
	DBProductManager dbm = new DBProductManager();
	List<Product> list = dbm.doSelect();
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h1>select</h1>
	<%=list %>
</body>
</html>