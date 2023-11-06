using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace saju_project2.temp
{
    [Serializable]
    public class UserData
    {
        public string Name; //이름
        public int BirthYear;//출생년도
        public int BirthMonth;//출생월
        public int BirthDay;//출생일
        public BirthTimeEnum BirthTime;//출생시간
        public bool isMale;//성별
        public string Calendar;//사용달력
        public UserData(string name, int birthYear, int birthMonth, int birthDay, BirthTimeEnum birthTime, bool isMale, string calendar)
        {
            Name = name;
            BirthYear = birthYear;
            BirthMonth = birthMonth;
            BirthDay = birthDay;
            BirthTime = birthTime;
            this.isMale = isMale;
            Calendar = calendar;
        }

        public string Serialize()
        {
            string json = JsonConvert.SerializeObject(this);
            return json;
        }
        public static BirthTimeEnum GetBirthTime(int index)
        {
            return (BirthTimeEnum)index;
        }
        public enum BirthTimeEnum {
            없음,
            자,
            축,
            인,
            묘,
            진,
            사,
            오,
            미,
            신,
            유,
            술,
            해
        };
    }
}
