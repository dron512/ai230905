package com.mh.ex04.board;

import jakarta.validation.Valid;
import org.apache.ibatis.annotations.Param;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;

import java.util.List;

@Controller
@RequestMapping("board")
public class BoardController {

    @Autowired
    BoardRepository boardRepository;

    @GetMapping("list")
    public String list(Model model, @RequestParam(required = false, defaultValue = "1") int pageNum) {
        // 현재 페이지 번호를 속성으로 등록
        model.addAttribute("pageNum", pageNum);

        pageNum = (pageNum - 1) * 5;
        List<Board> list = boardRepository.list(pageNum);
        int countRow = boardRepository.countRow();

        // db 테이블 list
        model.addAttribute("list", list);
        // 총 행 개수
        model.addAttribute("countRow", countRow);
        // 총 페이지 개수
        int countPage = (countRow / 5) + ((countRow % 5 > 0) ? 1 : 0);
        model.addAttribute("countPage", countPage);

        return "board/list";
    }

    @GetMapping("writeform")
    public String writeform(Model model, BoardReq boardReq) {
        model.addAttribute("first", "true");
        return "board/writeform";
    }

    @PostMapping("writeproc")
    public String writeproc(Model model,
                            @Valid BoardReq boardReq,
                            BindingResult result,
                            MultipartFile file) {
        String originalFilename = file.getOriginalFilename();
        System.out.println(originalFilename);
        // 유효성 검사
        if (result.hasErrors()) {
            return "board/writeform";
        }
        System.out.println(boardReq);
        /* 저장하는 부분 시작 */
        // boardReq 객체를 Board 객체로 변환
        Board board = Board.builder()
                .content(boardReq.getContent())
                .title(boardReq.getTitle())
                .name(boardReq.getName())
                .build();
        // db insert 하는 것
        boardRepository.insert(board);
        /* 저장하는 부분 끝 */
        return "redirect:/board/list";
    }

    @GetMapping("view")
    public String view(Model model,int idx){
        Board board = boardRepository.selectRow(idx);
        model.addAttribute("board",board);
        return "board/view";
    }
}
