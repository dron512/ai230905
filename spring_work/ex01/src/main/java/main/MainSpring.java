package main;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.support.AbstractApplicationContext;

import components.MemberRequest;
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
			else if ( command.startsWith("list")) {
				processListCommand();
			}
		}
		ctx.close();
	}
	
	private static void processListCommand() {
		MemberService ms = ctx.getBean(MemberService.class);
		ms.list();
	}

	// new dron512@naver.com 홍길동 1234 1234 
	private static void processNewCommand(String[] args) {
		if( args.length != 5 ) {
			System.out.println("\nnew email 이름 비밀번호 확인 순서로 입력 하세요\n");
			return;
		}
		MemberRequest mr = MemberRequest.builder()
							.email(args[1])
							.name(args[2])
							.pw(args[3])
							.conpw(args[4])
							.build();
		
		if( !mr.checkpw() ) {
			System.out.println(""
					+ "입력하신 비번이 다릅니다.");
			return;
		}
		MemberService ms = ctx.getBean(MemberService.class);
		try {
			ms.regist(mr);
			System.out.println("등록되었습니다.");
		} catch (Exception e) {
			System.out.println("중복되는 이메일있습니다.");
		}
		
	}
	
	private static void help() {
		System.out.println("입력하세요 ");
		System.out.println("1. new ");
		System.out.println("2. list ");
		System.out.println("3. exit ");
	}
}
















