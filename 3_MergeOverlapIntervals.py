def merge_overlapping_intervals(intervals):
  intervals.sort()
  for interval in reversed(intervals):
    for interval2 in reversed(intervals):
      if interval == interval2:
        continue
      if (interval[0] <= interval2[0] and  interval[1] >= interval2[0]):
        if interval2[1] <= interval[1]:
          intervals.remove(interval2)
        else:
          interval[1] = interval2[1]
          intervals.remove(interval2)
  return intervals
merge_overlapping_intervals([[1,15],[5,25],[15,40],[20,50],[55,60]])