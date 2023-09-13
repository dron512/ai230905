<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<%
// 		response.sendRedirect("cc.jsp");
		out.println(session.getAttribute("id"));
// 		request.getParameter("id");
	%>
</body>
</html>