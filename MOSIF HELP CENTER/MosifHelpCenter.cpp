#include <iostream>
#include <windows.h>
#include <cstdlib>
#include <fstream>
#include <string>
#include <thread>

using namespace std;

class HELPCENTER
{
private:
    std::string shell;
    std::string driveC;
    std::string driveD;
    float biosVersion;
public:
    HELPCENTER(string shell, string driveC, string driveD, float biosVersion)
    {
        this->shell = shell;
        this->driveC = driveC;
        this->driveD = driveD;
        this->biosVersion = biosVersion;
    }

    void PreventScreenChanges() 
    {
        HWND console = GetConsoleWindow();
        SetWindowLong(console, GWL_STYLE, GetWindowLong(console, GWL_STYLE) & ~WS_THICKFRAME & ~WS_MAXIMIZEBOX);
    }

    // 1 Variant

    void InformationSystem() 
    {
        SYSTEM_INFO systemInfo;
        GetSystemInfo(&systemInfo);

        std::cout << "Processor Architecture: " << systemInfo.dwProcessorType << std::endl;
        std::cout << "Number of Processors: " << systemInfo.dwNumberOfProcessors << std::endl;
        std::cout << "Page Size: " << systemInfo.dwPageSize << " bytes" << std::endl;

        MEMORYSTATUSEX memoryStatus;
        memoryStatus.dwLength = sizeof(memoryStatus);
        GlobalMemoryStatusEx(&memoryStatus);

        std::cout << "Total Physical Memory: " << memoryStatus.ullTotalPhys / (1024 * 1024) << " MB" << std::endl;
        std::cout << "Available Physical Memory: " << memoryStatus.ullAvailPhys / (1024 * 1024) << " MB" << std::endl;

        // BIOS VERSION
        std::cout << "BIOS Version: " << biosVersion << std::endl;

        SYSTEMTIME systemTime;
        GetLocalTime(&systemTime);

        std::cout << "System Time: " << systemTime.wHour << ":" << systemTime.wMinute << ":" << systemTime.wSecond << std::endl;
        std::cout << "Date: " << systemTime.wYear << "-" << systemTime.wMonth << "-" << systemTime.wDay << std::endl << "\n";
    }

    // 2 Variant

    void ScanningDrives()
    {
        for (int driveC = 0; driveC < 101; driveC++)
        {
            std::this_thread::sleep_for(std::chrono::duration<double>(0.5));
            std::cout << "Drive C Scanned - " << driveC << "%";
            system("cls");
        }

        for (int driveD = 0; driveD < 101; driveD++)
        {
            std::this_thread::sleep_for(std::chrono::duration<double>(0.5));
            std::cout << "Drive D Scanned - " << driveD << "%";
            system("cls");
        std::cout << "Disk D Syccefully Scanned!";
        std::this_thread::sleep_for(std::chrono::duration<double>(1.0));
        }
    }

    // C Language Syntax
    void DisplayInfo() 
    {
        printf(
            "+===================+\n"
            "| MOSIF HELP CENTER |\n"
            "+===================+\n\n"
        );

        std::cout << "Select the item that suits you:\n" << std::endl;

        printf(
            "1 - Show hardware information\n"
            "2 - Scanning your HDD/SSD\n"
            "3 - Repair your computer\n"
            "4 - Restoring/repairing MOSIF system files\n"
            "5 - Exit\n"
        );
    }

    void UserInput()
    {
        
    }
};

int main()
{
    HELPCENTER helpcenter("shell", "C", "D", 1.0);
    helpcenter.PreventScreenChanges();
    helpcenter.DisplayInfo();
    helpcenter.UserInput();

    return 0;
}