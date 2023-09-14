package jsp0914;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

public class StudentDAO {
	
	public static String dbClass = "com.mysql.cj.jdbc.Driver";
	public static String dbUrl = "jdbc:mysql://localhost:3306/test";
	public static String dbId = "root";
	public static String dbPasswrod = "1234";
	
	public List<StudentDTO> select() throws Exception{
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		List<StudentDTO> list = new ArrayList<StudentDTO>();
		try {
			Class.forName(dbClass);
			conn = DriverManager.getConnection(dbUrl, dbId, dbPasswrod);
			pstmt = conn.prepareStatement("select * from student");
			rs = pstmt.executeQuery();
			while(rs.next()) {
				list.add(
						new StudentDTO(
						rs.getString("hak"),
						rs.getString("name"), 
						rs.getString("major"))
					);
			}
		}catch (Exception e) {
			e.printStackTrace();
		}finally {
			rs.close();
			pstmt.close();
			conn.close();
		}
		return list;
	}

	public void insert(StudentDTO dto) throws Exception{
		System.out.println(dto);
		Connection conn = null;
		PreparedStatement pstmt = null;
		try {
			Class.forName(dbClass);
			conn = DriverManager.getConnection(dbUrl, dbId, dbPasswrod);
			pstmt = conn.prepareStatement("insert into student (hak,name,major) values(?,?,?)");
			pstmt.setString(1, dto.getHak());
			pstmt.setString(2, dto.getName());
			pstmt.setString(3, dto.getMajor());
			pstmt.executeUpdate();
		}catch (Exception e) {
			e.printStackTrace();
		}finally {
			pstmt.close();
			conn.close();
		}
	}
	
}
