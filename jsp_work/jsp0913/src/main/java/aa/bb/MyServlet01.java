package aa.bb;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/MyServlet01")
public class MyServlet01 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    public MyServlet01() {
        super();
    }

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
//		response.getWriter().append("Served at: ").append(request.getContextPath());
//		response.getWriter().append("asdfasdfasdfasdf");
		
		request.setAttribute("test", "test 속성값입니다.");
		request.getRequestDispatcher("a.jsp").forward(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
