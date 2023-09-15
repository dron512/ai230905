<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%-- <%@page import="jsp0915.ExBean"%> --%>
<%
	request.setCharacterEncoding("UTF-8");
/*
	ExBean exBean = new ExBean(); 
	exBean.setId(request.getParameter("id"));
	exBean.setPassword(request.getParameter("password"));
	exBean.setNumber(Integer.parseInt(request.getParameter("number")));
*/
%>

<jsp:useBean id="exBean" class="jsp0915.ExBean"></jsp:useBean>
<jsp:setProperty property="*" name="exBean"/>

<%=exBean%>