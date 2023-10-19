package com.mh.ex03.board;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.List;

@Controller
@RequestMapping("board")
public class BoardController {

    @Autowired
    BoardService boardService;
    @GetMapping("list")
    public String list(Model model){
        List<BoardDto> list = boardService.list();
        model.addAttribute("list",list);
        return "board/list";
    }
}
