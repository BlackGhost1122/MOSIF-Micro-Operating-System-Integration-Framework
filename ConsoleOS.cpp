#include <iostream>
#include <windows.h>
#include <chrono>
#include <ctime>
#include <iomanip>
#include <cstdlib>
#include <fstream>
#include <thread>
#include <string>

using namespace std;

class MOSIF_ENTERPRISE
{
private:
    std::string shell;
    float biosVersion;

public:
    MOSIF_ENTERPRISE(string shell, float biosVersion)
    {
        this->shell = shell;
        this->biosVersion = biosVersion;
    }

    void FullScreen()
    {
        HWND consoleWindow = GetConsoleWindow();
        ShowWindow(consoleWindow, SW_MAXIMIZE);
        SetConsoleTitle("");
        LONG style = GetWindowLong(consoleWindow, GWL_STYLE);
        style &= ~(WS_CAPTION | WS_THICKFRAME | WS_MINIMIZEBOX | WS_MAXIMIZEBOX | WS_SYSMENU);
        SetWindowLong(consoleWindow, GWL_STYLE, style);
        SetWindowPos(consoleWindow, NULL, 0, 0, 0, 0, SWP_NOSIZE | SWP_NOMOVE | SWP_NOZORDER | SWP_FRAMECHANGED);
    }

    void HideTaskbar()
    {
        // Hide taskbar windows
        HWND taskbar = FindWindow("Shell_TrayWnd", NULL);
        ShowWindow(taskbar, SW_HIDE);
    }

    void RestoreTaskbar()
    {
        // Restore taskbar windows
        HWND taskbar = FindWindow("Shell_TrayWnd", NULL);
        ShowWindow(taskbar, SW_SHOW);
    }

    void DisplayInfo()
    {
        system("cls");

        HANDLE consoleHandle = GetStdHandle(STD_OUTPUT_HANDLE);
        SetConsoleTextAttribute(consoleHandle, FOREGROUND_BLUE);

        std::cout << R"(
     __  ___  ____   _____   ____   ______
    /  |/  / / __ \ / ___/  /  _/  / ____/
   / /|_/ / / / / / \__ \   / /   / /_
  / /  / /_/ /_/ / ___/ / _/ / _ / __/
 /_/  /_/(_)____(_)____(_)___/(_)_/

     ______      __                       _
    / ____/___  / /____  _________  _____(_)_______
   / __/ / __ \/ __/ _ \/ ___/ __ \/ ___/ / ___/ _ \
  / /___/ / / / /_/  __/ /  / /_/ / /  / (__  )  __/
 /_____/_/ /_/\__/\___/_/  / .___/_/  /_/____/\___/
                          /_/

        )" << std::endl;

