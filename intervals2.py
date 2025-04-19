def insert(intervals, new_interval):
        n = len(intervals)
        i = 0
        new_arr = []

        while i < n and intervals[i][1] <= new_interval[0]:
                new_arr.append(intervals[i])
                i+=1

        while i < n and intervals[i][0] < new_interval[1]:
                new_interval[0] = min(intervals[i][0], new_interval[0])
                new_interval[1] = max(intervals[i][1], new_interval[1])
                i+=1
        new_arr.append(new_interval)

        while i < n:
                new_arr.append(intervals[i])
                i+=1

        return new_arr




Intervals = [[1,3],[6,9]]
newInterval = [2,5]

print(insert(Intervals, newInterval))
