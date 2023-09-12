<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="jsp0912.DBManager" %>
<%
	out.println(DBManager.aa);
	DBManager db = new DBManager();
	out.println(db.bb);
	//한글처리
	request.setCharacterEncoding("UTF-8");

	String strId = request.getParameter("id");
	String strPassword = request.getParameter("password");
	
	out.println("strId = "+strId);
	out.println("strPassword = "+strPassword);
	
	boolean result = db.doInsert(strId, strPassword);
	if(result){
		out.println("Insert 되었습니다.");
	}
	
%>