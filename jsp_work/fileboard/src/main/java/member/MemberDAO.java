package member;

import javax.sql.DataSource;

import db.DBDAO;

public class MemberDAO{
	private DataSource ds = DBDAO.getInstance().ds;

	private static MemberDAO dao = new MemberDAO();

	public static MemberDAO getInstance() {
		return dao;
	}

	// 0 로그인 성공 1 비번 체크 2 아이디 체크
	public int getCheck(String id,String password) {
		
		
		return 0;
	}
}
