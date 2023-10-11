package components;

import lombok.NoArgsConstructor;
import lombok.Setter;


@NoArgsConstructor
@Setter
public class MemberService {
	private MemberDAO memberDAO;
	public void regist(MemberRequest mr) throws Exception {
		MemberDTO dto = memberDAO.selectByEmail(mr.getEmail());
		if(dto !=null) {
			throw new Exception("중복되는 이메일 있습니다.");
		}
		MemberDTO newDTO = MemberDTO.builder()
						.email(mr.getEmail())
						.name(mr.getName())
						.pw(mr.getPw())
						.conpw(mr.getConpw())
						.build();
		memberDAO.insert(newDTO);
	}
	public void list() {
		memberDAO.selectAll();
	}
}
