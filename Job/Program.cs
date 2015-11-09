using System;
using System.Collections.Generic;
using System.Linq;

namespace Job
{
    class Program
    {

        static void Main(string[] args)
        {


            var jobCount = 10;
            TimeLine tl = new TimeLine(TimeSpan.FromHours(10), TimeSpan.FromHours(13));
            List<Job> jobs = new List<Job>();

            for (int i = 0; i < jobCount; i++)
            {
                Job j = Job.CreateJob(tl);
                j.EkranaJobYaz(tl);
                jobs.Add(j);
            }

            var baslamaSaatiGruplu = jobs.OrderBy(x => x.JobLength).GroupBy(x => x.Baslangic).OrderBy(a => a.Key);
            var avaregeJobLength = jobs.Average(x => x.JobLength);
            Console.WriteLine("Ortalama Uzunluk : {0:0.00}", avaregeJobLength);

            Console.WriteLine();
            Console.WriteLine();

            var secilenler = new List<Job>();

            foreach (var group in baslamaSaatiGruplu)
            {

                var uyanlar = group.Where(x => x.JobLength < avaregeJobLength).ToList();
                if (secilenler.Count == 0)
                {
                    if (uyanlar.Count > 0)
                    {
                        secilenler.Add(uyanlar.Last());
                    }
                }
                else
                {
                    bool eklendiMi = false;
                    foreach (Job item in uyanlar)
                    {
                        if (item.Baslangic > secilenler.Last().Bitis)
                        {
                            secilenler.Add(item);
                            eklendiMi = true;
                            break;
                        }
                    }

                    if (!eklendiMi)
                    {
                        var buyukler = group.Where(x => x.JobLength > avaregeJobLength).OrderBy(x => x.JobLength).ToList();
                        foreach (Job item in buyukler)
                        {
                            if (secilenler.Count==0)
                            {
                                secilenler.Add(item);
                                break;
                            }
                            if (item.Baslangic > secilenler.Last().Bitis)
                            {
                                secilenler.Add(item);
                            }
                        }
                    }

                }

            }

            foreach (var item in secilenler)
            {
                item.EkranaJobYaz(tl);
            }


            Console.ReadLine();

        }






    }
}
