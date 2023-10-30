package com.mh.ex04.board;

import jakarta.validation.constraints.NotEmpty;
import lombok.Builder;
import lombok.Data;

@Data
@Builder
public class BoardReq {

    private int idx;

    @NotEmpty
    private String title;

    @NotEmpty
    private String content;

    @NotEmpty
    private String name;

    private String originalfilename;
}
