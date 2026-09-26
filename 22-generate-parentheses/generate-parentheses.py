class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        result,sol=[],[]

        def backtrack(openn,closee):
            if openn==n and closee==n:
                result.append("".join(sol))
                return

            if openn < n:
                sol.append("(")
                backtrack(openn+1,closee)
                
                sol.pop()

            if openn > closee:
                sol.append(")")
                backtrack(openn,closee+1)
                
                sol.pop()



        backtrack(0,0)
        return result



        
        