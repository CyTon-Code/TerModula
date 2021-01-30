#include <cmath>
#include <iostream>
#include <fstream>
using namespace std;
char hi[80] = "[root ~]$ ";

int len(char List[]){
    int i = 0;
    for(;List[i]!='\0';i++);
    return i;
}
int main(void)
{
    //~ char command[80];
    //~ command[0] = '\0';
    //~ for(;;)
    //~ {
        //~ cout << hi << command;
        //~ char tmp = 'a';
        //~ s tp = 'a';
        //~ for (int j = 0; j < 80 && tmp != ' '; j++)
        //~ {
            //~ cin.getline(tmp, 1);

            //~ if (len(command)+1 < 80){
                //~ command[len(command)] = tmp;
                //~ command[len(command) + 1] = '\0';
            //~ }
            //~ cout << command << ' ';
     //       //~ for (int i = 0; i < len(command); i++)
   //         //~ command = (command + tmp);
        //~ }
        //~ cin >> command;
    //~ }
    //~ system(s);
    return 0;
}
//~ g++     Terminal_v1.cpp  -S -o Terminal_v1
//~ g++     Terminal_v1.cpp  -S -o Terminal_v1.s
