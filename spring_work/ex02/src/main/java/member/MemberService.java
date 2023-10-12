package member;

import org.springframework.beans.factory.annotation.Autowired;

import lombok.Getter;

@Getter
public class MemberService {
	@Autowired
	private MemberDAO memberDAO;

	public void regist(String email, String name, String pw, String conpw) {

		MemberDTO memberDTO = memberDAO.selectByEmail(email);
		System.out.println("memberDTO = " + memberDTO);
		if (memberDTO != null) {
			System.out.println("email 중복입니다.");
			return;
		}

		MemberDTO newMemberDTO = MemberDTO.builder()
								.email(email)
								.name(name)
								.password(pw)
								.build();

		int suc = memberDAO.insert(newMemberDTO);
		if (suc == 1) {
			System.out.println("등록되었습니다.");
		}
		/*
		 * selectbyEmail 중복체크 insert 합니다.
		 */
	}

}
