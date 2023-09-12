package jsp0912;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

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
	
	public boolean doInsert(String id,String password) {
		// sql 실행하는거 만들어야함..
		Connection conn = null;				// 연결하는 객체
		PreparedStatement pstmt = null;		// sql 구문 담는 객체
		try {
			Class.forName("");				//jar 파일이 추가 되어 있는지 확인
			
			conn = DriverManager.getConnection(dbUrl,dbId,dbPasswrod);
			pstmt = conn.prepareStatement("insert into member (id,password) values (?,?)");
			pstmt.executeUpdate();
			
		}catch (Exception e) {
			e.printStackTrace();
		}
		finally {
			pstmt.close();
			conn.close();
		}
		return true;
	}
	
}
