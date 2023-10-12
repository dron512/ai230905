package member;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;

public class MemberDAO {
	/*
	 * spring - mybatis
	 */
	@Autowired
	private SqlSession sqlsession;
	
	public void test2() {
		System.out.println(sqlsession.selectList("member.selectAll"));
	}

	
	public MemberDTO selectByEmail(String email) {
		MemberDTO dto = sqlsession.selectOne("member.selectByEmail",email);
		return dto;
	}


	public int insert(MemberDTO newMemberDTO) {
		sqlsession.insert("member.insert", newMemberDTO);
		return 1;
	}

	

}

