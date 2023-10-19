package com.mh.ex03.board;

import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;
import lombok.Data;

@Data
public class BoardReq {
    @NotNull
    private String name;

    @Size(min=10)
    private String content;

    @Size(min=2)
    private String title;
}
