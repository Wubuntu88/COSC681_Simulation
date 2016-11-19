//
//  StateTransitions.cpp
//  HW01
//
//  Created by William Gillespie on 9/27/16.
//  Copyright © 2016 William Gillespie. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string.h>
#include <unordered_map>
/**
 Initializes the state transition table and return it as a map.
 map["A0"] = "B"; means that state A can take transition 0 to arrive at B.
 @return: an unordered map representing a state transition table.
 */
std::unordered_map<std::string, std::string> initMap() {
    std::unordered_map<std::string, std::string> myMap;
    myMap["A0"] = "B";
    myMap["A1"] = "A";
    myMap["B0"] = "C";
    myMap["B1"] = "B";
    myMap["C0"] = "A";
    myMap["C1"] = "D";
    
    return myMap;
}

bool isValidSequence(std::string sequence) {
    for (int i = 0; i < sequence.length(); i++) {
        bool isEqualTo0 = sequence.substr(i, 1).compare("0") == 0;
        bool isEqualTo1 = sequence.substr(i, 1).compare("1") == 0;
        bool b = isEqualTo0 || isEqualTo1;
        
        if (b == 0) {//if it is not equal to 0 or 1
            return false;
        }
    }
    return true;
}

bool acceptSequence(std::string sequence,
                    std::unordered_map<std::string, std::string> map) {
    if (isValidSequence(sequence) == false) {
        std::cout << "invalid sequence: " << sequence << "\n";
        return false;
    }
    /** -- start -- **/
    std::string path_trace =
                "Trace of Transitions for sequence: " + sequence + "\n";
    path_trace.append("A");
    std::string arrow = " -> ";
    std::string current_state = "A";
    std::string final_state = "D";
    
    for (int i = 0; i < sequence.length(); i++) {
        std::string key = current_state + sequence[i];
        std::string nextLocation = map[key];
        path_trace.append(arrow + nextLocation);
        
        current_state = nextLocation;
        if (current_state.compare(final_state) == 0) { // if they are equal
            std::cout << path_trace << "\n\n";
            return true;
        }
    }
    /*
     if we have gone throught the entire input string (of 0s and 1s) and
     have not arrived at D, then the path is not accepted becuase
     D is our final state.
    */
    std::cout << "for sequence: " << sequence << "\nUnable to reach the final state D; string not accepted.\n\n";
    return false;
}



int main(int argc, const char * argv[]) {
    
    std::unordered_map<std::string, std::string> myMap = initMap();
    
    std::string test1 = "001";
    acceptSequence(test1, myMap);
    
    std::string test2 = "110101";
    acceptSequence(test2, myMap);
    
    std::string test3 = "110";
    acceptSequence(test3, myMap);
    
    std::string test4 = "0000";
    acceptSequence(test4, myMap);
    
    return 0;
}














