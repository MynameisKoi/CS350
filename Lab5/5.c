#include <stdio.h>

int main() {
    int best_car = 0, correct_expert = 0;
    int car = 0, expert = 0;
    int a,b,c,d;
    // Expert A said: #2 is the best.
    a = (car == 2);

    // Expert B said: #4 is the best.
    b = (car == 4);

    // Expert C said: #3 is NOT the best.
    c = (car != 3);

    // Expert D said: Expert B is wrong.
    d = (expert != 2 && car != 4);

    // assume A true first, check if B C D all wrong
    a = 1;
    while (a != 0){
        car = 2;
        expert = 1;
        if (b) {a = 0;}
        else if (c) {a = 0;}
        else if (d) {a = 0;}
        else {
            best_car = car;
            correct_expert = expert;
            break;
        }
    }

    // assume B true first, check if A C D all wrong
    b = 1;
    while (b != 0){
        car = 4;
        expert = 2;
        if (a) {b = 0;}
        else if (c) {b = 0;}
        else if (d) {b = 0;}
        else {
            best_car = car;
            correct_expert = expert;
            break;
            }
    }

    // assume C true first, check if A B D all wrong
    c = 1;
    while (c != 0){
        // since A and B have to be wrong, best_car != {2,4}
        // C true, which means best_car != 3 => best_car = 1
        car = 1;
        expert = 3;
        if (a) {c = 0;}
        else if (b) {c = 0;}
        else if (d) {c = 0;}
        else {
            best_car = car;
            correct_expert = expert;
            break;
        }
    }

    // assume D true first, check if A B C all wrong
    d = 1;
    while (d != 0){
        // since A and B have to be wrong, best_car != {2,4}
        // C also has to be wrong, thus best_car = 3
        car = 3;
        expert = 4;
        if (a) {d = 0;}
        else if (b) {d = 0;}
        else if (c) {d = 0;}
        else {
            best_car = car;
            correct_expert = expert;
            break;
        }
    }

    // Print the result
    printf("The best car is #%d, and the correct expert is %c.\n", car, correct_expert + 'A' - 1);

    return 0;
}
