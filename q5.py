def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    
    merged_intervals = []
    
    for interval in intervals:
        
        if not merged_intervals or interval[0] > merged_intervals[-1][1]:
            merged_intervals.append(interval)
        else:
            merged_intervals[-1] = (merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1]))
    
    return merged_intervals

intervals_str = input("Enter the intervals separated by commas: ").strip()
intervals = list(map(lambda x: tuple(map(int, x.strip("()").split(","))), intervals_str.split()))

result = merge_intervals(intervals)
print("Merged intervals:")
for interval in result:
    print(interval)