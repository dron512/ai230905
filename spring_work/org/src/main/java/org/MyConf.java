package org;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration	// 환경 설정
public class MyConf {

	@Bean
	public DAO dao() {
		return new DAO();
	}
}
