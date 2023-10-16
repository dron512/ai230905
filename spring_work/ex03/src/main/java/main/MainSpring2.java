package main;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import conf.AppCtx2;
import spring.AA;
import spring.BB;
import spring.CC;

public class MainSpring2 {
	
	public static void main(String[] args) {
		AnnotationConfigApplicationContext acac = 
				new AnnotationConfigApplicationContext(AppCtx2.class);
		
		BB bb = acac.getBean(BB.class);
		System.out.println(bb);
		
		CC cc = acac.getBean(CC.class);
		System.out.println(cc);
		
		AA aa = acac.getBean(AA.class);
		System.out.println(aa);
		
		acac.close();
	}

}
