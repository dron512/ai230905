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
    public partial class MainForm : Form {
        private Label[,] m_labels = null;
        private int[,]  m_values = null;
        public MainForm() {
            InitializeComponent();
            CreateObject();
            //InitializeObject();
        }

        private void CreateObject() {
            m_labels = new Label[9, 9];
            m_values = new int[9, 9];
        }
        private void InitializeObject() { 
            foreach( Control _item in panel_game_board.Controls) {
                if(_item is Label) {
                    Label _label = _item as Label;
                    if( _label != null ) {
                        string _label_tag = _label.Tag.ToString();
                        Point _pt = GetPoint(_label_tag);
                        _label.Location = new Point(_pt.X*50, _pt.Y*50);
                        m_labels[_pt.X, _pt.Y] = _label;
                    }
                }
            }  
            
        }

        private Point GetPoint(string aTag) {
            Point _point = new Point(-1,-1);
            string[] words =aTag.Split(new char[] {','});
            if(words.Length == 2) {
                _point = new Point(int.Parse(words[0]), int.Parse(words[1]) );
            }
            return _point;
        }

        private void btn_init_Click(object sender, EventArgs e) {
            InitializeObject();
        }
    }
}
