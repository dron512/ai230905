<%@page import="java.nio.file.StandardCopyOption"%>
<%@page import="java.nio.file.CopyOption"%>
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
	// 한글 나오게...
	request.setCharacterEncoding("utf-8");
	String webappFolder = "D:\\work\\jsp_work\\fileboard\\src\\main\\webapp\\images";

	String realFolder ="";
	String saveFolder = "/filesave"; // 파일 저장 위치
	String encType = "utf-8";		// 파일저장 인코딩 타임
	int filesize = 1024*1024*20;	// 20MB 설정
	
	
	ServletContext context = getServletContext();
	realFolder = context.getRealPath(saveFolder);

	try{
		// realPath 톰캣이 자동으로 만드는 서버 폴더
		Path realPath = Paths.get(realFolder);
		if( !Files.isDirectory(realPath)){
			Files.createDirectories(realPath);
		}
		out.print("realPath"+realPath+"<br/>");
		// webapp 폴더에 images 폴더 만들기		
		Path webPath = Paths.get(webappFolder);
		if( !Files.isDirectory(webPath)){
			Files.createDirectories(webPath);
		}
		out.print("webPath"+webPath);
		
		// 파일이 자동 저장 됩니다.
		MultipartRequest mrequest1 = new MultipartRequest(
				request ,realFolder, filesize, encType, new DefaultFileRenamePolicy());
		
		// 파일 3개...
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
			
			// multipartRequest 객체를 이용해서 디스크에 저장된 이름을 filename 배열에 저장
			filename[fileIndex] = fileSystemname;
			fileIndex++;
			
			// insert 기능에서 파일 저장하고 ... 복사하는것만 추가 된건거
			if(fileSystemname!=null){
				Path source = Paths.get(realFolder+"\\"+fileSystemname);
				Path target = Paths.get(webappFolder+"\\"+fileSystemname);
				Files.copy(source, target, StandardCopyOption.REPLACE_EXISTING);
			}
			
		}
		
		FileBoardDAO dao = (FileBoardDAO)FileBoardDAO.getInstance();
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
		
		response.sendRedirect("select.jsp");
		
	}catch(Exception e){
		e.printStackTrace();
	}
	
	
	
%>











