class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            count = 0
            gt = False
            for j in range(i,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    gt = True
                    break
                else:
                    count+=1
            if not gt:
                res.append(0)
            else:
                res.append(count)
        
        return res


         

        