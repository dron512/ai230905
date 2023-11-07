package com.mh.ex05.sec;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception{

        http.authorizeRequests(
                          req ->
                             req.requestMatchers("/css/**", "/js/**", "/img/**","/assets/**").permitAll()
                                .anyRequest().authenticated()
                     )
                .formLogin( formlogion ->
                            formlogion
                                .loginPage("/auth/login")
                                    .defaultSuccessUrl("/")
                                .usernameParameter("email")
                                    .failureUrl("/auth/login/error")
                                .permitAll() );

        return http.build();
    }
}
