using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.TaskbarClock;
using System.Xml.Linq;
using saju_project2.temp;
using static saju_project2.temp.UserData;
using static System.Net.Mime.MediaTypeNames;
using System.Globalization;
using System.Security.Cryptography;
using System.Net.Http;
using Newtonsoft.Json;

namespace saju_project2 {
    public partial class saju_main : Form {
        public saju_main() {
        InitializeComponent();
        }

        private async void btn_result_Click_1(object sender, EventArgs e) {
            try
            {
                var result = ConnectServer();
                var sajudata = DailySaju.MakeNewSaju(await result);
                saju_result pop = new saju_result(sajudata);
                pop.ShowDialog(this);
            }catch (Exception ex)
            {
                MessageBox.Show("에러 다시해");
            }
        }

        private UserData GetUserData()
        {
            // 데이터 생성
            string name = tbox_name.Text;
            int year = Convert.ToInt32(cbox_year.Text);
            int month = Convert.ToInt32(cbox_month.Text);
            int day = Convert.ToInt32(cbox_day.Text);
            var time = GetBirthTime(cbox_time.SelectedIndex);
            bool isMale = cbox_gender.Text.Equals("남자") ? true : false;
            string calendar = cbox_month2.Text;
            var data = new UserData(name, year, month, day, time, isMale, calendar);
            return data;
        }

        public async Task<string> ConnectServer()
        {
            UserData data = GetUserData();

            using (HttpClient client = new HttpClient())
            {
                try
                {
                    var requestData = data.Serialize();

                    var content = new StringContent(requestData, Encoding.UTF8, "application/json");

                    HttpResponseMessage response = await client.PostAsync("http://127.0.0.1:5000", content);
                    response.EnsureSuccessStatusCode(); // 응답이 성공이면 진행

                    string responseText = await response.Content.ReadAsStringAsync();
                    string decodedResponse = JsonConvert.DeserializeObject<string>(responseText);

                    Console.WriteLine(decodedResponse);
                    return decodedResponse;
                }
                catch (HttpRequestException e)
                {
                    string responseBody = e.Message;
                    return responseBody;
                }
            }
        }
    }
}
