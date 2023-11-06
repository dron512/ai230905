using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace saju_project2.temp
{
    public class DailySaju
    {
        public UserData UserData { get; set; }
        public int Num;
        public string Direction;
        public string Color;
        public string Flavor;
        public string Fruit;
        public string Animal;
        public string BodyParts;
        public string Mind;
        public string Guide;
        public string NaverSummary; //이름 바꿔야됨
        public string NaverDetail; //이것도

        public DailySaju(int num, string direction, string color, string flavor, string fruit, string animal, string bodyParts, string mind, string guide, string naver1, string naver2)
        {
            Num = num;
            Direction = direction;
            Color = color;
            Flavor = flavor;
            Fruit = fruit;
            Animal = animal;
            BodyParts = bodyParts;
            Mind = mind;
            Guide = guide;
            NaverSummary = naver1;
            NaverDetail = naver2;
        }

        public static DailySaju MakeNewSaju(string json)
        {
            var data = JsonConvert.DeserializeObject<DailySaju>(json);
            return data;
         }
    }
}
