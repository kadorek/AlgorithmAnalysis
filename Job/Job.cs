using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Job
{
    public class Job
    {
        static List<ConsoleColor> MuhtemelRenkler = new List<ConsoleColor> {
                                                                        ConsoleColor.Yellow,
                                                                        ConsoleColor.Red,
                                                                        ConsoleColor.Green,
                                                                        ConsoleColor.Cyan,
                                                                        ConsoleColor.Gray,
                                                                        ConsoleColor.Magenta};
        static Random rnd = new Random();
       // TimeSpan t = new TimeSpan();
        public TimeSpan Baslangic { get; set; }
        public TimeSpan Bitis { get; set; }

        ConsoleColor Yazi { get; set; }

        public int JobLength
        {
            get
            {
                return (int)(Bitis - Baslangic).TotalMinutes;
            }
        }


        public Job()
        {
            Baslangic = new TimeSpan();
            Bitis = new TimeSpan();
            do
            {
                Yazi = GetRandomConsoleColor();
            } while (Yazi == ConsoleColor.Black);

        }

        public static Job CreateJob(TimeLine tl)
        {
            Job j = new Job();
            do
            {
                j.Baslangic = tl.DayStart.Add(new TimeSpan(0, rnd.Next(tl.DayLengthMinute - tl.MaksJobLength), 0));
                j.Bitis = j.Baslangic.Add(new TimeSpan(0, rnd.Next(tl.MaksJobLength), 0));
            } while (j.JobLength > tl.MaksJobLength || j.JobLength < tl.MinJobLength);
            return j;
        }


        public void EkranaJobYaz(TimeLine tl)
        {
            Console.CursorSize = 20;
            TimeSpan fark = Baslangic - tl.DayStart;

            for (int i = 0; i < (int)Math.Ceiling(fark.TotalMinutes / 3.0); i++)
            {
                Console.Write("-");
            }
            Console.ForegroundColor = Yazi;
            for (int i = 0; i < (int)Math.Ceiling(JobLength / 3.0); i++)
            {
                Console.Write("*");
            }
            Console.ForegroundColor = ConsoleColor.White;
            TimeSpan sonFark = tl.DayFinish - Bitis;
            for (int i = 0; i < (int)Math.Ceiling(sonFark.TotalMinutes / 3.0); i++)
            {
                Console.Write("-");
            }
            Console.Write(" {0:hh\\:mm}-{1}dk. ", Baslangic, JobLength);
            Console.WriteLine();

        }


        public override string ToString()
        {
            return string.Format("{0}:{1}-{2}:{3}", Baslangic.Hours, Baslangic.Minutes, Bitis.Hours, Bitis.Minutes);
        }

        static ConsoleColor GetRandomConsoleColor()
        {
            return MuhtemelRenkler[rnd.Next(MuhtemelRenkler.Count)];
        }
    }
}
