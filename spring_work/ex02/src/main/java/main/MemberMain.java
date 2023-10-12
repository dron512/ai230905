package main;

import org.springframework.context.support.GenericXmlApplicationContext;

import member.MemberDAO;
import member.MemberService;

public class MemberMain {
	
	public static void main(String[] args) {
		GenericXmlApplicationContext ctx = 
				new GenericXmlApplicationContext("classpath:appconf1.xml");
		
		MemberService ms = ctx.getBean(MemberService.class);

		ms.regist("a@naver.com","홍길동","1234","1234");
		ms.regist("b@naver.com","홍길동","1234","1234");
		
		
//		MemberDAO md = ctx.getBean(MemberDAO.class);
//		md.test();
//		md.test2();
		
		ctx.close();
	}
}
