package member;

import java.sql.Connection;
import java.sql.SQLException;

import javax.sql.DataSource;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;

public class MemberDAO {
	@Autowired
	private DataSource dataSource;
	@Autowired
	private SqlSession sqlsession;
	
	public void test() {
		System.out.println("data = "+dataSource);
		Connection conn = null;
		try {
			conn = dataSource.getConnection();
			System.out.println("연결됨");
		}catch (Exception e) {
			e.printStackTrace();
		}finally {
			try {
				if(conn!=null)
					conn.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
	}
	
	public void test2() {
		System.out.println(sqlsession.selectList("member.selectAll"));
	}
}
