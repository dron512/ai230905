<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@page import="jsp09151.MemberDAO"%>
<jsp:useBean id="dto" class="jsp09151.MemberDTO">
</jsp:useBean>
<jsp:setProperty property="*" name="dto" />

<%
	MemberDAO dao = MemberDAO.getInstance();
	System.out.println(dao);

	boolean result = dao.update(dto);
	out.println(result);
	if(result)
		response.sendRedirect("index.jsp");
	else
		response.sendRedirect("updateForm.jsp");
%>