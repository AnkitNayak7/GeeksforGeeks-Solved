#User function Template for python3

# TC = O(n log log n) and SC=O(n)
class Solution:
    def isPrime (self,  n):
        prime_flag = 1
        if n<=1:
            return 0
        
        if n >1:
            for i in range(2, int(n**0.5) + 1):
                if n%i==0:
                    prime_flag = 0
                    break
        return prime_flag
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isPrime(N))
# } Driver Code Ends