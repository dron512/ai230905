package org;

public class AA {
	
	public static void main(String[] args) throws Exception {
		
		System.out.println("안녕하세요");
		
		Member member = Member.builder()
							.idx(0)
							.id("id")
							.password("mypassword")
							.build();
		System.out.println(member);
		
		DAO dao = new DAO();
		dao.check();
		
	}
}
