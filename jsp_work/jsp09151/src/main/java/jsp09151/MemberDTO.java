package jsp09151;

public class MemberDTO {

	private int idx;
	private String id;
	private String password;
	private String name;
	private int age;
	private String gender;
	
	// 기본 생성자, 설정하는 생성자, toString, getter,setter
	public MemberDTO() {}
	
	@Override
	public String toString() {
		return "MemberDTO [idx=" + idx + ", id=" + id + ", password=" + password + ", name=" + name + ", age=" + age
				+ ", gender=" + gender + "]";
	}
	public MemberDTO(int idx, String id, String password, String name, int age, String gender) {
		super();
		this.idx = idx;
		this.id = id;
		this.password = password;
		this.name = name;
		this.age = age;
		this.gender = gender;
	}
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
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public String getGender() {
		return gender;
	}
	public void setGender(String gender) {
		this.gender = gender;
	}
	
	
}
