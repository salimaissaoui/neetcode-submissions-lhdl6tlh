class Solution:
    def trap(self, height: List[int]) -> int:
        l_wall = 0
        r_wall = 0
        n = len(height)
        Lmax = [0] * n
        Rmax = [0] * n
        for i in range(n):
            j = -i -1
            Lmax[i] = l_wall
            Rmax[j] = r_wall
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])
        
        res = 0
        pot = 0
        for i in range(n):
            pot = min(Lmax[i], Rmax[i]) 
            res += max(0, pot - height[i])
        
        return res



            

