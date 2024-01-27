// BIOS DOS UTILITY [VERSION - 1.0]
// MOSIF CORPORATION

#include <iostream>
#include <thread>
#include <chrono>
#include <cstdlib>
#include <windows.h>
#include <fstream>

using namespace std;

class BIOS {
private:
    std::string OperatingSystem;
    std::string VideoCard;
    std::string CPU;
    std::string RAM;
    std::string shell;
    int MemoryRAM;
    int MemoryAmountDisk;
    float biosVersion;
public:
    BIOS(string OperatingSystem, string VideoCard, string CPU, string RAM, string shell, int MemoryRAM, int MemoryAmountDisk, float biosVersion) {
        this->OperatingSystem = OperatingSystem;
        this->VideoCard = VideoCard;
        this->CPU = CPU;
        this->RAM = RAM;
        this->shell = shell;
        this->MemoryRAM = MemoryRAM;
        this->MemoryAmountDisk = MemoryAmountDisk;
        this->biosVersion = biosVersion;
    }

    void PreventScreenChanges() {
        HWND console = GetConsoleWindow();
        SetWindowLong(console, GWL_STYLE, GetWindowLong(console, GWL_STYLE) & ~WS_THICKFRAME & ~WS_MAXIMIZEBOX);
    }

    void InformationSystem() {
        SYSTEM_INFO systemInfo;
        GetSystemInfo(&systemInfo);

        std::cout << "\t\t\t\t\t\tProcessor Architecture: " << systemInfo.dwProcessorType << std::endl;
        std::cout << "\t\t\t\t\t\tNumber of Processors: " << systemInfo.dwNumberOfProcessors << std::endl;
        std::cout << "\t\t\t\t\t\tPage Size: " << systemInfo.dwPageSize << " bytes" << std::endl;

        MEMORYSTATUSEX memoryStatus;
        memoryStatus.dwLength = sizeof(memoryStatus);
        GlobalMemoryStatusEx(&memoryStatus);

        std::cout << "\t\t\t\t\t\tTotal Physical Memory: " << memoryStatus.ullTotalPhys / (1024 * 1024) << " MB" << std::endl;
        std::cout << "\t\t\t\t\t\tAvailable Physical Memory: " << memoryStatus.ullAvailPhys / (1024 * 1024) << " MB" << std::endl;

        // BIOS VERSION
        std::cout << "\t\t\t\t\t\tBIOS Version: " << biosVersion << std::endl;

        SYSTEMTIME systemTime;
        GetLocalTime(&systemTime);

        std::cout << "\t\t\t\t\t\tSystem Time: " << systemTime.wHour << ":" << systemTime.wMinute << ":" << systemTime.wSecond << std::endl;
        std::cout << "\t\t\t\t\t\tDate: " << systemTime.wYear << "-" << systemTime.wMonth << "-" << systemTime.wDay << std::endl << "\n";
    }

    void StartingBIOS() {
        std::cout << "Starting bios..." << std::endl;
        std::this_thread::sleep_for(std::chrono::duration<double>(1.5));
        std::cout << "Scanning System..." << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(3));
    }

    void DisplayInfo() {
        std::system("cls");

        // BIOS LOGO
        std::cout << "\t\t\t\t\t\t ==============================" << std::endl;
        std::cout << "\t\t\t\t\t\t     BIOS DOS SETUP UTILITY" << std::endl;
        std::cout << "\t\t\t\t\t\t ==============================\n" << std::endl;

        InformationSystem();

        // Main menu
        std::cout << "\t\t\t\t\t\t ----------------------------" << std::endl;
        std::cout << "\t\t\t\t\t\t          Main menu:" << std::endl;
        std::cout << "\t\t\t\t\t\t ----------------------------" << std::endl;
        
        // Variants
        std::cout << "\t\t\t\t\t\t     1. Boot MOSIF OS" << std::endl;
        std::cout << "\t\t\t\t\t\t     2. BIOS UPDATE" << std::endl;
        std::cout << "\t\t\t\t\t\t     3. Boot from CD" << std::endl;
        std::cout << "\t\t\t\t\t\t     4. Shutdown" << "\n" << std::endl;
    }

    void OneVariant() {
        std::cout << "Loading MOSIF OS..." << std::endl;
        std::this_thread::sleep_for(std::chrono::duration<double>(3.0));
        std::string command = "ConsoleOS.exe";
        system(command.c_str());
    }

    void TwoVariant() {
        std::cout << "Checking update BIOS files..." << std::endl;
        std::this_thread::sleep_for(std::chrono::duration<double>(2.0));
        std::cout << "Could not find BIOS update files" << std::endl;
        std::this_thread::sleep_for(std::chrono::duration<double>(3.0));
    }

    void ThreeVariant() {
        std::cout << "Could not find bootable media" << std::endl;
        std::this_thread::sleep_for(std::chrono::duration<double>(2.0));
        system("cls");
        DisplayInfo();
    }

    void UserInput() {
        while (true) {
            std::cout << "Enter your choice (1-5): ";
            std::cin >> shell;

            if(shell == "1") {
                OneVariant();
                break;

            } else if(shell == "2") {
                TwoVariant();
                system("cls");
                DisplayInfo();

            } else if(shell == "3") {
                ThreeVariant();

            } else if(shell == "4") {
                break;

            } else {
                system("cls");
                DisplayInfo();
            }
        }
    }
};

int main() {
    BIOS bios("M.O.S.I.F", "NVIDIA Geforce RTX", "Intel Core i9", "ASUS DDR4", "shell", 12, 120, 1.0);
    bios.PreventScreenChanges();
    bios.StartingBIOS();
    if (!PlaySoundW(L"BIOS DOS UTILITY\\BIOS.wav", NULL, SND_ASYNC)) {

        return 1;
    }
    bios.DisplayInfo();
    bios.UserInput();
 
    return 0;
}