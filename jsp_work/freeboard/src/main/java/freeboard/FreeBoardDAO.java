package freeboard;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.sql.DataSource;

public class FreeBoardDAO {

	private DataSource ds = null;
	
	private static FreeBoardDAO dao = new FreeBoardDAO();
	
	public static FreeBoardDAO getInstance() {
		return dao;
	}

	public FreeBoardDAO() {
		// serverl.xml 에 있는 context 태그 사이에 있는 resource 를 찾아서 DB 커넥션풀에 대한 내용을 가져와서 ds 변수에 할당..
		try {
			Context initCtx = new InitialContext();
			Context envCtx = (Context) initCtx.lookup("java:comp/env");
			ds = (DataSource) envCtx.lookup("jdbc/basicjsp");
		}catch (Exception e) {
			e.printStackTrace();
		}
		
	}
	
}
