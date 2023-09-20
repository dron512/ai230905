package freeboard;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

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
		// serverl.xml 에 있는 context 태그 사이에 있는 resource 를 찾아서 DB 커넥션풀에 대한 내용을 가져와서 ds 변수에
		// 할당..
		try {
			Context initCtx = new InitialContext();
			Context envCtx = (Context) initCtx.lookup("java:comp/env");
			ds = (DataSource) envCtx.lookup("jdbc/basicjsp");
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public List<FreeBoardDTO> select() {
		List<FreeBoardDTO> list = new ArrayList<FreeBoardDTO>();

		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;

		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement("SELECT * FROM freeboard");
			rs = pstmt.executeQuery();
			while (rs.next()) {
				int idx = rs.getInt("idx");
				String title = rs.getString("title");
				String content = rs.getString("content");
				String name = rs.getString("name");
				LocalDate wdate = rs.getDate("wdate").toLocalDate();
				LocalDate udate = rs.getDate("udate").toLocalDate();
				list.add(new FreeBoardDTO(idx, title, content, name, wdate, udate));
			}
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			try {
				rs.close();
				pstmt.close();
				conn.close();
			} catch (Exception e) {
			}
		}

		return list;
	}

}
