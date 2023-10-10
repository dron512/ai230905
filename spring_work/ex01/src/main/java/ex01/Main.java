package ex01;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.support.GenericXmlApplicationContext;

public class Main {

	
	public static void main(String[] args) {
		
//		AnnotationConfigApplicationContext ctx = new AnnotationConfigApplicationContext(MyConf.class);
		GenericXmlApplicationContext ctx = new GenericXmlApplicationContext("classpath:myconf.xml");
		
		AA a1 = ctx.getBean(AA.class);
		AA a2 = ctx.getBean(AA.class);
		
		System.out.println("a1 = "+a1);
		System.out.println("a2 = "+a2);
		
		AA a3 = new AA();
		AA a4 = new AA();
		
		System.out.println(a1==a2);
		System.out.println(a3==a4);
		
		ctx.close();
		
	}
	
}
