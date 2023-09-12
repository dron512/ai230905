package jsp0912;

public class Member {
	
	private int idx;
	private String id;
	private String password;
	
	// alt+ shift + s -> s toString 
	@Override
	public String toString() {
		return "Member [idx=" + idx + ", id=" + id + ", password=" + password + "]";
	}
	// alt + shift + s -> o 생성자 자동만들기
	public Member(int idx, String id, String password) {
		super();
		this.idx = idx;
		this.id = id;
		this.password = password;
	}
	// alt + shift + s -> r getter setter 자동 만들기
	public int getIdx() {
		return idx;
	}
	public void setIdx(int idx) {
		this.idx = idx;
	}
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}

}
