package main;

import org.springframework.context.support.GenericXmlApplicationContext;

import member.MemberDAO;
import member.MemberService;

public class MemberMain {
	
	public static void main(String[] args) {
		GenericXmlApplicationContext ctx = 
				new GenericXmlApplicationContext("classpath:appconf1.xml");
		
		MemberService ms = ctx.getBean(MemberService.class);
		MemberDAO md = ctx.getBean(MemberDAO.class);
//		md.test();
		md.test2();
		
		ctx.close();
	}
}
