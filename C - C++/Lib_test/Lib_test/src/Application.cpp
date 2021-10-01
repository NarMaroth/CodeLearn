#include "Lib.h"

int main() 
{
	LibNS::printMessage();
}

// set main project as project->properties->Config.Properties->General->Config.Type->Application
// set lib project as project->properties->Config.Properties->General->Config.Type->Static Lib

// add in main project Lib Src Directory to project->properties->c/c++->General->Additional Includes Directories->$(SolutionDir)LibProjectSrcDir

// Link Lib Project doing main project->Add->Reference->Lib