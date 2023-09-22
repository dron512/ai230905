package fileboard;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.sql.DataSource;

public class FileBoardDAO {
	
	private DataSource ds = null;
	private static FileBoardDAO dao = new FileBoardDAO();
	
	public static FileBoardDAO getInstance() {
		return dao;
	}

	public FileBoardDAO() {
		try {
			Context initCtx = new InitialContext();
			Context envCtx = (Context) initCtx.lookup("java:comp/env");
			ds = (DataSource) envCtx.lookup("jdbc/basicjsp");
		}catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	public List<FileBoardDTO> selectAll() {
		List<FileBoardDTO> list = new ArrayList<FileBoardDTO>();
		
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement("SELECT * FROM fileboard");
			rs = pstmt.executeQuery();
			while(rs.next()) {
				list.add(FileBoardDTO.builder()
						.name(rs.getString("name"))
						.idx(rs.getInt("idx"))
						.title(rs.getString("title"))
						.content(rs.getString("content"))
						.filename(rs.getString("filename"))
						.rgwdate(rs.getObject("rgwdate",LocalDateTime.class))
						.build());
			}
		}catch (Exception e) {
			e.printStackTrace();
		}
		finally {
			try {
				rs.close();
				pstmt.close();
				conn.close();
			}catch (Exception e) {
				e.printStackTrace();
			}
		}
		return list;
	}
	
	public boolean update(FileBoardDTO dto) {
		Connection conn = null;
		PreparedStatement pstmt = null;
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement("UPDATE fileboard "
					+ " SET name=?, "
					+ " 	title=?, "
					+ "	    content=?,"
					+ "	    filename=? "
					+ "WHERE idx=?");
			pstmt.setString(1, dto.getName());
			pstmt.setString(2, dto.getTitle());
			pstmt.setString(3, dto.getContent());
			pstmt.setString(4, dto.getFilename());
			pstmt.setInt(5, dto.getIdx());
			pstmt.executeUpdate();
			return true;
		}catch (Exception e) {
			e.printStackTrace();
			return false;
		}
		finally {
			try {
				pstmt.close();
				conn.close();
			}catch (Exception e) {
				e.printStackTrace();
			}
		}
	}
	
	public boolean insert(FileBoardDTO dto) {
		Connection conn = null;
		PreparedStatement pstmt = null;
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement("INSERT INTO fileboard "
					+ "(name, title, content, filename, rgwdate) "
					+ "VALUES "
					+ "(?, ?, ?, ?, ?)");
			pstmt.setString(1, dto.getName());
			pstmt.setString(2, dto.getTitle());
			pstmt.setString(3, dto.getContent());
			pstmt.setString(4, dto.getFilename());
			pstmt.setString(5, LocalDateTime.now().toString());
			pstmt.executeUpdate();
			return true;
		}catch (Exception e) {
			e.printStackTrace();
			return false;
		}
		finally {
			try {
				pstmt.close();
				conn.close();
			}catch (Exception e) {
				e.printStackTrace();
			}
		}
	}
	
	public boolean delete(int idx) {
		Connection conn = null;
		PreparedStatement pstmt = null;
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement("DELETE FROM fileboard WHERE idx=?");
			pstmt.setInt(1, idx);
			pstmt.executeUpdate();
			return true;
		}catch (Exception e) {
			e.printStackTrace();
			return false;
		}
		finally {
			try {
				pstmt.close();
				conn.close();
			}catch (Exception e) {
				e.printStackTrace();
			}
		}
	}
}
