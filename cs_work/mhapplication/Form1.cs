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
    }
}