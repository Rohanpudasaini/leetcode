#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        largest = -1
        second_largest = -1
        
        for i in range(len(arr)):
            if arr[i] > largest:
                second_largest = largest
                largest = arr[i]
            
            elif arr[i] < largest and arr[i] > second_largest:
                second_largest = arr[i]
        return second_largest

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends