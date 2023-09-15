package jsp0915;

public class ExBean {
	
	private String id;
	private String password;
	private int number;
	
	// 1. 기본생성자 2. 속성을 지정할수 있는 생성자 3. getter setter 4. toString
	
	public ExBean() {}
	
	public ExBean(String id, String password, int number) {
		super();
		this.id = id;
		this.password = password;
		this.number = number;
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
	public int getNumber() {
		return number;
	}
	public void setNumber(int number) {
		this.number = number;
	}
	@Override
	public String toString() {
		return "ExBean [id=" + id + ", password=" + password + ", number=" + number + "]";
	}
	

}
