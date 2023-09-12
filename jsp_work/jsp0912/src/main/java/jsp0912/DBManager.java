package jsp0912;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

public class DBManager {

	public static String aa = "test";

	public static String dbClass = "com.mysql.cj.jdbc.Driver";
	public static String dbUrl = "jdbc:mysql://192.168.0.135:3306/test";
	public static String dbId = "root";
	public static String dbPasswrod = "1234";

	public String bb = "bb";

	public DBManager() {
		System.out.println("생성자호출");
	}

	public boolean doInsert(String id, String password) throws Exception {
		// sql 실행하는거 만들어야함..
		Connection conn = null; // 연결하는 객체
		PreparedStatement pstmt = null; // sql 구문 담는 객체
		try {
			Class.forName(dbClass); // jar 파일이 추가 되어 있는지 확인
			// 연결..
			conn = DriverManager.getConnection(dbUrl, dbId, dbPasswrod);
			// sql 구문
			pstmt = conn.prepareStatement("insert into member (id,password) values (?,?)");
			pstmt.setString(1, id);
			pstmt.setString(2, password);
			pstmt.executeUpdate();
			System.out.println("insert 성공");
		} catch (Exception e) {
			e.printStackTrace();
			return false;
		} finally {
			pstmt.close();
			conn.close();
		}
		return true;
	}

	public List<Member> doSelect() throws Exception {
		List<Member> list = new ArrayList<Member>();
		
		// sql 실행하는거 만들어야함..
		Connection conn = null; // 연결하는 객체
		PreparedStatement pstmt = null; // sql 구문 담는 객체
		ResultSet rs = null;
		try {
			Class.forName(dbClass); // jar 파일이 추가 되어 있는지 확인
			// 연결..
			conn = DriverManager.getConnection(dbUrl, dbId, dbPasswrod);
			// sql 구문
			pstmt = conn.prepareStatement("select * from member");
			rs = pstmt.executeQuery();
			while (rs.next()) {
				System.out.println(rs.getInt("idx"));
				System.out.println(rs.getString("id"));
				System.out.println(rs.getString("password"));
				list.add(
						new Member(
								rs.getInt("idx"),
								rs.getString("id"), 
								rs.getString("password")
							)
						);
			}
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			pstmt.close();
			conn.close();
		}
		return list;
	}
}











