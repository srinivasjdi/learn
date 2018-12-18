/*******************************
 * author : 
 * date : 
 * description : 
 * 
 * 
 * 
 ******************************/

#include <iostream>

extern int x;

int main(){
    
    int favourite_number ;
    std::cout << "hello ! enter number :";
    std::cin >> favourite_number;
    std::cout << "your favourite number is :" << favourite_number << std::endl;
    std::cout << x;
    return 0;
}

