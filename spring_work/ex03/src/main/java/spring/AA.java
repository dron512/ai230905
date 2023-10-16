package spring;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.lang.Nullable;
import org.springframework.stereotype.Component;

@Component
public class AA {
	
	@Autowired
//	@Qualifier("bb1")
	private BB bb;
	
	@Autowired
	@Qualifier("cc1")
	private CC cc;
	
	public void doPrint() {
		System.out.println(bb);
	}

}
