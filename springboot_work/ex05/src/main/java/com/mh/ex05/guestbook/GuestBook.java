package com.mh.ex05.guestbook;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;

@Entity
@AllArgsConstructor
@NoArgsConstructor
public class GuestBook {

    @Id
    private long idx;

    private String name;




}
