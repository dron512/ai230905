package components;

import lombok.NoArgsConstructor;
import lombok.Setter;


@NoArgsConstructor
@Setter
public class MemberService {

	private MemberDAO memberDAO;

	public void regist() {
		System.out.println(memberDAO);
	}
}
