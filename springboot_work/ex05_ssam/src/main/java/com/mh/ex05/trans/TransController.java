package com.mh.ex05.trans;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("trans")
public class TransController {

    @GetMapping("trans")
    public String trans(){
        return "trans/trans";
    }
}
