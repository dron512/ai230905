<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>정보를 입력</title>
<style type="text/css">
	.a{
		width: 100px;
		height: 100px;
		background-color: red;
	}
</style>
</head>
<body>
<div class="a">

</div>
<h2>정보를 입력을 입력하세요 page 238</h2>
<form method="post" action="ex01pro.jsp">
	학번<input type="text" name="hak"/><br/>
	이름<input type="text" name="name"/><br/>
	전공: <select name="major">
			<option value="0" selected>선택하세요</option>
			<option value="컴퓨터공학">컴퓨터공학</option>
			<option value="전자공학">전자공학</option>
			<option value="기계공학">기계공학</option>
		</select>
		<input type="submit" value="전송완료"/>
</form>
</body>
</html>