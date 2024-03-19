You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

​Return the minimum number of intervals required to complete all tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

#Psudo

# MAIN GOAL: ​Return the minimum number of intervals required to complete all tasks.
# Input , and cooling time 
# Output, the minimum time required to execute all tasks
# The tasks are represented by a string array, and each task represents a different task. Each task can be done in one unit of time.
# The cooling interval is between two same tasks.
# Cooling time is 2 in this case
# ["A","A","A","B","B","B"]
# A -> A -> A -> B -> B -> B == Task A -> Forced Idle(2) -> Task A -> Forced Idle(2) -> Task A -> Forced Idle(2) -> Task B -> Forced Idle(2) -> Task B -> Forced Idle(2) -> Task B
# 2+2+2+2 = 8 