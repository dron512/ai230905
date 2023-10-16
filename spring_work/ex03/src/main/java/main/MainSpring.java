package main;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import conf.AppCtx;
import spring.AA;

public class MainSpring {

	public static void main(String[] args) {
		
		
		AnnotationConfigApplicationContext ctx = 
				new AnnotationConfigApplicationContext(AppCtx.class);
		
		AA aa = ctx.getBean(AA.class);
		aa.doPrint();
		
		ctx.close();
	}
	
}
