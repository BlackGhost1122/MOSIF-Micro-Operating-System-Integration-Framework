using System;
using Figgle;
using System.Threading;
using System.Management;
using System.Diagnostics;
using System.Drawing;
using System.IO;

namespace OperatingSystem 
{
    class OperatingSystem
    {
        private string shell;
        private string name;
        private string password;
        private string ConfirmPassword;

        public OperatingSystem(string shell, string name, string password, string ConfirmPassword) 
        {
            this.shell = shell;
            this.name = name;
            this.password = password;
            this.ConfirmPassword = ConfirmPassword;
        }

        public void ConsoleFunction() 
        {
            OpenPythonFiles("\"C:/Users/Admin/Desktop/System Files/Musics/WelcomeMusic.py");
            Console.WriteLine("Starting system...");
            Console.Clear();
            string asciiArt = FiggleFonts.Slant.Render("M.O.S.I.F 2.5");
            Console.Write(asciiArt);
            ConsoleColor originalColor = Console.ForegroundColor;
            Console.ForegroundColor = ConsoleColor.Blue;
            Console.WriteLine(@"
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@#B@@@@@@@@@@@@@@@@
@@@@@@@@@@#?. !#@@@@@@@@@@@@@@
@@@@@@@@B7. .?B@@@@@@@@@@@@@@@
@@@@@@G!  :J#@@@@@@G7?#@@@@@@@
@@@@P~  ^Y&@@@@@@@@J. .7B@@@@@
@&5^  ~P&@@@@@@@@@@@#Y:  !G@@@
@!  .P@@@@@@@@@@@@@@@@@Y   Y@@
@P^  ~P&@@@@@@@@@@@@@#Y^  !B@@
@@@P~  ^Y&@@@@@@@@@B?: .7B@@@@
@@@@@G!  :J#@@@@@@&J..J#@@@@@@
@@@@@@@B7. .?B@@@@@@##@@@@@@@@
@@@@@@@@@#?.  7&@@@@@@@@@@@@@@
@@@@@@@@@@@#Y7P@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            ");
            Console.ForegroundColor = ConsoleColor.White;
            Console.WriteLine("M.O.S.I.F [Version 2.5]");
            Console.WriteLine("Type 'help' to see a list of commands\n");

            while(true) 
            {
                Console.Write("#> ");
                this.shell = Console.ReadLine();
                if(this.shell == "help" || this.shell == "Help" || this.shell == "HELP") 
                {
                    string[] commands = {"Disk Info", "System Info", "Os Info", "File Manager", "Creators", "Mendel Info", "Data Time", "Machine Info", "cls | clear", "Shut Down", "Open Browser", "Activate Mos", "Browser Info", "Open Calculator", "Open Calculator DOS", "Open Notepad", "Download GUIM", "Open GUIM", "Open Mendel GUI"};
                    LoopingThroughArrayElementsHelp(commands);
                }
                else if(this.shell == "disk info" || this.shell == "Disk info" || this.shell == "Disk Info" || this.shell == "DISK INFO") 
                {
                    DisplayDiskInfo();
                }
                else if(this.shell == "os info" || this.shell == "Os info" || this.shell == "Os Info" || this.shell == "OS INFO") 
                {
                    Console.WriteLine("Operating System: M.O.S.I.F - Micro Operating System Integration Framework\n");
                }
                else if(this.shell == "file manager" || this.shell == "File manager" || this.shell == "File Manager" || this.shell == "FILE MANAGER") 
                {
                    OpenPythonFiles("\"C:/Users/Admin/Desktop/System Files/Utilites/FileManager.py");
                }
                else if(this.shell == "creators" || this.shell == "Creators" || this.shell == "CREATORS") 
                {
                    Console.WriteLine("\nDevelopers: Amin Aliyev, Tahirli Saleh");
                    Console.WriteLine("Engineer Computer: Eldar Ismaylov, Tahirli Saleh\n");
                }
                else if(this.shell == "mendel info" || this.shell == "Mendel info" || this.shell == "Mendel Info" || this.shell == "MENDEL INFO")
                {
                    MendeleevTableConsoleInfo();
                }
                else if(this.shell == "data time" || this.shell == "Data time" || this.shell == "Data Time" || this.shell == "DATA TIME") 
                {
                    Thread.Sleep(2000);
                    DateTime currentTime = DateTime.Now;

                    TimeZoneInfo azTimeZone = TimeZoneInfo.FindSystemTimeZoneById("Azerbaijan Standard Time");
                    DateTime azTime = TimeZoneInfo.ConvertTime(currentTime, TimeZoneInfo.Local, azTimeZone);
                    Console.WriteLine("Текущая дата и время в Азербайджане: " + azTime.ToString("yyyy-MM-dd HH:mm:ss") + "\n");

                    TimeZoneInfo chinaTimeZone = TimeZoneInfo.FindSystemTimeZoneById("China Standard Time");
                    DateTime chinaTime = TimeZoneInfo.ConvertTime(currentTime, TimeZoneInfo.Local, chinaTimeZone);
                    Console.WriteLine("Текущая дата и время в Китае: " + chinaTime.ToString("yyyy-MM-dd HH:mm:ss") + "\n");

                    TimeZoneInfo estTimeZone = TimeZoneInfo.FindSystemTimeZoneById("Eastern Standard Time");
                    DateTime estTime = TimeZoneInfo.ConvertTime(currentTime, TimeZoneInfo.Local, estTimeZone);
                    Console.WriteLine("Текущая дата и время на Восточном побережье США: " + estTime.ToString("yyyy-MM-dd HH:mm:ss") + "\n");

                    TimeZoneInfo msTimeZone = TimeZoneInfo.FindSystemTimeZoneById("Russian Standard Time");
                    DateTime msTime = TimeZoneInfo.ConvertTime(currentTime, TimeZoneInfo.Local, msTimeZone);
                    Console.WriteLine("Текущая дата и время в Москве: " + msTime.ToString("yyyy-MM-dd HH:mm:ss") + "\n");

                    TimeZoneInfo turkeyTimeZone = TimeZoneInfo.FindSystemTimeZoneById("Turkey Standard Time");
                    DateTime turkeyTime = TimeZoneInfo.ConvertTime(currentTime, TimeZoneInfo.Local, turkeyTimeZone);
                    Console.WriteLine("Текущая дата и время в Турции: " + turkeyTime.ToString("yyyy-MM-dd HH:mm:ss\n"));
                }
                else if(this.shell == "machine info" || this.shell == "Machine info" || this.shell == "Machine Info" || this.shell == "MACHINE INFO")
                {
                    Thread.Sleep(3000);
                    DisplayComputerInfo();
                }
                else if(this.shell == "cls" || this.shell == "Cls" || this.shell == "CLS" || this.shell == "clear" || this.shell == "Clear" || this.shell == "CLEAR") 
                {
                    Console.Clear();
                    //onsole.WriteLine(asciiArt);
                    Console.WriteLine("M.O.S.I.F [Version 2.0]");
                    Console.WriteLine("Type 'help' to see a list of commands\n");
                }
                else if(this.shell == "exit" || this.shell == "Exit" || this.shell == "EXIT") 
                {
                    Console.WriteLine("Shutting Down...");
                    Thread.Sleep(3000);
                    break;
                }
                else if(this.shell == "open browser" || this.shell == "Open browser" || this.shell == "Open Browser" || this.shell == "OPEN BROWSER") 
                {
                    OpenPythonFiles("\"C:/Users/Admin/Desktop/System Files/Utilites/BrowserOpen.py");
                }
                else if(this.shell == "activate mos" || this.shell == "Activate mos" || this.shell == "Activate Mos" || this.shell == "ACTIVATE MOS")
                {
                    OpenPythonFiles("\"C:/Users/Admin/Desktop/System Files/Activation.py");
                }
                else if(this.shell == "browser info" || this.shell == "Browser info" || this.shell == "Browser Info" || this.shell == "BROWSER INFO")
                {
                    Console.WriteLine("Browser: Chrome");
                    Console.WriteLine("Browser Version: 3.2\n");
                }
                else if(this.shell == "open calculator" || this.shell == "Open calculator" || this.shell == "Open Calculator" || this.shell == "OPEN CALCULATOR") 
                {
                    OpenPythonFiles("\"C:/Users/Admin/Desktop/System Files/Utilites/calculatorGUI.py");
                }
                else if(this.shell == "open calculator dos" || this.shell == "Open calculator dos" || this.shell == "Open Calculator dos" || this.shell == "Open Calculator Dos" || this.shell == "OPEN CALCULATOR DOS") 
                {
                    Console.Clear();
                    string exePath = @"C:/Users/Admin/Desktop/System Files/Utilites/ConsoleCalc.exe";

                    try
                    {
                        System.Diagnostics.Process.Start(exePath);
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine($"Ошибка: {ex.Message}");
                    }
                    break;
                }
                else if(this.shell == "open notepad" || this.shell == "Open notepad" || this.shell == "Open Notepad" || this.shell == "OPEN NOTEPAD") 
                {
                    OpenPythonFiles("\"C:/Users/Admin/Desktop/System Files/Utilites/notepad.py");
                }
                else if(this.shell == "shut down" || this.shell == "Shut down" || this.shell == "Shut Down" || this.shell == "SHUT DOWN") 
                {
                    OpenPythonFiles("\"C:/Users/Admin/Desktop/System Files/Musics/ShutDown.py");
                    Console.WriteLine("Shutting Down...");
                    Console.Clear();
                    break;
                }
                else if(this.shell == "download guim" || this.shell == "Download Guim" || this.shell == "DOWNLOAD GUIM") 
                {
                    Console.WriteLine("Downloading GUIM Version...");
                    Thread.Sleep(2000);
                    for(int i = 0; i < 20; i++) 
                    {
                        Thread.Sleep(1200);
                        Console.Write("#");
                    Console.WriteLine("\n");
                    }
                    Console.WriteLine("GUIM Downloaded!\n");
                }
                else if(this.shell == "run guim" || this.shell == "Run guim" || this.shell == "RUN GUIM") 
                {
                    ConsoleColor originallColor = Console.ForegroundColor;
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Error - 0x00001");
                    Console.ForegroundColor = ConsoleColor.White;
                }
                else if(this.shell == "open mendel gui" || this.shell == "Open Mendel Gui" || this.shell == "OPEN MENDEL GUI") 
                {
                    string exePath = @"C:/Users/Admin/Desktop/OperatingSystemGUIM/OperatingSystemGUIM/bin/Debug/OperatingSystemGUIM";
                    try 
                    {
                        System.Diagnostics.Process.Start(exePath);
                    }
                    catch(Exception ex) 
                    {
                        Console.WriteLine($"Ошибка: {ex.Message}");
                    }
                }
//                else if(this.shell == "open office manager" || this.shell == "Open office manager" || this.shell == "Open Office manager" || this.shell == "Open Office Manager" || this.shell == "OPEN OFFICE MANAGER") 
//                {
//                    OpenPythonFiles("\"C:/Users/Admin/Desktop/System Files/MicrosoftOfficeManager.py");
//                }
                else 
                {
                    ConsoleColor origoinalColor = Console.ForegroundColor;
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("\nError! An unknown command was entered, please try again\n");
                    Console.ForegroundColor = ConsoleColor.White;
                }
            }
        }

        public void LoopingThroughArrayElementsHelp(string[] help)
        {
            foreach(string el in help) 
            {
                Console.WriteLine("Commands: " + el);
            }
        }

        public void DisplayDiskInfo() 
        {
            Console.WriteLine("\nИнформация о дисках:");

            ObjectQuery query = new ObjectQuery("SELECT * FROM Win32_LogicalDisk");
            ManagementObjectSearcher searcher = new ManagementObjectSearcher(query);
            ManagementObjectCollection collection = searcher.Get();

            foreach (ManagementObject m in collection)
            {
                Console.WriteLine("Диск " + m["DeviceID"] + ":");
                Console.WriteLine("  Тип: " + m["DriveType"]);
                Console.WriteLine("  Объем емкости: " + m["Size"] + " байт");
            }
        }

        public void OpenExeFiles(string filepath) {
            try 
            {
                Process process = new Process();
                process.StartInfo.FileName = filepath;
                process.Start();
            }
            catch(Exception ex) 
            {
                Console.WriteLine($"Произошла ошибка: {ex.Message}");
            }
        }

        public void OpenPythonFiles(string filepath) 
        {
            Process process = new Process();
            process.StartInfo.FileName = "python";
            process.StartInfo.Arguments = filepath;
            process.StartInfo.UseShellExecute = false;
            process.StartInfo.RedirectStandardOutput = true;

            process.Start();

            string output = process.StandardOutput.ReadToEnd();
            process.WaitForExit();

            Console.WriteLine(output);
        }

        public void WelcomeMusic() 
        {
            
        }

        public void MendeleevTableConsoleInfo() 
        {
            Console.WriteLine("\n---------- Менделеевская таблица ----------\n");
            Console.WriteLine("№ | Элемент  | Символ | Атомная масса");
            Console.WriteLine("1, 'Водород', 'H', 1.008");
            Console.WriteLine("2, 'Гелий', 'He', 4.0026");
            Console.WriteLine("3, 'Литий', 'Li', 6.94");
            Console.WriteLine("4, 'Бериллий', 'Be', 9.0122");
            Console.WriteLine("5, 'Бор', 'B', 10.81");
            Console.WriteLine("6, 'Углерод', 'C', 12.011");
            Console.WriteLine("7, 'Азот', 'N', 14.007");
            Console.WriteLine("8, 'Кислород', 'O', 15.999");
            Console.WriteLine("9, 'Фтор', 'F', 18.998");
            Console.WriteLine("10, 'Неон', 'Ne', 20.180");
            Console.WriteLine("11, 'Натрий', 'Na', 22.990");
            Console.WriteLine("12, 'Магний', 'Mg', 24.305");
            Console.WriteLine("13, 'Алюминий', 'Al', 26.982");
            Console.WriteLine("14, 'Кремний', 'Si', 28.085");
            Console.WriteLine("15, 'Фосфор', 'P', 30.974");
            Console.WriteLine("16, 'Сера', 'S', 32.06");
            Console.WriteLine("17, 'Хлор', 'Cl', 35.45");
            Console.WriteLine("18, 'Аргон', 'Ar', 39.948");
            Console.WriteLine("19, 'Калий', 'K', 39.098");
            Console.WriteLine("20, 'Кальций', 'Ca', 40.078");
            Console.WriteLine("21, 'Скандий', 'Sc', 44.956");
            Console.WriteLine("22, 'Титан', 'Ti', 47.867");
            Console.WriteLine("23, 'Ванадий', 'V', 50.942");
            Console.WriteLine("24, 'Хром', 'Cr', 51.996");
            Console.WriteLine("25, 'Марганец', 'Mn', 54.938");
            Console.WriteLine("26, 'Железо', 'Fe', 55.845");
            Console.WriteLine("27, 'Кобальт', 'Co', 58.933");
            Console.WriteLine("28, 'Никель', 'Ni', 58.693");
            Console.WriteLine("29, 'Медь', 'Cu', 63.546");
            Console.WriteLine("30, 'Цинк', 'Zn', 65.38");
            Console.WriteLine("31, 'Галлий', 'Ga', 69.723");
            Console.WriteLine("32, 'Германий', 'Ge', 72.630");
            Console.WriteLine("33, 'Мышьяк', 'As', 74.922");
            Console.WriteLine("34, 'Селен', 'Se', 78.971");
            Console.WriteLine("35, 'Бром', 'Br', 79.904");
            Console.WriteLine("36, 'Криптон', 'Kr', 83.798");
            Console.WriteLine("37, 'Рубидий', 'Rb', 85.468");
            Console.WriteLine("38, 'Стронций', 'Sr', 87.620");
            Console.WriteLine("39, 'Иттрий', 'Y', 88.906");
            Console.WriteLine("40, 'Цирконий', 'Zr', 91.224");
            Console.WriteLine("41, 'Ниобий', 'Nb', 92.906");
            Console.WriteLine("42, 'Молибден', 'Mo', 95.950");
            Console.WriteLine("43, 'Технеций', 'Tc', (98))");
            Console.WriteLine("44, 'Рутений', 'Ru', 101.070");
            Console.WriteLine("45, 'Родий', 'Rh', 102.906");
            Console.WriteLine("46, 'Палладий', 'Pd', 106.420");
            Console.WriteLine("47, 'Серебро', 'Ag', 107.868");
            Console.WriteLine("48, 'Кадмий', 'Cd', 112.414");
            Console.WriteLine("49, 'Индий', 'In', 114.818");
            Console.WriteLine("50, 'Олово', 'Sn', 118.710");
            Console.WriteLine("51, 'Антимоний', 'Sb', 121.760");
            Console.WriteLine("52, 'Теллур', 'Te', 127.600");
            Console.WriteLine("53, 'Иод', 'I', 126.904");
            Console.WriteLine("54, 'Ксенон', 'Xe', 131.293");
            Console.WriteLine("55, 'Цезий', 'Cs', 132.905");
            Console.WriteLine("56, 'Барий', 'Ba', 137.327");
            Console.WriteLine("57-71, 'Лантаноиды', 'La-Lu', -");
            Console.WriteLine("72, 'Гафний', 'Hf', 178.490");
            Console.WriteLine("73, 'Тантал', 'Ta', 180.948");
            Console.WriteLine("74, 'Вольфрам', 'W', 183.840");
            Console.WriteLine("75, 'Рений', 'Re', 186.207");
            Console.WriteLine("76, 'Осмий', 'Os', 190.230");
            Console.WriteLine("77, 'Иридий', 'Ir', 192.217");
            Console.WriteLine("78, 'Платина', 'Pt', 195.084");
            Console.WriteLine("79, 'Золото', 'Au', 196.967");
            Console.WriteLine("80, 'Ртуть', 'Hg', 200.592");
            Console.WriteLine("81, 'Таллий', 'Tl', 204.380");
            Console.WriteLine("82, 'Свинец', 'Pb', 207.200");
            Console.WriteLine("83, 'Висмут', 'Bi', 208.980");
            Console.WriteLine("84, 'Полоний', 'Po', 209");
            Console.WriteLine("85, 'Астат', 'At', 210");
            Console.WriteLine("86, 'Радон', 'Rn', 222");
            Console.WriteLine("87, 'Франций', 'Fr', 223");
            Console.WriteLine("88, 'Радий', 'Ra', 226");
            Console.WriteLine("89-103, 'Актиноиды', 'Ac-Lr'");
            Console.WriteLine("104, 'Резерфордий', 'Rf', (267)");
            Console.WriteLine("105, 'Дубний', 'Db', 270");
            Console.WriteLine("106, 'Сиборгий', 'Sg', 271");
            Console.WriteLine("107, 'Борий', 'Bh', '270'");
            Console.WriteLine("108, 'Хассий', 'Hs', 277");
            Console.WriteLine("109, 'Мейтнерий', 'Mt', 276");
            Console.WriteLine("110, 'Дармштадтий', 'Ds', 281");
            Console.WriteLine("111, 'Рентгений', 'Rg', 280");
            Console.WriteLine("112, 'Коперниций', 'Cn', 285");
            Console.WriteLine("113, 'Нихоний', 'Nh', 284");
            Console.WriteLine("114, 'Флеровий', 'Fl', 289");
            Console.WriteLine("115, 'Московий', 'Mc', 288");
            Console.WriteLine("116, 'Ливерморий', 'Lv', 293");
            Console.WriteLine("117, 'Теннессин', 'Ts', 294");
            Console.WriteLine("118, 'Оганессон', 'Og', 294\n");
        }

        public void DisplayComputerInfo() 
        {
            Console.WriteLine("Информация о компьютере:");

            ObjectQuery query = new ObjectQuery("SELECT * FROM Win32_ComputerSystem");
            ManagementObjectSearcher searcher = new ManagementObjectSearcher(query);
            ManagementObjectCollection collection = searcher.Get();

            foreach (ManagementObject m in collection)
            {
                Console.WriteLine("Модель: " + m["Model"]);
                Console.WriteLine("Имя компьютера: " + m["Name"]);
            }

            Console.WriteLine("\nИнформация о дисках:");

            query = new ObjectQuery("SELECT * FROM Win32_LogicalDisk");
            searcher = new ManagementObjectSearcher(query);
            collection = searcher.Get();

            Console.WriteLine("\nИнформация об оперативной памяти:");

            query = new ObjectQuery("SELECT * FROM Win32_ComputerSystem");
            searcher = new ManagementObjectSearcher(query);
            collection = searcher.Get();

            foreach (ManagementObject m in collection)
            {
                Console.WriteLine("Объем оперативной памяти: " + m["TotalPhysicalMemory"] + " байт\n");
            }
        }

        public void ImageOSLogo() 
        {
            Console.Write(@"              
                                    ..                      
                                  .oKXx,.                   
                                .oKWMWO;.                   
                              .oKWMWO:.                     
                            .oXMMWO:.          ;l,          
                          'oXWMNO:.          .dNMNx,        
                        'dXMMNO:.             ,xNMMNx,      
                      'dXMMNk;.                 ,xXMMNx,    
                     cXMMNk;                      'dXMMNd.  
                    .kMMMK:                        'OMMMK,  
                     'kNMMXx,                    .lKWWWO;   
                       ;kNMMXx,                .lKWMNO:.    
                         ;kNMMNx,            .lKWWNO:.      
                           ,xNMMNx,          .c0NO:.        
                             ,xNMMNx,          .'.          
                               ,xNMMNx,                     
                                 ,xNMWX:.                   
                                   ,xk:.
            ");
        }

    }
    class Program 
    {
        static void Main() 
        {
            OperatingSystem operatingSystem = new OperatingSystem("shell", "name", "password", "confirm password");
            operatingSystem.ConsoleFunction();
        }
    }
}