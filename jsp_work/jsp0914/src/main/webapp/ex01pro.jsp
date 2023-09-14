<%@page import="java.util.List"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="aa.bb.StudentDAO" %>
<%@ page import="aa.bb.StudentDTO" %>
<%
	request.setCharacterEncoding("utf-8");
%>
<jsp:useBean id="dto" class="aa.bb.StudentDTO">
</jsp:useBean>
<jsp:setProperty property="*" name="dto"/>
<%=dto %>

<%
	StudentDTO dto2 = new StudentDTO();
	dto2.setHak(request.getParameter("hak"));
	dto2.setName(request.getParameter("name"));
	dto2.setMajor(request.getParameter("major"));
// 	dto2.setMajor(request.getParameter("major"));

%>
<%
	StudentDAO dao = new StudentDAO();
	dao.insert(dto);
	dao.insert(dto2);
%>