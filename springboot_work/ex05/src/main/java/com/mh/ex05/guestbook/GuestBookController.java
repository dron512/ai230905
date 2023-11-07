package com.mh.ex05.guestbook;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
@RequestMapping("guestbook")
public class GuestBookController {

    @Autowired
    GuestBookRepository guestBookRepository;

    @GetMapping("test")
    @ResponseBody
    public String test(){
        guestBookRepository.save(new GuestBook(1l,"홍길동"));
        guestBookRepository.save(new GuestBook(2l,"이길동"));
        return "test";
    }

    @GetMapping("guestbook")
    public String guestbook(){
        return "guestbook/guestbook";
    }
}