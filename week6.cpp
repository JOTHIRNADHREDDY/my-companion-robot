#include "calculator.h"
#include "iostream"

int main ()
{
    int a,b,choice;
    std::cout << "Enter two integers: ";
    std::cout << "1)Addition\n2)Subtraction\n3)Multiplication\n4)Division\n";
    std::cout << "Enter your choice: ";
    std::cin >> choice;
    std::cin >> a >> b;
    switch(choice)
    {
        case 1:
            std::cout << "Result: " << add(a,b);
            break;
        case 2:
            std::cout << "Result: " << subtract(a,b);
            break;
        case 3:
            std::cout << "Result: " << multiply(a,b);
            break;
        case 4:
            std::cout << "Result: " << divide(a,b);
            break;
        default:
            std::cout << "Invalid choice!";
    }
    return 0;
}