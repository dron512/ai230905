package member;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import javax.sql.DataSource;

import db.DBDAO;

public class MemberDAO{
	private DataSource ds = DBDAO.getInstance().ds;

	private static MemberDAO dao = new MemberDAO();

	public static MemberDAO getInstance() {
		return dao;
	}

	// 0 로그인 성공 1 로그인 실패 
	public int getCheck(String id,String password) {
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement("SELECT * from member where id=? and password=?");
			pstmt.setString(1, id);
			pstmt.setString(2, password);
			rs = pstmt.executeQuery();
			if(rs.next()) {
				return 0;
			}
		}catch (Exception e) {
			e.printStackTrace();
			return 1;
		}
		finally {
			try {
				rs.close();
				pstmt.close();
				conn.close();
			}catch (Exception e) {
				e.printStackTrace();
			}
		}
		return 1;
	}
}





