<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<form method="post" action="ifMulPro.jsp">
		이름 : <input type="text" name="name"/><br/>
		지역 : <select name="local">
					<option value="서울">서울</option>
					<option value="대구">대구</option>		
			  </select>
		<br/>
		전화번호 : <input type="text" name="tel"/><br/>
		<input type="submit" value="전송"/>
	</form>
</body>
</html>