<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script type="text/javascript">
	localStorage.setItem('id', '마이 아이디 입니다.');
	function test(){
		localStorage.removeItem('id');
	}
</script>
</head>
<body>
<button onclick="test()">삭제</button>
</body>
</html>