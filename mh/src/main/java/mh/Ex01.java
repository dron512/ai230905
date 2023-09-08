package mh;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

// ctrl+ shift + o import 자동으로...
class Member{
	private int idx;
	private String name;
	private int age;
	private String gender;
	// alt + shift + s -> o 생성자 자동 만들기...
	public Member(int idx, String name, int age, String gender) {
		this.idx = idx;
		this.name = name;
		this.age = age;
		this.gender = gender;
	}
	// alt + shift + s -> s -> toString 자동 만들기...
	@Override
	public String toString() {
		return "Member [idx=" + idx + ", name=" + name + ", age=" + age + ", gender=" + gender + "]";
	}
}

public class Ex01 {
	
	
	public static void main(String[] args) {
		List<Member> list = new ArrayList<Member>();
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		try {
			conn = DriverManager.getConnection("jdbc:mysql://192.168.0.135:3306/test", "root", "1234");
			pstmt = conn.prepareStatement("select * from member");
			rs = pstmt.executeQuery();
			while(rs.next()) {
				int idx = rs.getInt("idx");
				String name = rs.getString("name");
				int age = rs.getInt("age");
				String gender = rs.getString("gender");
				list.add(new Member(idx, name, age, gender));
			}
			System.out.println("연결됨");
		}catch (Exception e) {
			e.printStackTrace();
		}
		finally {
			try {
				rs.close();
				pstmt.close();
				conn.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		System.out.println(list);
		
	}
	

}
