using System;
using System.Threading;
using System.Diagnostics;
using System.Management;

namespace FullCheckDiskDOS
{
    class Program
    {
        static void Main(string[] args)
        {
            DisplayInfo();

            while (true)
            {
                Console.Write("#> ");
                string choice = Console.ReadLine();
                if(choice == "y" || choice == "yes")
                {
                    Console.WriteLine("Run disk check...");
                    Thread.Sleep(2000);
                    Console.WriteLine("Scan disks...");
                    Thread.Sleep(5000);
                    Console.WriteLine("Disk scanning completed successfully!");
                    Thread.Sleep(1000);
                    for(int d = 0; d < 150; d++)
                    {
                        Thread.Sleep(1);
                        Console.Write("D: Scanning files - " + d + " files");
                        Thread.Sleep(2);
                        Console.Clear();
                    }

                    for(int c = 0; c < 150; c++)
                    {
                        Thread.Sleep(1);
                        Console.Write("C: Scanning files - " + c + " files");
                        Thread.Sleep(2);
                        Console.Clear();
                    }

                    Thread.Sleep(2000);
                    Console.WriteLine("The disks were successfully scanned and no errors were detected.");
                    Thread.Sleep(1000);
                    Console.WriteLine("Press Enter to exit Check Disk Program\n");
                    Console.ReadKey();
                    break;
                }
                else if(choice == "n" || choice == "no")
                {
                    Console.WriteLine("Exit...");
                    Thread.Sleep(1000);
                    break;
                }
                else
                {
                    Console.WriteLine("An unknown command was entered please try again");
                    Console.Clear();
                    DisplayInfo();
                }
            }
        }

        static void DisplayInfo()
        {
            Console.WriteLine("FULL CHECK DISK DOS PROGRAM");
            Console.WriteLine("Have you entered the program for checking and correcting disk errors ? Do you want to continue? (y/n)\n");
        }
    }
}