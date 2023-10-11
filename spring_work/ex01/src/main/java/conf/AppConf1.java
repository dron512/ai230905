package conf;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Import;

import components.MemberDAO;

@Configuration
//@Import(AppConf2.class)
public class AppConf1 {
	@Bean
	public MemberDAO memberDAO() {
		return new MemberDAO();
	}
}
