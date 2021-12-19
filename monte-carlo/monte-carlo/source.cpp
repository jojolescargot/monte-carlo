#include <iostream>
#include <random>
#include <iomanip>

std::random_device rd{};

std::default_random_engine eng(rd());
std::uniform_real_distribution<float> distribution(0, 1);

int main()
{	
	std::cout << "Starting programm\n";
	long in=0, iterations = 1e7;
	
	
	#pragma omp parallel
	{
		#pragma omp for reduction(+ : in)
		for (int i = 0; i < iterations; i++)
		{
			float x = distribution(eng);
			float y = distribution(eng);

			if (x * x + y * y <= 1)
			{
				in += 1;
			}
		}

	}

	std::cout << std::setprecision (10) << "Approximation of pi : " << (double)in / (double)iterations * 4.;
}