using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Job
{
    public class TimeLine
    {

        public TimeSpan DayStart { get; set; }
        public TimeSpan DayFinish { get; set; }
        public int MaksJobLength { get; set; } = 30;
        public int MinJobLength { get; set; } = 10;
        public int DayLengthMinute
        {
            get
            {
                return (int)((DayFinish - DayStart).TotalMinutes);
            }
        }





        public TimeLine(TimeSpan s, TimeSpan f)
        {
            DayStart = s;
            DayFinish = f;
        }



    }
}
