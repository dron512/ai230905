package conf;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import spring.AA;
import spring.BB;

@Configuration
public class AppCtx {

	@Bean
	public AA aa() {
		return new AA();
	}
	
	@Bean
	@Qualifier("bb1")
	public BB bb1() {
		return new BB();
	}
	
	@Bean
	@Qualifier("bb2")
	public BB bb2() {
		return new BB();
	}
	
}
