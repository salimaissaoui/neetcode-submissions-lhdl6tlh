class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        resul = 0
        for num in tokens:
            if num == "+":
                a = res.pop()
                b = res.pop()
                resul = a + b
                res.append(resul)
            
            elif num == "-":
                a = res.pop()
                b = res.pop()
                resul = b - a
                res.append(resul)
            
            elif num == "*":
                a = res.pop()
                b = res.pop()
                resul = a * b
                res.append(resul)
            
            elif num == "/":
                a = res.pop()
                b = res.pop()
                if b != 0:
                    resul = int(b/a)
                res.append(resul)
            
            else:
                res.append(int(num))
        
        if len(tokens) == 1:
            resul = int(tokens[0])
        return resul
            

        