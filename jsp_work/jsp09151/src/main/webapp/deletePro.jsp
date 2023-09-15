<%@page import="jsp09151.MemberDAO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	MemberDAO dao = new MemberDAO();
	
	String idx = request.getParameter("idx");

	if (idx == null){
		out.println("idx를 입력 하셔야 됩니다.");	
	}
	else{
		boolean succes= dao.delete(Integer.parseInt(idx));
		out.println(succes);
		if(succes)
			response.sendRedirect("index.jsp");
		else
			response.sendRedirect("deleteForm.jsp");
	}
	
%>