package com.mh.ex04.board;

import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface BoardRepository {

    public List<Board> list(int pageNum);
    public void insert(Board board);

    public int countRow();
    public Board selectRow(int idx);

}
