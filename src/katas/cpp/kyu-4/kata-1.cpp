#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <cmath>
#include <algorithm>
#include <sstream>

class SumOfDivided
{
public:
    static std::string sumOfDivided(std::vector<int> &lst)
    {
        std::unordered_map<int, int> prime_sums;

        for (int num : lst)
        {
            int n = std::abs(num);
            std::unordered_set<int> factors;

            // Check divisibility by 2
            while (n % 2 == 0)
            {
                factors.insert(2);
                n = n / 2;
            }

            // Check divisibility by odd numbers starting from 3
            for (int i = 3; i <= std::sqrt(n); i += 2)
            {
                while (n % i == 0)
                {
                    factors.insert(i);
                    n = n / i;
                }
            }

            // If n is a prime number greater than 2
            if (n > 2)
            {
                factors.insert(n);
            }

            // Update the sum for each prime factor
            for (int factor : factors)
            {
                prime_sums[factor] += num;
            }
        }

        // Sort the primes
        std::vector<int> primes;
        for (auto &entry : prime_sums)
        {
            primes.push_back(entry.first);
        }
        std::sort(primes.begin(), primes.end());

        // Create the result string
        std::ostringstream result;
        for (int prime : primes)
        {
            result << "(" << prime << " " << prime_sums[prime] << ")";
        }

        return result.str();
    }
};