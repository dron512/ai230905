namespace mhapplication {
    partial class FirstCustomControl {
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

        #region 구성 요소 디자이너에서 생성한 코드

        /// <summary> 
        /// 디자이너 지원에 필요한 메서드입니다. 
        /// 이 메서드의 내용을 코드 편집기로 수정하지 마세요.
        /// </summary>
        private void InitializeComponent() {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(FirstCustomControl));
            label1 = new Label();
            button7 = new Button();
            button1 = new Button();
            button2 = new Button();
            button3 = new Button();
            pictureBox1 = new PictureBox();
            ((System.ComponentModel.ISupportInitialize)pictureBox1).BeginInit();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("배달의민족 한나는 열한살", 99.7499847F, FontStyle.Regular, GraphicsUnit.Point);
            label1.ForeColor = Color.FromArgb(255, 128, 0);
            label1.Location = new Point(91, 91);
            label1.Name = "label1";
            label1.Size = new Size(263, 141);
            label1.TabIndex = 0;
            label1.Text = "$19";
            // 
            // button7
            // 
            button7.FlatAppearance.BorderSize = 0;
            button7.FlatStyle = FlatStyle.Flat;
            button7.Font = new Font("배달의민족 도현", 14.2499981F, FontStyle.Bold, GraphicsUnit.Point);
            button7.Location = new Point(101, 234);
            button7.Name = "button7";
            button7.Size = new Size(126, 38);
            button7.TabIndex = 16;
            button7.Text = "Study";
            button7.UseVisualStyleBackColor = true;
            // 
            // button1
            // 
            button1.FlatAppearance.BorderSize = 0;
            button1.FlatStyle = FlatStyle.Flat;
            button1.Font = new Font("배달의민족 도현", 14.2499981F, FontStyle.Bold, GraphicsUnit.Point);
            button1.ForeColor = Color.FromArgb(255, 128, 0);
            button1.Location = new Point(91, 37);
            button1.Name = "button1";
            button1.Size = new Size(126, 38);
            button1.TabIndex = 16;
            button1.Text = "Only";
            button1.UseVisualStyleBackColor = true;
            // 
            // button2
            // 
            button2.FlatAppearance.BorderSize = 0;
            button2.FlatStyle = FlatStyle.Flat;
            button2.Font = new Font("배달의민족 도현", 14.2499981F, FontStyle.Bold, GraphicsUnit.Point);
            button2.Location = new Point(101, 278);
            button2.Name = "button2";
            button2.Size = new Size(628, 38);
            button2.TabIndex = 16;
            button2.Text = "orem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s";
            button2.UseVisualStyleBackColor = true;
            // 
            // button3
            // 
            button3.FlatAppearance.BorderSize = 0;
            button3.FlatStyle = FlatStyle.Flat;
            button3.Font = new Font("배달의민족 도현", 14.2499981F, FontStyle.Bold, GraphicsUnit.Point);
            button3.Location = new Point(101, 315);
            button3.Name = "button3";
            button3.Size = new Size(573, 38);
            button3.TabIndex = 16;
            button3.Text = "It is a long established fact that a reader will be distracted by the readable content of ";
            button3.UseVisualStyleBackColor = true;
            // 
            // pictureBox1
            // 
            pictureBox1.Image = (Image)resources.GetObject("pictureBox1.Image");
            pictureBox1.Location = new Point(475, 22);
            pictureBox1.Name = "pictureBox1";
            pictureBox1.Size = new Size(470, 197);
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.TabIndex = 18;
            pictureBox1.TabStop = false;
            // 
            // FirstCustomControl
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            Controls.Add(pictureBox1);
            Controls.Add(button1);
            Controls.Add(button3);
            Controls.Add(button2);
            Controls.Add(button7);
            Controls.Add(label1);
            Name = "FirstCustomControl";
            Size = new Size(991, 357);
            ((System.ComponentModel.ISupportInitialize)pictureBox1).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
        private Button button7;
        private Button button1;
        private Button button2;
        private Button button3;
        private PictureBox pictureBox1;
    }
}
