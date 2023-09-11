<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="jsp0911.Member" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
	Member member= new Member();
	Member member2= new Member("dron512","password",39);
	Member member3= new Member("12asdf","password",45);

	// _jspService 메서드 안에 
%>
<%=member.id %>님의 비밀번호는 <%=member.passwd %>이고, 나이는 <%=member.age %>입니다<br/>
<%=member2.id %>님의 비밀번호는 <%=member2.passwd %>이고, 나이는 <%=member2.age %>입니다<br/>
<%=member3.id %>님의 비밀번호는 <%=member3.passwd %>이고, 나이는 <%=member3.age %>입니다<br/>
</body>
</html>