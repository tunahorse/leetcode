#Make a class Solution
class Solution: 
    #Create function to find minimum number of arrows needed to burst all balloons
    #Sort the points based on their ending x-coordinate (x_end)
    #Initialize the count of arrows needed to 1 because we'll shoot at least one arrow
    
    def findMinArrowShots(self, points):
        # If the input list is empty, return 0 as no arrows are needed
        if not points:
            return 0

        # Sort the points based on their ending x-coordinate (x_end)
        points.sort(key=lambda x: x[1])
    

        # Initialize the count of arrows needed to 1 because we'll shoot at least one arrow
        # and set 'first_end' to the end x-coordinate of the first balloon in the sorted list
        arrows = 1
        first_end = points[0][1]

        # Iterate through each balloon in the sorted list
        for x_start, x_end in points:
            # If the current balloon's start x-coordinate is greater than 'first_end',
            # it means the current arrow cannot burst this balloon, so we need to shoot a new arrow
            if x_start > first_end:
                arrows += 1  # Increment the arrow count as we need a new arrow
                first_end = x_end  # Update 'first_end' to the end x-coordinate of the current balloon

        # After iterating through all balloons, return the total number of arrows needed
        return arrows

# Example usage of the Solution class and its findMinArrowShots method:
solution = Solution()
points1 = [[10,16],[2,8],[1,6],[7,12]]
print(solution.findMinArrowShots(points1))  # Expected output: 2
