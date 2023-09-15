package jsp09151;

import java.sql.Connection;
import java.sql.PreparedStatement;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.sql.DataSource;

public class MemberDAO {

	private DataSource ds = null;
	
	// 생성자 호출할때 ds 객체 담아오기
	public MemberDAO() {
		try {
			Context initCtx = new InitialContext();
			Context envCtx = (Context) initCtx.lookup("java:comp/env");
			ds = (DataSource) envCtx.lookup("jdbc/basicjsp");
		}catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	public boolean delete(int idx) {
		Connection conn = null;
		PreparedStatement pstmt = null;
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement("DELETE FROM member WHERE idx=?");
			pstmt.setInt(1, idx);
			pstmt.executeUpdate();
			return true;
		}catch (Exception e) {
			e.printStackTrace();
			return false;
		}
		finally {
			try {
				pstmt.close();
				conn.close();
			}catch (Exception e) {
				e.printStackTrace();
			}
		}
	}
	
	public boolean update(MemberDTO dto) {
		Connection conn = null;
		PreparedStatement pstmt = null;
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement("UPDATE member "
										+ "	SET id=?, "
										+ "	PASSWORD=?, "
										+ "	NAME=?, "
										+ "	age=?, "
										+ "	gender=? "
										+ " WHERE idx=?");
			pstmt.setString(1, dto.getId());
			pstmt.setString(2, dto.getPassword());
			pstmt.setString(3, dto.getName());
			pstmt.setInt(4, dto.getAge());
			pstmt.setString(5, dto.getGender());
			pstmt.setInt(6, dto.getIdx());
			pstmt.executeUpdate();
			return true;
		}catch (Exception e) {
			e.printStackTrace();
			return false;
		}
		finally {
			try {
				pstmt.close();
				conn.close();
			}catch (Exception e) {
				e.printStackTrace();
			}
		}
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
}
