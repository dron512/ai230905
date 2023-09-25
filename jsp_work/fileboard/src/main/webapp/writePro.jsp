<%@page import="fileboard.FileBoardDTO"%>
<%@page import="fileboard.FileBoardDAO"%>
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
	int filesize = 1024*1024*20;	//10MB 설정
	
	
	ServletContext context = getServletContext();
	realFolder = context.getRealPath(saveFolder);
	out.println(realFolder);
	try{
		Path realPath = Paths.get(realFolder);
		if( !Files.isDirectory(realPath)){
			Files.createDirectories(realPath);
		}
		
		request.setCharacterEncoding("utf-8");
		
		// 파일이 자동 저장 됩니다.
		MultipartRequest mrequest1 = new MultipartRequest(request,realFolder,filesize,new DefaultFileRenamePolicy());
		
		String filename[] = new String[3];
		
		String name = mrequest1.getParameter("name");
		String title = mrequest1.getParameter("title");
		String content = mrequest1.getParameter("content");
		
		Enumeration<?> files = mrequest1.getFileNames();
		int fileIndex = 0;
		while(files.hasMoreElements()){
			String ename = (String)files.nextElement(); 
			String fileSystemname = mrequest1.getFilesystemName(ename);
			String originalFileName = mrequest1.getOriginalFileName(ename);
			
			out.println("<br/>");
			out.println("fileSystemname = "+fileSystemname+"<br/>");
			out.println("originalFileName = "+originalFileName+"<br/>");
			filename[fileIndex] = fileSystemname;
			fileIndex++;
		}
		FileBoardDAO dao = FileBoardDAO.getInstance();
		dao.insert(
				FileBoardDTO.builder()
				.content(content)
				.title(title)
				.name(name)
				.filename1(filename[0])
				.filename2(filename[1])
				.filename3(filename[2])
				.build()
			);
		
	}catch(Exception e){
		e.printStackTrace();
	}
	
	
	
%>











