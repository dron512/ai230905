<%@page import="java.util.List"%>
<%@page import="java.time.LocalDateTime"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="fileboard.*" %>
<%
	FileBoardDAO dao = FileBoardDAO.getInstance();

// 	dao.update(
// 		FileBoardDTO.builder()
// 		.idx(4)
// 		.name("박길동수정")
// 		.filename("b수정.png")
// 		.title("게게게목")
// 		.content("내용")
// 		.build()
// 	);
// 	dao.delete(1);

	List<FileBoardDTO> list = dao.selectAll();
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style type="text/css">
	h1{
		color: blue;
	}
	.aa{
		border:1px solid black;
		background-color: red;
		padding: 10px;
		margin: 30px;
	}
	#mytable{
		border:5px solid black;
		width:100%;
	}
</style>
</head>
<body>
<h1>FileBoard 목록</h1>
<div class="aa">
	<table id="mytable">
		<tr>
			<th>idx</th>
			<th>이름</th>
			<th>제목</th>
			<th>작성일자</th>
			<th>첨부파일</th>
		</tr>
		<% for(FileBoardDTO dto : list ){ %>
		<tr>
			<td><%=dto.getIdx() %></td>
			<td><%=dto.getName() %></td>
			<td><a href="view.jsp?idx=<%=dto.getIdx()%>"><%=dto.getTitle() %></a></td>
			<td><%=dto.getRgwdate() %></td>
			<td><%=dto.getFilename() %></td>
		</tr>	
		<% } %>
	</table>
</div>
<h1>프로젝트 기본설정</h1>
1. jar추가<br/>
2. server.xml context 태그와 resource태그 추가<br/>
3. web.xml 추가<br/>
</body>
</html>