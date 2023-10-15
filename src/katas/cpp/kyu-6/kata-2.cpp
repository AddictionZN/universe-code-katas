#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

class Stat
{
public:
    static std::string format_time(int seconds)
    {
        int hh = seconds / 3600;
        int mm = (seconds % 3600) / 60;
        int ss = seconds % 60;
        std::stringstream ss_time;
        ss_time << (hh < 10 ? "0" : "") << hh << "|"
                << (mm < 10 ? "0" : "") << mm << "|"
                << (ss < 10 ? "0" : "") << ss;
        return ss_time.str();
    }

    static std::string stat(const std::string &times)
    {
        if (times.empty())
            return "";

        std::stringstream ss(times);
        std::string token;
        std::vector<int> all_times;

        while (getline(ss, token, ','))
        {
            int hh, mm, ss;
            sscanf(token.c_str(), "%d|%d|%d", &hh, &mm, &ss);
            all_times.push_back(hh * 3600 + mm * 60 + ss);
        }

        std::sort(all_times.begin(), all_times.end());

        int range = all_times.back() - all_times.front();

        int total_time = 0;
        for (int time : all_times)
        {
            total_time += time;
        }
        int mean = total_time / all_times.size();

        int median;
        int n = all_times.size();
        if (n % 2 == 1)
        {
            median = all_times[n / 2];
        }
        else
        {
            median = (all_times[n / 2 - 1] + all_times[n / 2]) / 2;
        }

        return "Range: " + format_time(range) + " Average: " + format_time(mean) + " Median: " + format_time(median);
    }
};