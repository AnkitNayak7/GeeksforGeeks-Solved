#User function Template for python3

class Solution:
    def countSquares(self, N):
        if N <= 1:
            return 0
    
        sqrt_N = int(N**0.5)

        if sqrt_N*sqrt_N==N:
            return sqrt_N-1
        else:
            return sqrt_N


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.countSquares(N))
# } Driver Code Ends