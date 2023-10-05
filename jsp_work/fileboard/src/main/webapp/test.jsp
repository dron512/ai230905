<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	String cookieid = "";
	String id = (String)session.getAttribute("id");

%>
<%=id%>
<%
	Cookie[] cos = request.getCookies();
	if(cos !=null){
		for(int i =0; i<cos.length;i++){
			if(cos[i].getName().equals("id")){
				cookieid = cos[i].getValue();
			}
		}
	}
%>
<%=cookieid%>