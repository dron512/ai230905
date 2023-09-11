package jsp0911;

public class Member {
	private String name;
	private String local;
	private String tel;
	
	// alt + shift + s -> s
	@Override
	public String toString() {
		return "Member [name=" + name + ", local=" + local + ", tel=" + tel + ", id=" + id + ", passwd=" + passwd
				+ ", age=" + age + "]";
	}

	public Member(String name, String local, String tel) {
		super();
		this.name = name;
		this.local = local;
		this.tel = tel;
	}

	public String id;
	public String passwd;
	public int age;
	
	public Member() {
		id="test";
		passwd="testpass";
		age=20;	
	}
	
	// alt + shift + s -> o 자동생성자 만들기
	public Member(String id, String passwd, int age) {
		this.id = id;
		this.passwd = passwd;
		this.age = age;
	}
	
	
}
