package com.mh.ex02.board;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class BoardService {

    @Autowired
    BoardDao boardDao;

    public List<BoardDto> getAll(){
        return boardDao.getAll();
    }
}
