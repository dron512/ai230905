package components;

import java.util.HashMap;
import java.util.Map;

public class MemberDAO {
	
	private Map<String,MemberDTO> map = new HashMap<String, MemberDTO>();

	public MemberDTO selectByEmail(String email) {
		return map.get(email);
	}
	
	public void insert(MemberDTO md) {
		map.put(md.getEmail(), md);
	}

	public void selectAll() {
		map.values().forEach( ele -> System.out.println(ele) );
	}
}






