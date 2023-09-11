<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	request.setCharacterEncoding("utf-8");
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
	String strName = request.getParameter("name");
	String strAge = request.getParameter("age");
	int age = Integer.parseInt(strAge);
%>
<%=strName %>
<%=strAge %>
<%  if(age<20) { %>
	나이가 <%=age %>이기 떄문에 미성년자 입니다.
<%	}else{ %>
	나이가 <%=age %>이기 떄문에 성인 입니다.
<%  } %>
</body>
</html>