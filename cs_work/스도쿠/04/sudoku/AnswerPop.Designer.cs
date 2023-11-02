namespace sudoku {
    partial class AnswerPop {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing) {
            if (disposing && (components != null)) {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent() {
            this.panel1 = new System.Windows.Forms.Panel();
            this.panel2 = new System.Windows.Forms.Panel();
            this.tbox_answer = new System.Windows.Forms.TextBox();
            this.btn_answer = new System.Windows.Forms.Button();
            this.panel1.SuspendLayout();
            this.panel2.SuspendLayout();
            this.SuspendLayout();
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.btn_answer);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.panel1.Location = new System.Drawing.Point(0, 104);
            this.panel1.Name = "panel1";
            this.panel1.Padding = new System.Windows.Forms.Padding(15);
            this.panel1.Size = new System.Drawing.Size(154, 63);
            this.panel1.TabIndex = 0;
            // 
            // panel2
            // 
            this.panel2.Controls.Add(this.tbox_answer);
            this.panel2.Dock = System.Windows.Forms.DockStyle.Fill;
            this.panel2.Location = new System.Drawing.Point(0, 0);
            this.panel2.Name = "panel2";
            this.panel2.Padding = new System.Windows.Forms.Padding(20);
            this.panel2.Size = new System.Drawing.Size(154, 104);
            this.panel2.TabIndex = 1;
            // 
            // tbox_answer
            // 
            this.tbox_answer.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tbox_answer.Font = new System.Drawing.Font("굴림", 40F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(129)));
            this.tbox_answer.Location = new System.Drawing.Point(20, 20);
            this.tbox_answer.Name = "tbox_answer";
            this.tbox_answer.Size = new System.Drawing.Size(114, 69);
            this.tbox_answer.TabIndex = 0;
            this.tbox_answer.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.tbox_answer.KeyDown += new System.Windows.Forms.KeyEventHandler(this.tbox_answer_KeyDown);
            // 
            // btn_answer
            // 
            this.btn_answer.Dock = System.Windows.Forms.DockStyle.Fill;
            this.btn_answer.Location = new System.Drawing.Point(15, 15);
            this.btn_answer.Name = "btn_answer";
            this.btn_answer.Size = new System.Drawing.Size(124, 33);
            this.btn_answer.TabIndex = 0;
            this.btn_answer.Text = "입력";
            this.btn_answer.UseVisualStyleBackColor = true;
            this.btn_answer.Click += new System.EventHandler(this.btn_answer_Click);
            // 
            // AnswerPop
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(154, 167);
            this.Controls.Add(this.panel2);
            this.Controls.Add(this.panel1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "AnswerPop";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
            this.Text = "AnswerPop";
            this.Load += new System.EventHandler(this.AnswerPop_Load);
            this.panel1.ResumeLayout(false);
            this.panel2.ResumeLayout(false);
            this.panel2.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Button btn_answer;
        private System.Windows.Forms.Panel panel2;
        private System.Windows.Forms.TextBox tbox_answer;
    }
}