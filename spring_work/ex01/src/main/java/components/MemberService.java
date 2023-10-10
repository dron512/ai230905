package components;

import lombok.AllArgsConstructor;

@AllArgsConstructor
public class MemberService {

	private MemberDAO memberDAO;

	public void regist() {
		System.out.println(memberDAO);
	}
}
