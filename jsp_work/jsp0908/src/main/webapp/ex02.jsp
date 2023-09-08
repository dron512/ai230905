<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

<h1>129page 문제 3번</h1>
<h1>166page 문제 3번 ,4번 </h1>

ctrl+ shift +c 주석처리 ...
<%!
	// ex02_jsp.java 클래스 안에 들어간다...
	String a = "안녕하세요";
	public String doA(){
		System.out.println("콘솔창에 출력됩니다.");
		return a;
	}
%>
<%
// ex02_jsp.java _jspservice 라는 메서드 안에 들어간다...
// 	int bbb = 20;
// 	out.println(bbb);
%>
<%
	out.println("test");
%>
<%="test" %>

</body>
</html>


