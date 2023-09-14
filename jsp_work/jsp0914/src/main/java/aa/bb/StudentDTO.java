package aa.bb;

public class StudentDTO {

	private String hak;
	private String name;
	private String major;
	private String age;
	private String gender;
	private String department;
	
	public String getAge() {
		return age;
	}

	public void setAge(String age) {
		this.age = age;
	}

	public String getGender() {
		return gender;
	}

	public void setGender(String gender) {
		this.gender = gender;
	}

	public String getDepartment() {
		return department;
	}

	public void setDepartment(String department) {
		this.department = department;
	}

	public StudentDTO() {}
	
	// 생성자 toString getter setter
	public StudentDTO(String hak, String name, String major) {
		this.hak = hak;
		this.name = name;
		this.major = major;
	}
	@Override
	public String toString() {
		return "StudentDTO [hak=" + hak + ", name=" + name + ", major=" + major + "]";
	}
	public String getHak() {
		return hak;
	}
	public void setHak(String hak) {
		this.hak = hak;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getMajor() {
		return major;
	}
	public void setMajor(String major) {
		this.major = major;
	}
	
	
}
