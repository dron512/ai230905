package jsp0912;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

public class DBProductManager {

	public static String aa = "test";

	public static String dbClass = "com.mysql.cj.jdbc.Driver";
	public static String dbUrl = "jdbc:mysql://192.168.0.135:3306/test";
	public static String dbId = "root";
	public static String dbPasswrod = "1234";

	public String bb = "bb";

	public DBProductManager() {
		System.out.println("생성자호출");
	}

	public boolean doInsert(String name, int quan) throws Exception {
		Connection conn = null;
		PreparedStatement pstmt = null;
		try {
			Class.forName(dbClass); 
			conn = DriverManager.getConnection(dbUrl, dbId, dbPasswrod);
			pstmt = conn.prepareStatement("insert into product (name,quan) values (?,?)");
			pstmt.setString(1, name);
			pstmt.setInt(2, quan);
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

	public List<Product> doSelect() throws Exception {
		List<Product> list = new ArrayList<Product>();
		Connection conn = null; 
		PreparedStatement pstmt = null; 
		ResultSet rs = null;
		try {
			Class.forName(dbClass); 
			conn = DriverManager.getConnection(dbUrl, dbId, dbPasswrod);
			pstmt = conn.prepareStatement("select * from product");
			rs = pstmt.executeQuery();
			while (rs.next()) {
				list.add(
						new Product(
								rs.getInt("idx"),
								rs.getString("name"), 
								rs.getInt("quan")
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











