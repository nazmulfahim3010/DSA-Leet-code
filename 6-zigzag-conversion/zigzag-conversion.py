class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows==1 or numRows>len(s):
            return s
        # n number of string for n row 

        data=[""]*numRows
        counter = 0
        direction=1
        result=""
        
        for alpha in s:
            data[counter] += alpha
            # counter direction set

            if counter == numRows - 1:
                direction = -1
            elif counter == 0:
                direction = 1
            counter += direction
        # parts concatanation

        for part in data:
            result+=part

        return result



        