#User function Template for python3

class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, l = None):
        if l == None:
            l = len(arr)
        if l <= 1:
            return
        for i in range(l-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        self.bubbleSort(arr, l-1)
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):

        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends