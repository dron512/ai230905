<%@page import="java.nio.file.Paths"%>
<%@page import="java.nio.file.Files"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
<%@ page import="fileboard.FileBoardDTO"%>
<%@ page import="fileboard.FileBoardDAO"%>
<%
	String idx = request.getParameter("idx");
	String webappFolder = "D:\\work\\jsp_work\\fileboard\\src\\main\\webapp\\images";

	FileBoardDAO dao = (FileBoardDAO)FileBoardDAO.getInstance();
	FileBoardDTO dto = dao.selectONE(Integer.parseInt(idx));
	
	try{
		Files.delete(Paths.get(webappFolder+"\\"+dto.getFilename1()));
	}catch(Exception e){
		e.printStackTrace();
	}
	
	try{
		Files.delete(Paths.get(webappFolder+"\\"+dto.getFilename2()));
	}catch(Exception e){
		e.printStackTrace();
	}
	
	try{
		Files.delete(Paths.get(webappFolder+"\\"+dto.getFilename3()));
	}catch(Exception e){
		e.printStackTrace();
	}
	
	dao.delete(dto.getIdx());
	
	response.sendRedirect("select.jsp");
%>




















