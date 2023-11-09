package com.mh.ex05.guestbook;

import com.mh.ex05.member.Member;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
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
