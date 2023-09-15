package jsp09151;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@ToString
@AllArgsConstructor
@NoArgsConstructor
public class MemberDTO {

	private int idx;
	private String id;
	private String password;
	private String name;
	private int age;
	private String gender;
	
	// 기본 생성자, 설정하는 생성자, toString, getter,setter
	
	
}
