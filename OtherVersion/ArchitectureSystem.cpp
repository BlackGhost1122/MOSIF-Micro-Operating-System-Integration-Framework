#include <iostream>
#include <string>
#include <thread>
#include <fstream>
#include <cstdlib>

using namespace std;

class ArchitectureSystemInfo {
private:
    string os;
    string disk_type;
    int memory_disk;
    string name_video_card;
    int memory_video_card;
    int bit;
    string cpu;
    int ram;
public:
    ArchitectureSystemInfo(string os, string disk_type, int memory_disk, string name_video_card, int memory_video_card, int bit, string cpu, int ram) {
        this->os = os;
        this->disk_type = disk_type;
        this->memory_disk = memory_disk;
        this->name_video_card = name_video_card;
        this->memory_video_card = memory_video_card;
        this->bit = bit;
        this->cpu = cpu;
        this->ram = ram;
    }

    void DisplayInfo() {
        cout << "Scaning System..." << endl;
        this_thread::sleep_for(chrono::seconds(3));
        system("cls");
        this_thread::sleep_for(chrono::seconds(3));
        cout << "Operating System Info: " << os << endl;
        cout << "Disk Info: " << disk_type << " - " << memory_disk << "Gb" << endl;
        cout << "Video Card Info: " << name_video_card << " - " << memory_video_card << "Gb" << endl;
        cout << "System Capacity Info: " << "x" << "64" << endl;
        cout << "CPU Info: " << cpu << endl;
        cout << "Random Access Memory Info: " << ram << endl;
    }

    void StartingOS() {
        cout << endl;
        cout << "Starting System..." << endl;
        this_thread::sleep_for(chrono::seconds(4));
        system("cls");
        system("\"C:\\Users\\Admin\\Desktop\\MOSIF Enterprise\\ConsoleOS.exe\"");
    }
};

int main() {
    setlocale(LC_ALL, "RU");

    ArchitectureSystemInfo architecturesysteminfo("M.O.S.I.F", "SSD", 1000, "NVIDIA Geforce", 2, 64, "Intel Core i9", 12);
    architecturesysteminfo.DisplayInfo();
    architecturesysteminfo.StartingOS();

    return 0;
}