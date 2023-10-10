package conf;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import components.MemberDAO;
import components.MemberService;
import ex01.AA;

@Configuration
public class AppConf2 {
	
	@Autowired
	private MemberDAO memberDAO;
	
	@Bean
	public MemberService memberService() {
		return new MemberService(memberDAO);
	}
	
	@Bean
	public AA aa() {
		return new AA();
	}

}
