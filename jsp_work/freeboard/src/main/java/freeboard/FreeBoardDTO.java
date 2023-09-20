package freeboard;

import java.time.LocalDate;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

@Builder // 빌더 사용해서 객체 만들기 -- 새로나온 내용
@Getter // 값 가져오기
@Setter // 값 설정
@ToString	// ToString 주소값 출력하지 말고 객체안에 담겨있는값 출력
@AllArgsConstructor // 모든 컬럼 설정해서 만드는 생성자
@NoArgsConstructor //기본생성자
public class FreeBoardDTO {
	
	// 기본키 primary key
	private int idx;
	// 글제목
	private String title;
	private String content;
	
	// 작성한 사람 이름
	private String name;
	
	// 최초 작성시간
	private LocalDate wdate;
	// 마지막으로 작성시간
	private LocalDate udate;
	
	
	
	

}
