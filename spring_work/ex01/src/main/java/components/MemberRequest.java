package components;

import java.time.LocalDate;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Setter
@Getter
@ToString
@Builder
public class MemberRequest {
	private String email;
	private String pw;
	private String conpw;
	private String name;
	private LocalDate wdate;
	
	public boolean checkpw() {
		return pw.equals(conpw);
	}
}