package fileboard;

import java.time.LocalDateTime;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@ToString
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class FileBoardDTO {

	private int idx;
	private String name;
	private String title;
	private String content;
	private String filename;
	private LocalDateTime rgwdate;
	
}
