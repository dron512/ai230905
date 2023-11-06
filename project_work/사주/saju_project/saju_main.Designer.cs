namespace saju_project2 {
    partial class saju_main {
        /// <summary>
        /// 필수 디자이너 변수입니다.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 사용 중인 모든 리소스를 정리합니다.
        /// </summary>
        /// <param name="disposing">관리되는 리소스를 삭제해야 하면 true이고, 그렇지 않으면 false입니다.</param>
        protected override void Dispose(bool disposing) {
        if (disposing && (components != null)) {
        components.Dispose();
        }
        base.Dispose(disposing);
        }

        #region Windows Form 디자이너에서 생성한 코드

        /// <summary>
        /// 디자이너 지원에 필요한 메서드입니다. 
        /// 이 메서드의 내용을 코드 편집기로 수정하지 마세요.
        /// </summary>
        private void InitializeComponent() {
            this.pan_bottom = new System.Windows.Forms.Panel();
            this.cbox_year = new System.Windows.Forms.ComboBox();
            this.cbox_month2 = new System.Windows.Forms.ComboBox();
            this.label_month2 = new System.Windows.Forms.Label();
            this.label_time = new System.Windows.Forms.Label();
            this.label_day = new System.Windows.Forms.Label();
            this.label_month = new System.Windows.Forms.Label();
            this.label_year = new System.Windows.Forms.Label();
            this.cbox_time = new System.Windows.Forms.ComboBox();
            this.cbox_day = new System.Windows.Forms.ComboBox();
            this.cbox_month = new System.Windows.Forms.ComboBox();
            this.tbox_name = new System.Windows.Forms.TextBox();
            this.cbox_gender = new System.Windows.Forms.ComboBox();
            this.btn_result = new System.Windows.Forms.Button();
            this.label_gender = new System.Windows.Forms.Label();
            this.label_birth = new System.Windows.Forms.Label();
            this.label_name = new System.Windows.Forms.Label();
            this.pan_midle = new System.Windows.Forms.Panel();
            this.label_text = new System.Windows.Forms.Label();
            this.pan_title = new System.Windows.Forms.Panel();
            this.pan_bottom.SuspendLayout();
            this.pan_midle.SuspendLayout();
            this.SuspendLayout();
            // 
            // pan_bottom
            // 
            this.pan_bottom.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(252)))), ((int)(((byte)(203)))), ((int)(((byte)(167)))));
            this.pan_bottom.Controls.Add(this.cbox_year);
            this.pan_bottom.Controls.Add(this.cbox_month2);
            this.pan_bottom.Controls.Add(this.label_month2);
            this.pan_bottom.Controls.Add(this.label_time);
            this.pan_bottom.Controls.Add(this.label_day);
            this.pan_bottom.Controls.Add(this.label_month);
            this.pan_bottom.Controls.Add(this.label_year);
            this.pan_bottom.Controls.Add(this.cbox_time);
            this.pan_bottom.Controls.Add(this.cbox_day);
            this.pan_bottom.Controls.Add(this.cbox_month);
            this.pan_bottom.Controls.Add(this.tbox_name);
            this.pan_bottom.Controls.Add(this.cbox_gender);
            this.pan_bottom.Controls.Add(this.btn_result);
            this.pan_bottom.Controls.Add(this.label_gender);
            this.pan_bottom.Controls.Add(this.label_birth);
            this.pan_bottom.Controls.Add(this.label_name);
            this.pan_bottom.Dock = System.Windows.Forms.DockStyle.Fill;
            this.pan_bottom.Location = new System.Drawing.Point(0, 273);
            this.pan_bottom.Name = "pan_bottom";
            this.pan_bottom.Size = new System.Drawing.Size(674, 329);
            this.pan_bottom.TabIndex = 7;
            // 
            // cbox_year
            // 
            this.cbox_year.FormattingEnabled = true;
            this.cbox_year.Items.AddRange(new object[] {
            "1920",
            "1921",
            "1922",
            "1923",
            "1924",
            "1925",
            "1926",
            "1927",
            "1928",
            "1929",
            "1930",
            "1931",
            "1932",
            "1933",
            "1934",
            "1935",
            "1936",
            "1937",
            "1938",
            "1939",
            "1940",
            "1941",
            "1942",
            "1943",
            "1944",
            "1945",
            "1946",
            "1947",
            "1948",
            "1949",
            "1950",
            "1951",
            "1952",
            "1953",
            "1954",
            "1955",
            "1956",
            "1957",
            "1958",
            "1959",
            "1960",
            "1961",
            "1962",
            "1963",
            "1964",
            "1965",
            "1966",
            "1967",
            "1968",
            "1969",
            "1970",
            "1971",
            "1972",
            "1973",
            "1974",
            "1975",
            "1976",
            "1977",
            "1978",
            "1979",
            "1980",
            "1981",
            "1982",
            "1983",
            "1984",
            "1985",
            "1986",
            "1987",
            "1988",
            "1989",
            "1990",
            "1991",
            "1992",
            "1993",
            "1994",
            "1995",
            "1996",
            "1997",
            "1998",
            "1999",
            "2000",
            "2001",
            "2002",
            "2003",
            "2004",
            "2005",
            "2006",
            "2007",
            "2008",
            "2009",
            "2010",
            "2011",
            "2012",
            "2013",
            "2014",
            "2015",
            "2016",
            "2017",
            "2018",
            "2019",
            "2020",
            "2021",
            "2022",
            "2023"});
            this.cbox_year.Location = new System.Drawing.Point(213, 119);
            this.cbox_year.Name = "cbox_year";
            this.cbox_year.Size = new System.Drawing.Size(86, 20);
            this.cbox_year.TabIndex = 16;
            this.cbox_year.Text = "1989";
            // 
            // cbox_month2
            // 
            this.cbox_month2.FormattingEnabled = true;
            this.cbox_month2.Items.AddRange(new object[] {
            "양력/평달",
            "음력/평달",
            "음력/윤달"});
            this.cbox_month2.Location = new System.Drawing.Point(545, 195);
            this.cbox_month2.Name = "cbox_month2";
            this.cbox_month2.Size = new System.Drawing.Size(86, 20);
            this.cbox_month2.TabIndex = 15;
            this.cbox_month2.Text = "양력/평달";
            // 
            // label_month2
            // 
            this.label_month2.AutoSize = true;
            this.label_month2.Font = new System.Drawing.Font("경기천년바탕 Bold", 24F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(129)));
            this.label_month2.Location = new System.Drawing.Point(271, 188);
            this.label_month2.Name = "label_month2";
            this.label_month2.Size = new System.Drawing.Size(260, 32);
            this.label_month2.TabIndex = 14;
            this.label_month2.Text = "양,음력(평달,윤달)";
            // 
            // label_time
            // 
            this.label_time.BackColor = System.Drawing.Color.Transparent;
            this.label_time.Location = new System.Drawing.Point(591, 120);
            this.label_time.Name = "label_time";
            this.label_time.Size = new System.Drawing.Size(53, 18);
            this.label_time.TabIndex = 13;
            this.label_time.Text = "시 출생";
            this.label_time.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label_day
            // 
            this.label_day.BackColor = System.Drawing.Color.Transparent;
            this.label_day.Location = new System.Drawing.Point(449, 120);
            this.label_day.Name = "label_day";
            this.label_day.Size = new System.Drawing.Size(22, 17);
            this.label_day.TabIndex = 12;
            this.label_day.Text = "일";
            this.label_day.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label_month
            // 
            this.label_month.BackColor = System.Drawing.Color.Transparent;
            this.label_month.Location = new System.Drawing.Point(375, 120);
            this.label_month.Name = "label_month";
            this.label_month.Size = new System.Drawing.Size(22, 17);
            this.label_month.TabIndex = 11;
            this.label_month.Text = "월";
            this.label_month.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label_year
            // 
            this.label_year.BackColor = System.Drawing.Color.Transparent;
            this.label_year.Location = new System.Drawing.Point(305, 121);
            this.label_year.Name = "label_year";
            this.label_year.Size = new System.Drawing.Size(22, 17);
            this.label_year.TabIndex = 10;
            this.label_year.Text = "년";
            this.label_year.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // cbox_time
            // 
            this.cbox_time.FormattingEnabled = true;
            this.cbox_time.Items.AddRange(new object[] {
            "생시모름",
            "23:30~01:30 [자시]",
            "01:30~03:30 [축시]",
            "03:30~05:30 [인시]",
            "05:30~07:30 [묘시]",
            "07:30~09:30 [진시]",
            "09:30~11:30 [사시]",
            "11:30~13:30 [오시]",
            "13:30~15:30 [미시]",
            "15:30~17:30 [신시]",
            "17:30~19:30 [유시]",
            "19:30~21:30 [술시]",
            "21:30~23:30 [해시]"});
            this.cbox_time.Location = new System.Drawing.Point(478, 118);
            this.cbox_time.Name = "cbox_time";
            this.cbox_time.Size = new System.Drawing.Size(112, 20);
            this.cbox_time.TabIndex = 9;
            this.cbox_time.Text = "생시모름";
            // 
            // cbox_day
            // 
            this.cbox_day.FormattingEnabled = true;
            this.cbox_day.Items.AddRange(new object[] {
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30",
            "31"});
            this.cbox_day.Location = new System.Drawing.Point(408, 118);
            this.cbox_day.Name = "cbox_day";
            this.cbox_day.Size = new System.Drawing.Size(38, 20);
            this.cbox_day.TabIndex = 8;
            this.cbox_day.Text = "1";
            // 
            // cbox_month
            // 
            this.cbox_month.FormattingEnabled = true;
            this.cbox_month.Items.AddRange(new object[] {
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12"});
            this.cbox_month.Location = new System.Drawing.Point(334, 118);
            this.cbox_month.Name = "cbox_month";
            this.cbox_month.Size = new System.Drawing.Size(38, 20);
            this.cbox_month.TabIndex = 7;
            this.cbox_month.Text = "1";
            // 
            // tbox_name
            // 
            this.tbox_name.Location = new System.Drawing.Point(114, 43);
            this.tbox_name.Name = "tbox_name";
            this.tbox_name.Size = new System.Drawing.Size(123, 21);
            this.tbox_name.TabIndex = 5;
            this.tbox_name.Text = "이창민";
            // 
            // cbox_gender
            // 
            this.cbox_gender.FormattingEnabled = true;
            this.cbox_gender.Items.AddRange(new object[] {
            "남자",
            "여자"});
            this.cbox_gender.Location = new System.Drawing.Point(119, 195);
            this.cbox_gender.Name = "cbox_gender";
            this.cbox_gender.Size = new System.Drawing.Size(88, 20);
            this.cbox_gender.TabIndex = 4;
            this.cbox_gender.Text = "남자";
            // 
            // btn_result
            // 
            this.btn_result.BackColor = System.Drawing.Color.Peru;
            this.btn_result.Font = new System.Drawing.Font("경기천년바탕 Bold", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(129)));
            this.btn_result.Location = new System.Drawing.Point(140, 256);
            this.btn_result.Name = "btn_result";
            this.btn_result.Size = new System.Drawing.Size(407, 54);
            this.btn_result.TabIndex = 3;
            this.btn_result.Text = "결과보기";
            this.btn_result.UseVisualStyleBackColor = false;
            this.btn_result.Click += new System.EventHandler(this.btn_result_Click_1);
            // 
            // label_gender
            // 
            this.label_gender.AutoSize = true;
            this.label_gender.Font = new System.Drawing.Font("경기천년바탕 Bold", 24F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(129)));
            this.label_gender.Location = new System.Drawing.Point(36, 188);
            this.label_gender.Name = "label_gender";
            this.label_gender.Size = new System.Drawing.Size(72, 32);
            this.label_gender.TabIndex = 2;
            this.label_gender.Text = "성별";
            // 
            // label_birth
            // 
            this.label_birth.AutoSize = true;
            this.label_birth.Font = new System.Drawing.Font("경기천년바탕 Bold", 24F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(129)));
            this.label_birth.Location = new System.Drawing.Point(36, 111);
            this.label_birth.Name = "label_birth";
            this.label_birth.Size = new System.Drawing.Size(171, 32);
            this.label_birth.TabIndex = 1;
            this.label_birth.Text = "생년월일 시";
            // 
            // label_name
            // 
            this.label_name.AutoSize = true;
            this.label_name.Font = new System.Drawing.Font("경기천년바탕 Bold", 24F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(129)));
            this.label_name.Location = new System.Drawing.Point(36, 37);
            this.label_name.Name = "label_name";
            this.label_name.Size = new System.Drawing.Size(72, 32);
            this.label_name.TabIndex = 0;
            this.label_name.Text = "성명";
            // 
            // pan_midle
            // 
            this.pan_midle.BackColor = System.Drawing.Color.DarkGoldenrod;
            this.pan_midle.Controls.Add(this.label_text);
            this.pan_midle.Dock = System.Windows.Forms.DockStyle.Top;
            this.pan_midle.Location = new System.Drawing.Point(0, 241);
            this.pan_midle.Name = "pan_midle";
            this.pan_midle.Size = new System.Drawing.Size(674, 32);
            this.pan_midle.TabIndex = 6;
            // 
            // label_text
            // 
            this.label_text.BackColor = System.Drawing.Color.SandyBrown;
            this.label_text.Dock = System.Windows.Forms.DockStyle.Fill;
            this.label_text.Font = new System.Drawing.Font("경기천년제목V Bold", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(129)));
            this.label_text.ForeColor = System.Drawing.Color.White;
            this.label_text.Location = new System.Drawing.Point(0, 0);
            this.label_text.Name = "label_text";
            this.label_text.Size = new System.Drawing.Size(674, 32);
            this.label_text.TabIndex = 2;
            this.label_text.Text = "생년월일시 정보를 입력하여 주십시요.";
            this.label_text.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // pan_title
            // 
            this.pan_title.BackgroundImage = global::saju_project2.Properties.Resources._1_1;
            this.pan_title.Dock = System.Windows.Forms.DockStyle.Top;
            this.pan_title.Location = new System.Drawing.Point(0, 0);
            this.pan_title.Name = "pan_title";
            this.pan_title.Size = new System.Drawing.Size(674, 241);
            this.pan_title.TabIndex = 0;
            // 
            // saju_main
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(674, 602);
            this.Controls.Add(this.pan_bottom);
            this.Controls.Add(this.pan_midle);
            this.Controls.Add(this.pan_title);
            this.MaximumSize = new System.Drawing.Size(690, 641);
            this.MinimumSize = new System.Drawing.Size(690, 641);
            this.Name = "saju_main";
            this.ShowInTaskbar = false;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "saju.com";
            this.pan_bottom.ResumeLayout(false);
            this.pan_bottom.PerformLayout();
            this.pan_midle.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel pan_title;
        private System.Windows.Forms.Panel pan_bottom;
        private System.Windows.Forms.ComboBox cbox_year;
        private System.Windows.Forms.ComboBox cbox_month2;
        private System.Windows.Forms.Label label_month2;
        private System.Windows.Forms.Label label_time;
        private System.Windows.Forms.Label label_day;
        private System.Windows.Forms.Label label_month;
        private System.Windows.Forms.Label label_year;
        private System.Windows.Forms.ComboBox cbox_time;
        private System.Windows.Forms.ComboBox cbox_day;
        private System.Windows.Forms.ComboBox cbox_month;
        private System.Windows.Forms.TextBox tbox_name;
        private System.Windows.Forms.ComboBox cbox_gender;
        private System.Windows.Forms.Button btn_result;
        private System.Windows.Forms.Label label_gender;
        private System.Windows.Forms.Label label_birth;
        private System.Windows.Forms.Label label_name;
        private System.Windows.Forms.Panel pan_midle;
        private System.Windows.Forms.Label label_text;
    }
}

