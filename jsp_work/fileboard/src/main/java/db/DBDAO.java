package db;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.sql.DataSource;

import fileboard.FileBoardDAO;

public class DBDAO {
	protected DataSource ds = null;
	private static DBDAO dao = new FileBoardDAO();
	
	public static DBDAO getInstance() {
		return dao;
	}

	public DBDAO() {
		try {
			Context initCtx = new InitialContext();
			Context envCtx = (Context) initCtx.lookup("java:comp/env");
			ds = (DataSource) envCtx.lookup("jdbc/basicjsp");
			System.out.println("ds 의 주소값 = "+ds);
		}catch (Exception e) {
			e.printStackTrace();
		}
	}
}
