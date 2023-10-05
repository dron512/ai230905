<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="member.*" %>
<%
	// DB member 테이블에 해당 아이디와 비밀번호가 있으면
	// session 이라는 곳에 로그인 정보를 넣어야 합니다.
	request.setCharacterEncoding("utf-8");

	String id = request.getParameter("id");
	String password = request.getParameter("password");
	
	MemberDAO dao = MemberDAO.getInstance();
	int result = dao.getCheck(id, password);
	if( result == 0 ){
		session.setAttribute("id", id);
%>
	<script>
		alert('로그인성공');
		location.href='../select.jsp';
	</script>

<%
	}else{
%>
	<script>
		alert('로그인실패');
		location.href='../select.jsp';
	</script>
<%	
	}
%>
