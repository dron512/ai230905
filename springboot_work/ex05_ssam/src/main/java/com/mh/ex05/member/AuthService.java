package com.mh.ex05.member;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

@Service
public class AuthService implements UserDetailsService {

    @Autowired
    PasswordEncoder passwordEncoder;

    @Autowired
    MemberRepository memberRepository;

    @Override
    public UserDetails loadUserByUsername(String email) throws UsernameNotFoundException {
        System.out.println("일로온다");
        System.out.println(email);

        // member table 에 email있는지 확인

        Member dbMember = memberRepository.findByEmail(email);

        if(dbMember == null)
            throw new UsernameNotFoundException(email);

        return User.builder()
                .username(dbMember.getEmail())
                .password(dbMember.getPassword())
                .roles("ADMIN")
                .build();

    }
}
