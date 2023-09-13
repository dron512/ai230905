<%@page import="jsp0912.DBProductManager"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%

	request.setCharacterEncoding("UTF-8");

	String name = request.getParameter("name");
	int quan = Integer.parseInt(request.getParameter("quan"));

	DBProductManager dbm = new DBProductManager();
	boolean result = dbm.doInsert(name, quan);
	
	if(result)
		out.println("insert 되었습니다.");

%>