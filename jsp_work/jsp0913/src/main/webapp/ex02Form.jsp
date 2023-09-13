<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	out.println(session.getAttribute("id"));
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<form method="post" action="ex02Pro.jsp">
		id : <input type="text" name="id"/>
		id : <input type="text" name="id"/>
		id : <input type="text" name="id"/>
		id : <input type="text" name="id"/>
		삭제 할 행 지정
		<input type="checkbox" name="idx" value="1">
		<input type="checkbox" name="idx" value="2">
		<input type="checkbox" name="idx" value="3">
		password : <input type="text" name="password"/>
		<input type="submit" value="전송"/>
	</form>
</body>
</html>