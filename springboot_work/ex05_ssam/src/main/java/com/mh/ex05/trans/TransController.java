package com.mh.ex05.trans;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping("trans")
public class TransController {

    @Autowired
    TransService transService;

    @Autowired
    TransRepository transRepository;

    @GetMapping("trans")
    public String trans(){
        return "trans/trans";
    }

    @PostMapping("req")
    @ResponseBody
    public String req(@RequestBody TranslationJson translationJson){
        System.out.println("일로온다....");
        System.out.println(translationJson);

        String target = transService.main(translationJson.getText());

        transRepository.save(Trans.builder()
                        .source(translationJson.getText())
                        .target(target)
                        .build());

        return target;
    }
}
