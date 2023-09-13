package jsp0912;

// DTO 
public class Product {
	
	private int idx;
	private String name;
	private int quan;
	
	/*
	 * alt + shift+ s + o 생성자 자동만들기
	 * alt + shift + s -> s ToString 자동
	 * alt + shift + s -> r getter setter
	 */
	
	public Product(int idx, String name, int quan) {
		super();
		this.idx = idx;
		this.name = name;
		this.quan = quan;
	}
	@Override
	public String toString() {
		return "Product [idx=" + idx + ", name=" + name + ", quan=" + quan + "]";
	}
	public int getIdx() {
		return idx;
	}
	public void setIdx(int idx) {
		this.idx = idx;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getQuan() {
		return quan;
	}
	public void setQuan(int quan) {
		this.quan = quan;
	}
	
}
