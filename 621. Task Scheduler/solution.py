# Input: tasks = ["A","A","A","B","B","B"], n = 2
#2+
# Output: 8

# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

# After completing task A, you must wait two cycles before doing A again. 
# The same applies to task B. In the 3rd interval, neither A nor B can be done,
# so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.


#Psudo

# MAIN GOAL: ​Return the minimum number of intervals required to complete all tasks.
# Input , and cooling time 
# Output, the minimum time required to execute all tasks
# The tasks are represented by a string array, and each task represents a different task. Each task can be done in one unit of time.
# The cooling interval is between two same tasks.
# Cooling time is 2 in this case
# ["A","A","A","B","B","B"]
# A -> A -> A -> B -> B -> B == Task A -> Forced Idle(2) -> Task A -> Forced Idle(2) -> Task A -> Task B -> Forced Idle(2) -> Task B -> Forced Idle(2) -> Task B
# 2+2+2+2 = 8 

from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_frequency = max(task_counts.values())
        max_count = list(task_counts.values()).count(max_frequency)
        min_time = max((max_frequency - 1) * (n + 1) + max_count, len(tasks))
        
        return min_time

solution = Solution()
