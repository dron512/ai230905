package main;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.support.AbstractApplicationContext;

import components.MemberService;
import conf.AppConf1;
import conf.AppConf2;

public class MainSpring {

	private static AbstractApplicationContext ctx = null;
	
	public static void main(String[] args) throws IOException {
		
		ctx = new AnnotationConfigApplicationContext(AppConf1.class, AppConf2.class);
//		ctx = new AnnotationConfigApplicationContext(AppConf1.class);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		while (true) {
			help();
			String command = br.readLine();
			if(command.equals("exit")) {
				System.out.println("종료합니다.");
				break;
			}
			else if (command.startsWith("new ")) {
				processNewCommand(command.split(" "));
			}
		}
		ctx.close();
	}
	
	private static void processNewCommand(String[] args) {
		System.out.println("args[0]" + args[0]);
		System.out.println("args[1]" + args[1]);
		System.out.println("args[2]" + args[2]);
		System.out.println("이쪽으로 온다.");
		MemberService ms = ctx.getBean(MemberService.class);
		ms.regist();
	}
	
	private static void help() {
		System.out.println("입력하세요 ");
		System.out.println("1. new ");
		System.out.println("2. list ");
		System.out.println("3. exit ");
	}
}
