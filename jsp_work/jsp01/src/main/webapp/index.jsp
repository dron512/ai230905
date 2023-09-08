<%@ page language="java" contentType="text/html; charset=EUC-KR" pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<h1>안녕하세요</h1>
JSP 입니다 개발환경 설정은 
1. 이클립스 for web
2. java 17
3. tomcat 9
이렇게 받았습니다...
프로젝트는 dynamic web project 로 만들었구요....
아무렇게나 적으셔도 됩니다.........................
<%
	int a[] = {10,20,30,40,50};
	for (int i =0; i< a.length;i++){
		out.println(a[i]+"<br/>");
	}
%>
</body>
</html>   
