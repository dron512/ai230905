<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
// 세션 모든값 삭제
// 	session.invalidate();
	session.removeAttribute("id");
%>

<script>
	alert('로그아웃하셨습니다.');
	location.href='../select.jsp';
</script>