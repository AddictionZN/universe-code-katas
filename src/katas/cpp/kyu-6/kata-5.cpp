#include <vector>
#include <algorithm>
#include <iostream>

int FindOutlier(const std::vector<int> &arr)
{
    int oddCount = 0, evenCount = 0;
    int oddOutlier = 0, evenOutlier = 0;

    // Count odd and even numbers in the first few elements
    for (int i = 0; i < std::min(3, static_cast<int>(arr.size())); ++i)
    {
        if (arr[i] % 2 == 0)
        {
            evenCount++;
            evenOutlier = arr[i];
        }
        else
        {
            oddCount++;
            oddOutlier = arr[i];
        }
    }

    // Find the outlier based on the counts
    if (oddCount > evenCount)
    {
        // The array is primarily odd, so the outlier is even
        return *std::find_if(arr.begin(), arr.end(), [](int n)
                             { return n % 2 == 0; });
    }
    else
    {
        // The array is primarily even, so the outlier is odd
        return *std::find_if(arr.begin(), arr.end(), [](int n)
                             { return n % 2 != 0; });
    }
}
