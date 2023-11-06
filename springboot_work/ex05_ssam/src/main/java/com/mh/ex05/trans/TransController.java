package com.mh.ex05.trans;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping("trans")
public class TransController {

    @Autowired
    TransService transService;

    @GetMapping("trans")
    public String trans(){
        return "trans/trans";
    }

    @PostMapping("req")
    @ResponseBody
    public String req(@RequestBody TranslationJson translationJson){
        System.out.println(translationJson);
        transService.main(translationJson.getText());
        return "asdfasdfasedrqwer";
    }
}
