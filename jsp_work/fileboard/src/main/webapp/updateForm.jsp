<%@ page language="java" contentType="text/html; charset=UTF-8"
   pageEncoding="UTF-8"%>
<%@ page import="fileboard.FileBoardDTO"%>
<%@ page import="fileboard.FileBoardDAO"%>
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
h1{
	text-align: center;
}
input[type='text'],textarea{
	padding :0.5rem;
}
input[type='submit']{
	font-size: 2rem;
	margin-top: 1rem;
}
#wrap{
	
}
</style>
</head>
<body>
<div id="wrap">
	<h1>UpdateForm</h1>
	<a href="select.jsp">목록</a>
	<form method="post" enctype="multipart/form-data" action="updatePro.jsp">
		<input type="hidden" name="idx" value="<%=dto.getIdx()%>">
		
		<input type="hidden" name="originalfile1" value="<%=dto.getFilename1()%>">
		<input type="hidden" name="originalfile2" value="<%=dto.getFilename2()%>">
		<input type="hidden" name="originalfile3" value="<%=dto.getFilename3()%>">
		
		<h2>제목</h2>
		<input type="text" name="title" value="<%=dto.getTitle()%>">
		<h2>내용</h2>
		<textarea rows="7" cols="60" name="content"><%=dto.getContent()%></textarea>
		<h2>작성자</h2>
		<input type="text" name="name" value="<%=dto.getName()%>"/>
		<h2>파일업로드</h2>
		<input type="file" name="filename1" /><br/>
		<input type="file" name="filename2" /><br/>
		<input type="file" name="filename3" /><br/>
		<input type="submit" value="글쓰기">
	</form>
</div>
</body>
</html>







