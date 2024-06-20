#include <iostream>
#include <cstdlib>
#include <ctime>
#include <sstream>
#include <fstream>

using namespace std;

int main(){
    srand(time(0));
    stringstream ss;
    ofstream file("testset.csv");
    
    for(int i = -100000; i < 100000; i++){
        int random_value = ((i < 0)? -1 : 1) *(rand() % 1000000);
        ss << random_value << "," << abs(random_value % 2) << endl;
    }

    file << ss.str();
    file.close();
}