        std::cout << R"(
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

        )" << std::endl;

        std::cout << " M.O.S.I.F [Version 2.5]" << std::endl;
        std::cout << " Type 'help' to see a list of commands\n" << std::endl;

        SetConsoleTextAttribute(consoleHandle, 15);
    }

    void CommandsList()
    {
        std::cout << R"(
 +------------------------------+
 | command: help                |
 | command: open file manager   |
 | command: disk info           |
 | command: os info             |
 | command: system info         |
 | command: open office manager |
 | command: creators            |
 | command: mendel info         |
 | command: data time           |
 | command: cls\clear           |
 | command: shut down/Ctrl+C    |
 | command: restart             |
 | command: open browser\info   |
 | command: activate mos        |
 | command: open calculator     |
 | command: open mendel gui     |
 | command: open notepad        |
 | command: open help center    |
 | command: BIOS DOS            |
 | command: BIOS GUI            |
 +------------------------------+
        )" << std::endl;
    }

    void FileManager()
    {
        std::thread([](){
            system("python FileManager.py");
        }).detach();
    }

    void DriveInfo()
    {
        DWORD drives = GetLogicalDrives();

        for (char drive = 'A'; drive <= 'Z'; ++drive)
        {
            if (drives & 1)
            {
                std::string rootPath = std::string(1, drive) + ":\\";
                DWORD sectorsPerCluster, bytesPerSector, numberOfFreeClusters, totalNumberOfClusters;

                if (GetDiskFreeSpace(rootPath.c_str(), &sectorsPerCluster, &bytesPerSector, &numberOfFreeClusters, &totalNumberOfClusters))
                {
                    std::cout << "Drive: " << rootPath << std::endl;
                    std::cout << "  Sectors per cluster: " << sectorsPerCluster << std::endl;
                    std::cout << "  Bytes per sector: " << bytesPerSector << std::endl;
                    std::cout << "  Free clusters: " << numberOfFreeClusters << std::endl;
                    std::cout << "  Total clusters: " << totalNumberOfClusters << std::endl;
                    std::cout << "  Total size (bytes): " << totalNumberOfClusters * sectorsPerCluster * bytesPerSector << std::endl;
                    std::cout << "  Free space (bytes): " << numberOfFreeClusters * sectorsPerCluster * bytesPerSector << std::endl;
                }
            }
                drives >>= 1;
        }
    }

    void OsInfo()
    {
        std::cout << " M.O.S.I.F - Micro Operating System Integration Framework" << std::endl;
        std::cout << " M.O.S.I.F Enterprise [Version - 4.1]\n" << std::endl;
    }

    void SystemInfo()
    {
        SYSTEM_INFO systemInfo;
        GetSystemInfo(&systemInfo);

        std::cout << " Processor Architecture: " << systemInfo.dwProcessorType << std::endl;
        std::cout << " Number of Processors: " << systemInfo.dwNumberOfProcessors << std::endl;
        std::cout << " Page Size: " << systemInfo.dwPageSize << " bytes" << std::endl;

        MEMORYSTATUSEX memoryStatus;
        memoryStatus.dwLength = sizeof(memoryStatus);
        GlobalMemoryStatusEx(&memoryStatus);

        std::cout << " Total Physical Memory: " << memoryStatus.ullTotalPhys / (1024 * 1024) << " MB" << std::endl;
        std::cout << " Available Physical Memory: " << memoryStatus.ullAvailPhys / (1024 * 1024) << " MB" << std::endl;

        // BIOS VERSION
        std::cout << " BIOS Version: " << biosVersion << std::endl;

        SYSTEMTIME systemTime;
        GetLocalTime(&systemTime);

        std::cout << " System Time: " << systemTime.wHour << ":" << systemTime.wMinute << ":" << systemTime.wSecond << std::endl;
        std::cout << " Date: " << systemTime.wYear << "-" << systemTime.wMonth << "-" << systemTime.wDay << std::endl << "\n";
    }

    void MicrosoftOfficeManager()
    {
        std::thread([](){
            system("python MicrosoftOfficeManager.py");
        }).detach();
    }

    void Creators()
    {
        std::cout << R"(
 +---------------------------------------------+       
 |  Name     Surname      Work        Active   |
 +---------------------------------------------+
 |  Amin     Aliyev     Developer      True    |
 |  Saleh    Tahirli    Devel\Comp     True    |
 |  Eldar    Ismaylov   Eng Comp       True    |
 |  Ugur     Ragimov    Developer      True    |
 |  Rasul    Mamedli    Devel\Audio    True    |
 |  Elmar      ???      Developer      False   |
 +---------------------------------------------+
        )" << std::endl;
    }

    void MendelInfo()
    {
        std::cout << R"(
---------- Менделеевская таблица ---------+
 "№ | Элемент  | Символ | Атомная мас
 "1, 'Водород', 'H', 1.008"
 "2, 'Гелий', 'He', 4.0026"
 "3, 'Литий', 'Li', 6.94"
 "4, 'Бериллий', 'Be', 9.0122"
 "5, 'Бор', 'B', 10.81"
 "6, 'Углерод', 'C', 12.011"
 "7, 'Азот', 'N', 14.007"
 "8, 'Кислород', 'O', 15.999"
 "9, 'Фтор', 'F', 18.998"
 "10, 'Неон', 'Ne', 20.180"
 "11, 'Натрий', 'Na', 22.990"
 "12, 'Магний', 'Mg', 24.305"
 "13, 'Алюминий', 'Al', 26.982"
 "14, 'Кремний', 'Si', 28.085"
 "15, 'Фосфор', 'P', 30.974"
 "16, 'Сера', 'S', 32.06"
 "17, 'Хлор', 'Cl', 35.45"
 "18, 'Аргон', 'Ar', 39.948"
 "19, 'Калий', 'K', 39.098"
 "20, 'Кальций', 'Ca', 40.078"
 "21, 'Скандий', 'Sc', 44.956"
 "22, 'Титан', 'Ti', 47.867"
 "23, 'Ванадий', 'V', 50.942"
 "24, 'Хром', 'Cr', 51.996"
 "25, 'Марганец', 'Mn', 54.938"
 "26, 'Железо', 'Fe', 55.845"
 "27, 'Кобальт', 'Co', 58.933"
 "28, 'Никель', 'Ni', 58.693"
 "29, 'Медь', 'Cu', 63.546"
 "30, 'Цинк', 'Zn', 65.38"
 "31, 'Галлий', 'Ga', 69.723"
 "32, 'Германий', 'Ge', 72.630"
 "33, 'Мышьяк', 'As', 74.922"
 "34, 'Селен', 'Se', 78.971"
 "35, 'Бром', 'Br', 79.904"
 "36, 'Криптон', 'Kr', 83.798"
 "37, 'Рубидий', 'Rb', 85.468"
 "38, 'Стронций', 'Sr', 87.620"
 "39, 'Иттрий', 'Y', 88.906"
 "40, 'Цирконий', 'Zr', 91.224"
 "41, 'Ниобий', 'Nb', 92.906"
 "42, 'Молибден', 'Mo', 95.950"
 "43, 'Технеций', 'Tc', (98))"
 "44, 'Рутений', 'Ru', 101.070"
 "45, 'Родий', 'Rh', 102.906"
 "46, 'Палладий', 'Pd', 106.420"
 "47, 'Серебро', 'Ag', 107.868"
 "48, 'Кадмий', 'Cd', 112.414"
 "49, 'Индий', 'In', 114.818"
 "50, 'Олово', 'Sn', 118.710"
 "51, 'Антимоний', 'Sb', 121.760"
 "52, 'Теллур', 'Te', 127.600"
 "53, 'Иод', 'I', 126.904"
 "54, 'Ксенон', 'Xe', 131.293"
 "55, 'Цезий', 'Cs', 132.905"
 "56, 'Барий', 'Ba', 137.327"
 "57-71, 'Лантаноиды', 'La-Lu"
 "72, 'Гафний', 'Hf', 178.490"
 "73, 'Тантал', 'Ta', 180.948"
 "74, 'Вольфрам', 'W', 183.840"
 "75, 'Рений', 'Re', 186.207"
 "76, 'Осмий', 'Os', 190.230"
 "77, 'Иридий', 'Ir', 192.217"
 "78, 'Платина', 'Pt', 195.084"
 "79, 'Золото', 'Au', 196.967"
 "80, 'Ртуть', 'Hg', 200.592"
 "81, 'Таллий', 'Tl', 204.380"
 "82, 'Свинец', 'Pb', 207.200"
 "83, 'Висмут', 'Bi', 208.980"
 "84, 'Полоний', 'Po', 209"
 "85, 'Астат', 'At', 210"
 "86, 'Радон', 'Rn', 222"
 "87, 'Франций', 'Fr', 223"
 "88, 'Радий', 'Ra', 226"
 "89-103, 'Актиноиды', 'Ac-Lr'"
 "104, 'Резерфордий', 'Rf', (267)"
 "105, 'Дубний', 'Db', 270"
 "106, 'Сиборгий', 'Sg', 271"
 "107, 'Борий', 'Bh', '270'"
 "108, 'Хассий', 'Hs', 277"
 "109, 'Мейтнерий', 'Mt', 276"
 "110, 'Дармштадтий', 'Ds', 281"
 "111, 'Рентгений', 'Rg', 280"
 "112, 'Коперниций', 'Cn', 285"
 "113, 'Нихоний', 'Nh', 284"
 "114, 'Флеровий', 'Fl', 289"
 "115, 'Московий', 'Mc', 288"
 "116, 'Ливерморий', 'Lv', 293"
 "117, 'Теннессин', 'Ts', 294"
 "118, 'Оганессон', 'Og', 294)" << std::endl;
    }

    void DataTime()
    {
        std::time_t now = std::time(nullptr);
        std::tm* utc_time = std::gmtime(&now);

       
        const int turkish_offset = 3;
        const int azerbaijan_offset = 4;
        const int russian_offset = 3;
        const int chinese_offset = 8;
        const int american_est_offset = -5;

        std::tm* turkish_time = std::gmtime(&now);
        turkish_time->tm_hour += turkish_offset;

        std::tm* azerbaijan_time = std::gmtime(&now);
        azerbaijan_time->tm_hour += azerbaijan_offset;

        std::tm* russian_time = std::gmtime(&now);
        russian_time->tm_hour += russian_offset;

        std::tm* chinese_time = std::gmtime(&now);
        chinese_time->tm_hour += chinese_offset;

        std::tm* american_est_time = std::gmtime(&now);
        american_est_time->tm_hour += american_est_offset;

        std::cout << " Current time in Turkey: " << std::put_time(turkish_time, "%c %Z") << std::endl;
        std::cout << " Current time in Azerbaijan: " << std::put_time(azerbaijan_time, "%c %Z") << std::endl;
        std::cout << " Current time in Russia: " << std::put_time(russian_time, "%c %Z") << std::endl;
        std::cout << " Current time in China: " << std::put_time(chinese_time, "%c %Z") << std::endl;
        std::cout << " Current time in America (EST): " << std::put_time(american_est_time, "%c %Z") << std::endl;

    }

    void ActivateMos()
    {
        std::thread([](){
            system("python Activation.py");
        }).detach();
    }

    void Calculator()
    {
        std::thread([](){
            system("python calculatorGUI.py");
        }).detach();
    }

    void NotePad()
    {
        std::thread([](){
            system("python notepad.py");
        }).detach();
    }

    void BIOS_DOS()
    {
        std::thread([](){
            system("BIOS.exe");
        }).detach();
    }

    void UserInputCommands()
    {
        while (std::cout << " #> ", std::getline(std::cin, shell))
        {
            if (shell == "help")
            {
                CommandsList();
            }

            else if (shell == "open file manager" || shell == "Open file manager" || shell == "Open File manager" || shell == "Open File Manager" || shell == "OPEN FILE MANAGER")
            {
                FileManager();
            }

            else if (shell == "disk info" || shell == "Disk info" || shell == "Disk Info" || shell == "DISK INFO")
            {
                DriveInfo();
            }

            else if (shell == "os info" || shell == "Os info" || shell == "Os Info" || shell == "OS INFO")
            {
                OsInfo();
            }

            else if (shell == "system info" || shell == "System info" || shell == "System Info" || shell == "SYSTEM INFO")
            {
                SystemInfo();
            }

            else if (shell == "open office manager" || shell == "Open office manager" || shell == "Open Office manager" || shell == "Open Office Manager" || shell == "OPEN OFFICE MANAGER")
            {
                MicrosoftOfficeManager();
            }

            else if (shell == "creators" || shell == "Creators" || shell == "CREATORS")
            {
                Creators();
            }

            else if (shell == "mendel info" || shell == "Mendel info" || shell == "Mendel Info" || shell == "MENDEL INFO")
            {
                MendelInfo();
            }

            else if (shell == "data time" || shell == "Data time" || shell == "Data Time" || shell == "DATA TIME")
            {
                DataTime();
            }

            else if (shell == "cls" || shell == "Cls" || shell == "CLS" || shell == "clear" || shell == "Clear" || shell == "CLEAR")
            {
                system("cls");
                DisplayInfo();
            }

            else if (shell == "shut down" || shell == "Shut down" || shell == "Shut Down" || shell == "SHUT DOWN")
            {
                system("shutdown /s /t 0");
            }

            else if (shell == "restart" || shell == "Restart" || shell == "RESTART")
            {
                system("shutdown /r /t 0");
            }

            else if (shell == "open browser" || shell == "Open browser" || shell == "Open Browser" || shell == "OPEN BROWSER")
            {
                const char* url = "https://google.com";
                ShellExecute(NULL, "open", url, NULL, NULL, SW_SHOWNORMAL);
            }

            else if (shell == "activate mos" || shell == "Activate mos" || shell == "Activate Mos" || shell == "ACTIVATE MOS")
            {
                ActivateMos();
            }

            else if (shell == "open calculator" || shell == "Open calculator" || shell == "Open Calculator" || shell == "OPEN CALCULATOR")
            {
                Calculator();
            }

            else if (shell == "open notepad" || shell == "Open notepad" || shell == "Open Notepad" || shell == "OPEN NOTEPAD")
            {
                NotePad();
            }

            else if (shell == "bios dos" || shell == "Bios dos" || shell == "Bios Dos" || shell == "BIOS DOS")
            {
                BIOS_DOS();
            }

            else if (shell == "exit" || shell == "Exit" || shell == "EXIT")
            {
                RestoreTaskbar();
                break;
            }

            else
            {
                HANDLE consoleHandle = GetStdHandle(STD_OUTPUT_HANDLE);
                SetConsoleTextAttribute(consoleHandle, FOREGROUND_RED);
                std::cout << " Error! Unknown command please try again\n" << std::endl;
                SetConsoleTextAttribute(consoleHandle, 15);
            }
        }
    }


};

int main()
{
    setlocale(LC_ALL, "RU");

    MOSIF_ENTERPRISE mosif_enterprise("shell", 1.0);
    mosif_enterprise.HideTaskbar();
    mosif_enterprise.FullScreen();
    mosif_enterprise.DisplayInfo();
    mosif_enterprise.UserInputCommands();

    mosif_enterprise.RestoreTaskbar();
    return 0;
}
