<%@page import="java.time.LocalDateTime"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="fileboard.*" %>
<%
	FileBoardDAO dao = FileBoardDAO.getInstance();


// 	dao.update(new FileBoardDTO(3,"홍길동수정","글제목","글내용","a.png",null));
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

	out.println(dao.selectAll());
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>프로젝트 기본설정</h1>
1. jar추가<br/>
2. server.xml context 태그와 resource태그 추가<br/>
3. web.xml 추가<br/>
</body>
</html>