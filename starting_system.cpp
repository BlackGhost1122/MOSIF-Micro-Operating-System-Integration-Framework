#include <iostream>
#include <windows.h>
#include <cstdlib>
#include <chrono>
#include <thread>

using namespace std;


int main() 
{
    const char* exePath = "C:\\Users\\Admin\\Desktop\\MOSIF_Enterprise\\ConsoleOS.exe";

    int result = system(exePath);

    if (result == 0) {
        std::cout << "The files were successfully uploaded" << std::endl;
        return 0;
    } else {
        std::cout << "Error! System file not found" << std::endl;
        return 1;
    }
}