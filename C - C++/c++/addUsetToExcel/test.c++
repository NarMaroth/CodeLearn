#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main () {
   ifstream userData;
   userData.open("data.csv");

   string username = "alberto",password = "123";
   bool userfound=false, correctPassword=false;

   int raw=0;
   while (userData.good() && userfound == false)
   {
      string line;
      getline(userData,line,'\n');

      if (raw == 0){
         raw++;
         continue;
      }

      string name = "";
      string pass = "";
      int i=0;
      while (i<line.length())
      {
         if( line[i] != ';')
            if (userfound == false)
               name += line[i];
            else
               pass += line[i];
         else{
            if(userfound == false){
               if (name == username)
                  userfound = true;
               else
                  break;
            }
         }

         if(i==line.length()-1)
            if(pass == password)
               correctPassword = true;
         i++;
      }
   }

   cout << "Userfound: " << userfound <<endl;
   if (userfound)
      cout << "Password is correct: " << correctPassword;
 return 0;
}