package jsp0914;

public class StudentDTO {

	private String hak;
	private String name;
	private String major;
	
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
