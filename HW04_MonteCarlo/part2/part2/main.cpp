//
//  main.cpp
//  part2
//
//  Created by William Gillespie on 12/3/16.
//  Copyright © 2016 William Gillespie. All rights reserved.
//

#include <iostream>
#include <math.h>

double randomInRange(double min, double max) {
    double range = max - min;
    double random = rand();
    return range * (random / (double) RAND_MAX) + min;
}

bool isInCircle1(double x, double y) {
    //x^2+y^2=6^2
    double radiusSquared = 36;
    double distanceSquared = pow(x, 2) + pow(y, 2);
    return distanceSquared < radiusSquared ? true : false;
}

bool isInCircle2(double x, double y) {
    //(x-3)^2 + (y-3)^2 = 4^2
    double radiusSquared = 16;
    double distanceSquared = pow(x - 3, 2) + pow(y - 3, 2);
    return distanceSquared < radiusSquared ? true : false;
}

bool isUnderLine1(double x, double y) {
    //y = -2x + 7
    double threshold = -2 * x + 7;
    return y < threshold ? true : false;
}

struct BoundingBox {
    double x_min, x_max, y_min, y_max;
};

int main(int argc, const char * argv[]) {
    srand(time(NULL));
    
    BoundingBox box;
    box.x_min = -1; box.x_max = 3.944; box.y_min = -1; box.y_max = 5.99;
    
    int total = 0;
    int inIntersection = 0;
    
    int ITERATIONS = 1000000;
    
    for (int i = 0; i < ITERATIONS; i++) {
        double random_x = randomInRange(box.x_min, box.x_max);
        double random_y = randomInRange(box.y_min, box.y_max);
        
        bool isInIntersection = isInCircle1(random_x, random_y) &&
                                isInCircle2(random_x, random_y) &&
                                isUnderLine1(random_x, random_y);
        if (isInIntersection) {
            inIntersection++;
        }
        total++;
    }
    
    double ratio = (double) inIntersection / (double) total;
    std::cout << "ratio: " << ratio << "\n";
    
    double area = ratio * (box.x_max - box.x_min) * (box.y_max - box.y_min);
    std::cout << "area: " << area << "\n";

    /*
    if (isInIntersection) {
        std::cout << "x: " << random_x << ", y: " << random_y << " is in intersection\n";
    } else {
        std::cout << "x: " << random_x << ", y: " << random_y << " is not in intersection\n";
    }
     */
    return 0;
}
