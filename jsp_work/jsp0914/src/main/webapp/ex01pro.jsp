<%@page import="java.util.List"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="jsp0914.StudentDAO" %>
<%@ page import="jsp0914.StudentDTO" %>
<%
	request.setCharacterEncoding("utf-8");
%>
<%
	String hak = request.getParameter("hak");
	String name = request.getParameter("name");
	String major = request.getParameter("major");
%>
학번<%=hak %><br/>
이름<%=name %><br/>
전공<%=major %><br/>
<%
	StudentDAO sdao = new StudentDAO();
	sdao.insert(new StudentDTO(hak,name,major));
	
	List<StudentDTO> list=sdao.select();
	out.println(list);
%>
