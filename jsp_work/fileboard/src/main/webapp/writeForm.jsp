<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
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
	<h1>WriteForm</h1>
	<a href="select.jsp">목록</a>
	<form method="post" enctype="multipart/form-data" action="writePro.jsp">
		<h2>제목</h2>
		<input type="text" name="title">
		<h2>내용</h2>
		<textarea rows="7" cols="60" name="content"></textarea>
		<h2>작성자</h2>
		<input type="text" name="name"/>
		<h2>파일업로드</h2>
		<input type="file" name="filename1"/><br/>
		<input type="file" name="filename2"/><br/>
		<input type="file" name="filename3"/><br/>
		<input type="submit" value="글쓰기">
	</form>
</div>
</body>
</html>







