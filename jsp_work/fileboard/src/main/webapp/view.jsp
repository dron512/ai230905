<%@page import="fileboard.FileBoardDTO"%>
<%@page import="fileboard.FileBoardDAO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	String idx = request.getParameter("idx");

	FileBoardDAO dao = FileBoardDAO.getInstance();
	FileBoardDTO dto = dao.selectONE(Integer.parseInt(idx));
	
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>View</h1>
<%=dto %>
</body>
</html>