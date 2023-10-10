package conf;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import components.MemberDAO;

@Configuration
public class AppConf1 {
	
	@Bean
	public MemberDAO memberDAO() {
		return new MemberDAO();
	}
	
	
}
