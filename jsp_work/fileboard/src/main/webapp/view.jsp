<%@page import="fileboard.FileBoardDTO"%>
<%@page import="fileboard.FileBoardDAO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	String idx = request.getParameter("idx");

	FileBoardDAO dao = FileBoardDAO.getInstance();
	FileBoardDTO dto = dao.selectONE(Integer.parseInt(idx));
	
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<%@ include file="head.jsp" %>
<style type="text/css">
	#content{
		text-align: center;
	}
	#content > div{
		border : 1px solid black;
	}
	#content_sub{
		margin:1rem;
		padding : 1rem;
		border : 1px solid black;
		text-align:left;
		min-height: 300px;
	}
</style>
</head>
<body>
<div id="content">
	<h1>View</h1>
	<a href="select.jsp">목록</a>
	<a href="updateForm.jsp">수정</a>
	<a href="delete.jsp">삭제</a>
	<div>
		<h2>제목 <%=dto.getTitle() %></h2>
		<h4>작성일자 <%=dto.getRgwdate() %></h4>
		<div id="content_sub"><%=dto.getContent() %></div>
		<h2>
			작성자 <%=dto.getName() %>
			업로드된 파일 <a href="<%=dto.getFilename()%>"><%=dto.getFilename() %></a>
		</h2>
	</div>
</div>

</body>
</html>




















