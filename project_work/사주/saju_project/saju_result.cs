using saju_project2.temp;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Reflection.Emit;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace saju_project2 {
    public partial class saju_result : Form {
        DailySaju data;
        public saju_result(DailySaju sajudata) {
            InitializeComponent();
            this.data = sajudata;
            loadpop();
        }
        private void loadpop()
        {
            label_number.Text = data.Num.ToString();
            label_direction.Text = data.Direction;
            label_animal.Text = data.Animal;
            label_body.Text = data.BodyParts;
            label_color.Text = data.Color;
            label_fruit.Text = data.Fruit;
            label_Guide.Text = data.Guide;
            label_mind.Text = data.Mind;
            label_taste.Text = data.Flavor;
            textBox1.Text = $"총운:{data.NaverSummary}\n{ data.NaverDetail}";
        }

        private void btn_result_Click(object sender, EventArgs e) {
            Close();
        }
    }
}
