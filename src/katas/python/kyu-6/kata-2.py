def stat(strg):
    if not strg:
        return ""
    
    # Parse input string into list of times in seconds
    times_in_seconds = []
    for time in strg.split(", "):
        h, m, s = map(int, time.split("|"))
        total_seconds = h * 3600 + m * 60 + s
        times_in_seconds.append(total_seconds)
        
    times_in_seconds.sort()
    
    # Calculate range, average, and median
    range_time = times_in_seconds[-1] - times_in_seconds[0]
    
    average_time = sum(times_in_seconds) // len(times_in_seconds)
    
    n = len(times_in_seconds)
    if n % 2 == 1:
        median_time = times_in_seconds[n // 2]
    else:
        median_time = (times_in_seconds[n // 2 - 1] + times_in_seconds[n // 2]) // 2
    
    # Convert times to "hh|mm|ss" format
    def format_time(time):
        h, remainder = divmod(time, 3600)
        m, s = divmod(remainder, 60)
        return f"{h:02}|{m:02}|{s:02}"
    
    return f"Range: {format_time(range_time)} Average: {format_time(average_time)} Median: {format_time(median_time)}"




# Test the function
print(stat("01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"))
