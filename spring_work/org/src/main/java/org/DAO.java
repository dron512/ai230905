package org;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class DAO {
	public static String dbClass = "com.mysql.cj.jdbc.Driver";
	public static String dbUrl = "jdbc:mysql://localhost:3306/test";
	public static String dbId = "root";
	public static String dbPasswrod = "1234";
	
	public void check()  throws Exception{
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		try {
			Class.forName(dbClass);
			conn = DriverManager.getConnection(dbUrl, dbId, dbPasswrod);
			pstmt = conn.prepareStatement("select * from student");
			rs = pstmt.executeQuery();
			while(rs.next()) {
				System.out.println("rs.getString()"+rs.getString("name"));
			}
		}catch (Exception e) {
			e.printStackTrace();
		}finally {
			rs.close();
			pstmt.close();
			conn.close();
		}
	}
}
