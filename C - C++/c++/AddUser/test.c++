#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main () {
   string username = "anamaria",password = "123";
   string newUser = username+";"+password;

   ifstream userData;
   userData.open("data.csv");
   
   string currentData;
   while (userData.good())
   {
      string newLine;
      getline(userData,newLine);
      if (newLine != "")
         currentData += newLine+"\n";
   }
   userData.close();

   currentData += newUser;

   ofstream updateData;
   updateData.open("data.csv");

   updateData << currentData <<endl;

   updateData.close();
 return 0;
}