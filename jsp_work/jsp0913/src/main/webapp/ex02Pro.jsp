<%@page import="java.util.Enumeration"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	String pass = request.getParameter("password");
	String[] ids = request.getParameterValues("id");
	
	out.println(ids[0]);
	out.println(ids[1]);
	out.println(ids[2]);
	out.println(ids[3]);
	
	String[] idxs = request.getParameterValues("idx");
	
	out.println("idxs = "+ idxs);
	
	if ( idxs != null){
		for (String temp : idxs){
			out.println(temp);
		}
	}
	
	Enumeration<String> enums = request.getParameterNames();
	while(enums.hasMoreElements()){
		out.println(enums.nextElement());
	}
	out.println("요청한 ip = ");
	out.println(request.getRemoteAddr());
%>















