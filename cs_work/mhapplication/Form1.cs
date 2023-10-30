using System.Text;
using System.Net.Http;
using System.Threading.Tasks;

namespace mhapplication {
    public partial class Form1 : Form {
        public Form1() {
            InitializeComponent();
            sidepanel.Height = button1.Height;
            firstCustomControl1.BringToFront();
        }

        private void button1_Click(object sender, EventArgs e) {
            sidepanel.Height = button1.Height;
            sidepanel.Top = button1.Top;
            firstCustomControl1.BringToFront();
        }

        private void button2_Click(object sender, EventArgs e) {
            sidepanel.Height = button2.Height;
            sidepanel.Top = button2.Top;
            secondCustomControl1.BringToFront();
        }

        private void button3_Click(object sender, EventArgs e) {
            sidepanel.Height = button3.Height;
            sidepanel.Top = button3.Top;
            thirdCustomControl1.BringToFront();
        }

        private void button11_Click(object sender, EventArgs e) {
            Application.Exit();
        }

        private void button9_Click(object sender, EventArgs e) {
            MessageBox.Show("누름");
            JsonConnect();
        }

        public async Task JsonConnect() {
            using (HttpClient client = new HttpClient()) {
                try {
                    var requestData = new { len = 30, wei = 600 }; // POST할 데이터

                    string json = Newtonsoft.Json.JsonConvert.SerializeObject(requestData); // 데이터를 JSON으로 변환

                    var content = new StringContent(json, Encoding.UTF8, "application/json");

                    HttpResponseMessage response = await client.PostAsync("http://127.0.0.1:5000", content);
                    response.EnsureSuccessStatusCode(); // 응답이 성공이면 진행

                    string responseBody = await response.Content.ReadAsStringAsync();
                    MessageBox.Show(responseBody);
                }
                catch (HttpRequestException e) {
                    MessageBox.Show($"HTTP 요청 오류: {e.Message}");
                }
            }
        }


    }
}