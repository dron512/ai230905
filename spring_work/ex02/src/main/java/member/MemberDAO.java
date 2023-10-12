package member;

import java.sql.Connection;
import java.sql.SQLException;

import javax.sql.DataSource;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;

public class MemberDAO {
	
	@Autowired
	private SqlSession sqlsession;
	
	public void test2() {
		System.out.println(sqlsession.selectList("member.selectAll"));
	}
}
