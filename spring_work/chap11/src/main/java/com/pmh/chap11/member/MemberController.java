package com.pmh.chap11.member;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class MemberController {
	
	@Autowired
	SqlSession sqlSession;

	
	@GetMapping("member")
	public String member() {
		sqlSession.insert("member.insert");
		return "member";
	}
}
