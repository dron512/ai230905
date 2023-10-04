package fileboard;

import java.sql.Connection;				// 디비연결
import java.sql.PreparedStatement;		// SQL 만들기
import java.sql.ResultSet;				// select 내용반환
import java.time.LocalDateTime;			// 현재 시간...
import java.util.ArrayList;				// 리스트형태
import java.util.List;					// 리스트

import javax.sql.DataSource;

import db.DBDAO;

public class FileBoardDAO{
	private DataSource ds = DBDAO.getInstance().ds;
	private static FileBoardDAO dao = new FileBoardDAO();

	public static FileBoardDAO getInstance() {
		return dao;
	}
	
	public int selectRowCont() {
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement("SELECT count(*) as cnt FROM fileboard");
			rs = pstmt.executeQuery();
			if(rs.next()) {
				return rs.getInt("cnt");
			}
		}catch (Exception e) {
			e.printStackTrace();
			return 0;
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
		return 0;
	}
	
	public FileBoardDTO selectONE(int idx) {
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement("SELECT * FROM fileboard where idx = ?");
			pstmt.setInt(1, idx);
			rs = pstmt.executeQuery();
			if(rs.next()) {
				return FileBoardDTO.builder()
						.name(rs.getString("name"))
						.idx(rs.getInt("idx"))
						.title(rs.getString("title"))
						.content(rs.getString("content"))
						.filename1(rs.getString("filename1"))
						.filename2(rs.getString("filename2"))
						.filename3(rs.getString("filename3"))
						.rgwdate(rs.getObject("rgwdate", LocalDateTime.class))
						.build();
			}
		}catch (Exception e) {
			e.printStackTrace();
			return new FileBoardDTO();
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
		return new FileBoardDTO();
	}
	
	public List<FileBoardDTO> selectAll(int pageNum) {
		List<FileBoardDTO> list = new ArrayList<FileBoardDTO>();
		
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement("SELECT * FROM fileboard "
											+ "order by idx desc "
											+ "limit ?,5");
			// pageNum 1,2,3,4 번호에 따라서 0,5,10,15
			pageNum = (pageNum - 1) * 5;
			pstmt.setInt(1, pageNum);
			rs = pstmt.executeQuery();
			while(rs.next()) {
				list.add(FileBoardDTO.builder()
						.name(rs.getString("name"))
						.idx(rs.getInt("idx"))
						.title(rs.getString("title"))
						.content(rs.getString("content"))
						.filename1(rs.getString("filename1"))
						.filename2(rs.getString("filename2"))
						.filename3(rs.getString("filename3"))
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
					+ "	    filename1=?, "
					+ "	    filename2=?, "
					+ "	    filename3=? "
					+ "WHERE idx=?");
			pstmt.setString(1, dto.getName());
			pstmt.setString(2, dto.getTitle());
			pstmt.setString(3, dto.getContent());
			pstmt.setString(4, dto.getFilename1());
			pstmt.setString(5, dto.getFilename2());
			pstmt.setString(6, dto.getFilename3());
			pstmt.setInt(7, dto.getIdx());
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
					+ "(name, title, content, filename1, filename2, filename3, rgwdate) "
					+ "VALUES "
					+ "(?, ?, ?, ?, ?, ?, ?)");
			pstmt.setString(1, dto.getName());
			pstmt.setString(2, dto.getTitle());
			pstmt.setString(3, dto.getContent());
			pstmt.setString(4, dto.getFilename1());
			pstmt.setString(5, dto.getFilename2());
			pstmt.setString(6, dto.getFilename3());
			pstmt.setString(7, LocalDateTime.now().toString());
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
