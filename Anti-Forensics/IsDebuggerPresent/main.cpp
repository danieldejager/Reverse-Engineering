#include <iostream>
#include <windows.h>

using namespace std;

int main()
{
    if(IsDebuggerPresent())
    {
        std::cout << "Debugger was detected" << endl;
    }
    else
    {
        std::cout << "Nothing to worry about" << endl;
    }
    std::cin.get();
    return 0;
}
