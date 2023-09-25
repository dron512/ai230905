<%@page import="java.util.Enumeration"%>
<%@page import="java.nio.file.Files"%>
<%@page import="java.nio.file.Path"%>
<%@page import="java.nio.file.Paths"%>
<%@page import="com.oreilly.servlet.multipart.DefaultFileRenamePolicy"%>
<%@page import="com.oreilly.servlet.MultipartRequest"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	String webappFolder = "D:\\work\\jsp_work\\fileboard\\src\\main\\webapp";

	String realFolder ="";
	String saveFolder = "/filesave"; // 파일 저장 위치
	String encType = "utf-8";		// 파일저장 인코딩 타임
	int filesize = 1024*1024*10;	//10MB 설정
	
	
	ServletContext context = getServletContext();
	realFolder = context.getRealPath(saveFolder);
	out.println(realFolder);
	try{
		Path realPath = Paths.get(realFolder);
		if( !Files.isDirectory(realPath)){
			Files.createDirectories(realPath);
		}
		
		// 파일이 자동 저장 됩니다.
		MultipartRequest mrequest1 = new MultipartRequest(request,realFolder,filesize,new DefaultFileRenamePolicy());
		
		String filename1 = mrequest1.getParameter("filename1");
		String filename2 = mrequest1.getParameter("filename2");
		String filename3 = mrequest1.getParameter("filename3");
		
		String name = mrequest1.getParameter("name");
		String title = mrequest1.getParameter("title");
		String content = mrequest1.getParameter("content");
		
		
		
		Enumeration<?> files = mrequest1.getFileNames();
		
		while(files.hasMoreElements()){
			String ename = (String)files.nextElement(); 
			String fileSystemname = mrequest1.getFilesystemName(ename);
			String originalFileName = mrequest1.getOriginalFileName(ename);
			
			out.println("<br/>");
			out.println("fileSystemname = "+fileSystemname+"<br/>");
			out.println("originalFileName = "+originalFileName+"<br/>");
		}
	}catch(Exception e){
		e.printStackTrace();
	}
	
	
	
%>











