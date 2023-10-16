package conf;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

import spring.DD;

@Configuration
@ComponentScan(basePackages = {"spring","spring2"})
public class AppCtx2 {

	@Bean
	public DD dd() {
		return new DD();
	}
}
