package com.mh.ex05.member;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("auth")
public class AuthController {

    @GetMapping("login")
    public String login(){
        return "auth/login";
    }

    @GetMapping("register")
    public String register(){
        return "auth/register";
    }

    @GetMapping("password")
    public String password(){
        return "auth/password";
    }

}
