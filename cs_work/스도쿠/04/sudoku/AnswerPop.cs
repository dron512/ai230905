using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace sudoku {
    public partial class AnswerPop : Form {
        public int Answer {
            get { return Convert.ToInt32(tbox_answer.Text); }
        }
        public AnswerPop() {
            InitializeComponent();
            tbox_answer.SelectAll();
        }

        private void btn_answer_Click(object sender, EventArgs e) {
            DialogResult = DialogResult.OK;
        }

        private void AnswerPop_Load(object sender, EventArgs e) {

            tbox_answer.Select();
        }

        private void tbox_answer_KeyDown(object sender, KeyEventArgs e) {
            if (e.KeyCode == Keys.Enter) {
                DialogResult = DialogResult.OK;

            }
        }
    }
}
