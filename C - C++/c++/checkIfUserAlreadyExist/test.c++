#include <iostream>
#include <fstream>
#include <string>
#include <string.h>

using namespace std;


int main () {

   ifstream userData;
   userData.open("testFolder/data.csv");

   string username = "juanamaria";


   bool nameExist=false;
   int raw=0;
   while (userData.good() && nameExist == false)
   {
      string line;
      getline(userData,line,'\n');

      if (raw == 0){ // filter first line
         raw++;
         continue;
      }

      int pos = line.find(';');
      string name = line.substr(0,pos);

      if (name == username)
         nameExist = true;

   }

   cout << "User found: "<<nameExist;
   
   userData.close();
 return 0;
}