<%@page import="java.util.List"%>
<%@page import="java.time.LocalDateTime"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="fileboard.*" %>
<%

	int pageNum = 1;

	if( request.getParameter("pageNum") != null && 
			!request.getParameter("pageNum").equals("") ){
		pageNum = Integer.parseInt(request.getParameter("pageNum"));
	}
	FileBoardDAO dao = (FileBoardDAO)FileBoardDAO.getInstance();

	List<FileBoardDTO> list = dao.selectAll(pageNum);
	int rowCnt = dao.selectRowCont();
	int totalpage = rowCnt / 5 + ( rowCnt % 5>0 ? 1:0 ); 
	
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<%@ include file="head.jsp" %>
<style type="text/css">
	h1{
		color: blue;
	}
	a{
		color: #efefef;
		text-decoration: none;
	}
	tr> td > a:hover{
		background-color: #ccc;
	}
	.aa{
		color: #efefef;
		border:1px solid black;
		background-color: #333;
		padding: 10px;
		margin: 30px;
	}
	#mytable{
		border:5px solid black;
		width:100%;
	}
	.login{
		width:200px;
		height:100px;
		background-color: red;
		position: absolute;
		top:20px; right:20px;
	}
	.login input[type='text'], input[type='password']{
		width:120px;
	}
	h2{
		margin: 0;
	}
</style>
<script type="text/javascript">
	function memberForm(){
		location.href='member/memberForm.jsp';
	}
</script>
</head>
<body>
<h1>FileBoard 목록</h1>
<a style="color:black;" href="writeForm.jsp">글쓰기</a>
<div class="login">
	<h2>로그인</h2>
	<form action="member/loginPro.jsp">
		아이디 <input type="text" name="id"/><br/> 비밀번호 <input type="password" name="password"/>
		<div style="position: absolute; bottom: 0; right: 0;">
			<input type="submit" value="로그인" style="margin-right: 10px;"/>
			<input type="button" value="회원가입" onclick="memberForm();"/>
		</div>
	</form>
</div>
<div class="aa">
	<table id="mytable">
		<tr>
			<th width="50">idx</th>
			<th width="100">이름</th>
			<th>제목</th>
			<th width="200">작성일자</th>
		</tr>
		<% for(FileBoardDTO dto : list ){ %>
		<tr>
			<td><%=dto.getIdx() %></td>
			<td><%=dto.getName() %></td>
			<td><a href="view.jsp?idx=<%=dto.getIdx()%>"><%=dto.getTitle() %></a></td>
			<td><%=dto.getRgwdate() %></td>
		</tr>	
		<% } %>
	</table>
	<div>
		<h2>페이지</h2>
		<% for (int i=1; i<totalpage+1 ; i++){ %>
			<a href="?pageNum=<%=i%>"><%=i%></a> |
		<% } %>
	</div>
</div>
<h1>프로젝트 기본설정</h1>
1. jar추가<br/>
2. server.xml context 태그와 resource태그 추가<br/>
3. web.xml 추가<br/>
</body>
</html>
















