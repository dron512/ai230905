using System;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.Rebar;

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
            cbox_level.SelectedIndex = 0;
        }
        private void InitializeObject() { 
            foreach( Control _item in panel_game_board.Controls) {
                if(_item is Label) {
                    Label _label = _item as Label;
                    if( _label != null ) {
                        string _label_tag = _label.Tag.ToString();
                        Point _pt = GetPoint(_label_tag);
                        _label.Location = new Point(_pt.Y*50,_pt.X*50);
                        m_labels[_pt.X, _pt.Y] = _label;
                        m_labels[_pt.X, _pt.Y].Tag = null;
                        m_labels[_pt.X, _pt.Y].Text = "";// string.Format("{0},{1}",_pt.Y,_pt.X);
                        m_labels[_pt.X, _pt.Y].Click += new System.EventHandler(this.btn_answer_Click);
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
        private void btn_answer_Click(object sender, EventArgs e) {
            Label _label = sender as Label;
            if (_label != null && _label.Text == "") {
                    AnswerPop _pop = new AnswerPop();
                if(_pop.ShowDialog() == DialogResult.OK) {
                    if (_pop.Answer == Convert.ToInt32(_label.Tag)) {
                        _label.Text = _label.Tag.ToString();
                    } else {
                        MessageBox.Show("틀렸습니다.");
                    }
                }

            }
        }


        private void btn_random_Click(object sender, EventArgs e) {
            //난수만들기
            this.tbox_result.Clear();
            ArrayList _rands = MakeRandomArray();
            string _strTemp = "";
            foreach (int _rand in _rands) {
                _strTemp += " " + _rand + " ";
            }
            tbox_result.AppendText(_strTemp + "\r\n");
        }
        private ArrayList MakeRandomArray() {
            ArrayList _nums = new ArrayList();
            Random _random = new Random();
            //int[] _nums = new int[9];
            int _cnt = 0;
            while (_cnt<9) {
                //int _rand = (_random.Next(100) * _random.Next(100)) % 9 + 1;
                int _rand = _random.Next(9);
                bool _exist = false;
                foreach(int _value in _nums) {
                    if (_value == _rand) {
                        _exist = true;
                        break;
                    } 
                }
                if(_exist == false) {
                    _nums.Add(_rand);
                    _cnt++;
                }
            }
            for(int _idx = 0; _idx<9;_idx++) {
                _nums[_idx] = (int)_nums[_idx] +1;
            }
            return _nums;
        }
        private bool check_insertable(int aRow, int aCol, int aValue) {
            bool _result = true;
            //수평비교
            for(int _cdx = 0; _cdx < 9; _cdx++) {
                if(m_values[aRow,_cdx] == aValue) {
                    _result = false;
                    break;
                }
            }
            //수직비교
            if(_result == true) {
                for (int _rdx = 0; _rdx < 9; _rdx++) {
                    if (m_values[_rdx, aCol] == aValue) {
                        _result = false;
                        break;
                    }
                }
            }

            //그룹비교
            if (_result == true) {
                int groupY = aRow / 3;
                int groupX = aCol / 3;
                for (int _rdx = 0; _rdx < 9; _rdx++) {
                    for (int _cdx = 0; _cdx < 9; _cdx++) {
                        if (groupX == _cdx / 3 && groupY == _rdx / 3 && m_values[_rdx, _cdx] == aValue) {
                            _result = false;
                            break;
                        }
                    }
                }
            }
            return _result;
        }
        private void btn_question_Click(object sender, EventArgs e) {
            bool _run_question = true;
            while (_run_question) {
                _run_question = false;

                for (int _rdx = 0; _rdx < 9; _rdx++) {
                    for (int _cdx = 0; _cdx < 9; _cdx++) {
                        m_values[_rdx, _cdx] = 0;
                    } 
                }

                for (int _rdx = 0; _rdx < 9; _rdx++) {
                    int _iTry = 0;
                    while (true) {
                        bool _line_ok = true;
                        ArrayList _rands = MakeRandomArray();
                        for (int _cdx = 0; _cdx < 9; _cdx++) {
                            bool _col_ok = false;
                            foreach (int _rand in _rands) {
                                if (check_insertable(_rdx, _cdx, _rand) == true) {
                                    m_values[_rdx, _cdx] = _rand;
                                    m_labels[_rdx, _cdx].Tag = _rand;
                                    //m_labels[_rdx, _cdx].Text = _rand.ToString();
                                    //m_labels[_rdx, _cdx].Tag = int.Parse(m_labels[_rdx, _cdx].Text);
                                    _rands.Remove(_rand);
                                    _col_ok = true;
                                    break;
                                }
                            }
                            if(_col_ok == false) {
                                for (int _ncdx = 0; _ncdx < 9; _ncdx++) {
                                    m_values[_rdx, _ncdx] = 0;
                                }
                                _line_ok = false;
                                break; 
                            }
                        }
                        if(_line_ok == true) { break; }
                        _iTry++;
                        if(_iTry>100000) {
                            _run_question = true;
                            _rdx = 10;
                            break;
                        }
                    }
                }
                //------------------------------------------

            }

        }


        private void cbox_level_SelectedIndexChanged(object sender, EventArgs e) {

        }
        private void btn_start_Click(object sender, EventArgs e) {
            int _step = cbox_level.SelectedIndex+1;
            
            for(int _grdx = 0; _grdx < 3;_grdx++) {
                for (int _gcdx = 0; _gcdx < 3; _gcdx++) {
                    System.Threading.Thread.Sleep(_gcdx+1);
                    ArrayList _survive = MakeRandomArray();
                    for (int _edx = 0; _edx < _step; _edx++) {
                        _survive.RemoveAt(_survive.Count -1);
                    }

                    for (int _rdx = _grdx*3; _rdx < (_grdx * 3)+3; _rdx++) {
                        for (int _cdx = _gcdx * 3; _cdx < (_gcdx * 3) + 3; _cdx++) {
                            int _tag = Convert.ToInt32(m_labels[_rdx,_cdx].Tag);
                            if (_survive.Contains(_tag) == true) {
                                m_labels[_rdx, _cdx].Text = _tag.ToString();
                            } else {
                                m_labels[_rdx, _cdx].Text = "";
                            }
                        }
                    }


                }
            }
        }

        private void btn_answeer_Click(object sender, EventArgs e) {

            //결과창에 표시하기
            tbox_result.Text = "";
            for (int _rdx = 0; _rdx < 9; _rdx++) {
                string _tempo = "";
                for (int _cdx = 0; _cdx < 9; _cdx++) {
                    //m_labels[_rdx, _cdx].Text = m_labels[_rdx, _cdx].Tag.ToString();
                    _tempo += " " + m_values[_rdx, _cdx];
                }
                tbox_result.AppendText(_tempo + "\r\n");
            }

        }
        private void btn_answeer2_Click(object sender, EventArgs e) {
            for (int _rdx = 0; _rdx < 9; _rdx++) {
                for (int _cdx = 0; _cdx < 9; _cdx++) {
                    m_labels[_rdx, _cdx].Text = m_labels[_rdx, _cdx].Tag.ToString();
                }
            }
        }
    }
}
