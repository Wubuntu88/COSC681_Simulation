//
//  main.cpp
//  HW01
//
//  Created by William Gillespie on 9/27/16.
//  Copyright © 2016 William Gillespie. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <unordered_map>
struct pair {
    int choice;
    std::string destination;
};
int main(int argc, const char * argv[]) {
    
    std::unordered_map<std::string, pair> myMap;
    pair p;
    p.choice = 0;
    p.destination = "b";
    myMap["a"] = p;
    std::cout << "a's choice: " << myMap["a"].choice << "\n";
    std::cout << "a's destination: " << myMap["a"].destination << "\n";
    return 0;
}
