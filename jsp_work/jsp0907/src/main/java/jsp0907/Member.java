package jsp0907;

public class Member {
	private int idx;
	private String name;
	private int age;
	private String gender;
	// alt + shift + s -> o 생성자 자동 만들기...
	public Member(int idx, String name, int age, String gender) {
		this.idx = idx;
		this.name = name;
		this.age = age;
		this.gender = gender;
	}
	// alt + shift + s -> s -> toString 자동 만들기...
	@Override
	public String toString() {
		return "Member [idx=" + idx + ", name=" + name + ", age=" + age + ", gender=" + gender + "]";
	}
}
