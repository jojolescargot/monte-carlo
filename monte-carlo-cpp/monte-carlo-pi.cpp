#include <iostream>
#include <random>


int main()
{

    std::random_device rd{};

    std::default_random_engine gen(rd());
    std::uniform_real_distribution<float> distribution(0,1);

    std::cout << "Random : " << distribution(gen);
}