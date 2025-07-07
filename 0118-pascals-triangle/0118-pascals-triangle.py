class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            if i == 0:
                result.append([1])
            elif i == 1:
                result.append([1,1])
            else:
                result.append(self.get_next_list(result[-1]))
        return result
    
    def get_next_list(self,previous:List[int])->List[int]:
        for i in range(len(previous)+1):
            if i == 0:
                new_result = [1]
            elif i == len(previous):
                new_result.append(1)
            else:
                new_result.append(previous[i]+ previous[i-1])
        return new_result
            


        