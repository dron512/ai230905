package member;

import org.springframework.beans.factory.annotation.Autowired;

import lombok.Getter;

@Getter
public class MemberService {
	@Autowired
	private MemberDAO memberDAO;
	
}
