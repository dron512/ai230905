
class CC{} 

class BB extends CC{
	
}

public class Test{
	
	
	public static void main(String[] args) {
	
		CC cc = new BB();
		System.out.println(cc);
//		BB bb = (BB) new CC();
		
	}
	

}


