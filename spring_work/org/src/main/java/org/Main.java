package org;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class Main {

	
	public static void main(String[] args) {
		
		// 객체컨테이너를 만들때 어노테이션 문법을... 스프링 4버전..
		// 객체컨테이너를 만들때 xml 파일로 생성했습니다... 스프링 2.5버전...
		AnnotationConfigApplicationContext ctx = new AnnotationConfigApplicationContext(MyConf.class);
		
		DAO dao1 = ctx.getBean(DAO.class);
		DAO dao2 = ctx.getBean(DAO.class);
		
		DAO dao3 = new DAO();
		
		System.out.println(dao1.dbPasswrod);
		System.out.println(dao2.dbPasswrod);
		
		dao1.dbPasswrod = "5567";
		
		System.out.println(dao1);
		System.out.println(dao2);
		
		System.out.println(dao1.dbPasswrod);
		System.out.println(dao2.dbPasswrod);
		
		ctx.close();
		
	}
}
