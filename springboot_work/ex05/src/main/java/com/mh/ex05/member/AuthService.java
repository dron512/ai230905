package com.mh.ex05.member;

import jakarta.transaction.Transactional;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

@Service
@Transactional
@RequiredArgsConstructor
public class AuthService implements UserDetailsService {

    @Autowired
    PasswordEncoder passwordEncoder;
    @Override
    public UserDetails loadUserByUsername(String email) throws UsernameNotFoundException {
        System.out.println(email);
//        Member member = memberRepository.findByEmail(email);
//        if (member==null){
//            throw new UsernameNotFoundException(email);
//        }
        return User.builder()
                .username("aa@naver.com")
                .password(passwordEncoder.encode("1234"))
                .roles("ADMIN")
                .build();
    }
}
