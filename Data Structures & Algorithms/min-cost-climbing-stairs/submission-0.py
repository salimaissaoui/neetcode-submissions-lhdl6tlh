class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        i = 0
        j = 1
        res1 = 0
        res2 = 0

        while i < len(cost):
            if i+2 < len(cost) and cost[i+1] < cost[i+2]  :
                res1+= cost[i]
                i += 1
                
            
            else:
                res1+= cost[i]
                i+=2
                
        

        while j < len(cost):
            if j+2 < len(cost) and cost[j+1] < cost[j+2] :
                res2+= cost[j]
                j += 1
                
            
            else:
                res2+= cost[j]
                j+=2
        
        return min(res1, res2)
                


        