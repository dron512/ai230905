<%@page import="freeboard.FreeBoardDAO"%>
<%@page import="freeboard.FreeBoardDTO"%>
<%@page import="java.util.List"%>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
	FreeBoardDAO dao1 = FreeBoardDAO.getInstance();
	List<FreeBoardDTO> list = dao1.select();
%>
<table border="1">
	<tr>
		<th>idx</th>
		<th>title</th>
		<th>name</th>
		<th>wdate</th>
	</tr>
	<tr>
		<td>1</td>
		<td>2</td>
		<td>3</td>
		<td>4</td>
	</tr>
	<%
		for(FreeBoardDTO dto : list){
			out.println("<tr>");
			out.println("<td>");
			out.println(dto.getIdx());
			out.println("</td>");
			out.println("<td>");
			out.println(dto.getTitle());
			out.println("</td>");
			out.println("<td>");
			out.println(dto.getName());
			out.println("</td>");
			out.println("<td>");
			out.println(dto.getWdate());
			out.println("</td>");
			out.println("</tr>");
		}
	%>
	<%
		for(FreeBoardDTO dto : list){
	%>
		<tr>
			<td><%=dto.getIdx() %></td>
			<td><%=dto.getTitle() %></td>
			<td><%=dto.getName() %></td>
			<td><%=dto.getWdate() %></td>
		</tr>
	<%
		}
	%>
	
</table>


<c:set  var="a" value="jtsl변수입니다.."/>
${a}<br/>

<h1>lombok.jar</h1>
<p>
	1. lombok.jar 실행 이클립스에 설치<br/>
	2. 이클립스 재시작<br/>
	3. lombok.jar 를 해당 프로젝트에 추가<br/>
	4. 소스 컴파일
</p>
<h1>jar 파일 설명</h1>
<p>
	1. jstl은 c:foreach c:out c:set 사용 가능<br/>
	2. lombok getter setter 사용가능<br/>
	3. mysql-connector-j-8.033은 mysql 연결가능
</p>


</body>
</html>