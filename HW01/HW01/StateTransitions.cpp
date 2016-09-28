//
//  main.cpp
//  HW01
//
//  Created by William Gillespie on 9/27/16.
//  Copyright © 2016 William Gillespie. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string.h>
#include <unordered_map>


int main(int argc, const char * argv[]) {
    
    std::unordered_map<std::string, std::string> myMap;
    myMap["A0"] = "B";
    myMap["A1"] = "A";
    myMap["B0"] = "C";
    myMap["B1"] = "B";
    myMap["C0"] = "A";
    myMap["C1"] = "D";
    
    std::string test = "001";
    std::string current_state = "A";
    std::string final_state = "D";
    
    for (int i = 0; i < test.length(); i++) {
        std::string s = test.substr(i, 1);
        
        std::string key = s + current_state;
        std::cout << key << "\n";
    }
    
    return 0;
}














