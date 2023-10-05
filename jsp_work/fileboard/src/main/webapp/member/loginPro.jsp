<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="member.*" %>
<%
	// DB member 테이블에 해당 아이디와 비밀번호가 있으면
	// session 이라는 곳에 로그인 정보를 넣어야 합니다.
	request.setCharacterEncoding("utf-8");

	String id = request.getParameter("id");
	String password = request.getParameter("password");
	
	String checkbox = request.getParameter("save");
	
	MemberDAO dao = MemberDAO.getInstance();
	int result = dao.getCheck(id, password);
	if( result == 0 ){
		// checkbox 를 체크 했을때 하는 일...		
		if( checkbox != null && checkbox.equals("on")){		
			Cookie cookie = new Cookie("id",id);
			cookie.setMaxAge(60*20);
			response.addCookie(cookie);
			out.println("쿠키 시간 60*20");
		// checkbox 를 체크 안했을때... 쿠키 시간 설정
		}else{
			Cookie cookie = new Cookie("id",id);
			cookie.setMaxAge(0);
			out.println("쿠키 시간 0");
			response.addCookie(cookie);
		}
		
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
