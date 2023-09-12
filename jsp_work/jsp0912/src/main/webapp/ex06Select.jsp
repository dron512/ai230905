
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="jsp0912.DBManager" %>
<%@ page import="jsp0912.Member" %>
<%@ page import="java.util.List"%>
<%
	DBManager db = new DBManager();
	List<Member> list = db.doSelect();
	
// 	out.println(list);
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
	for ( int i =0; i<list.size(); i++){
		out.println(list.get(i)+"<br>");
	}
%>

</body>
</html>