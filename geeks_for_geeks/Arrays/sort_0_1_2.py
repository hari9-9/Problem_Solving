#{
 # Driver Code Starts

# } Driver Code Ends
class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        val = [0,0,0]
        for i in arr:
            val[i]+=1
        for i in range(len(arr)):
            if val[0]:
                arr[i] = 0
                val[0]-=1
            elif val[1]:
                arr[i] = 1
                val[1]-=1
            else:
                arr[i] = 2




#{
 # Driver Code Starts.
def main():
    t = int(input().strip())  # Read the number of test cases
    ob = Solution()

    while t > 0:
        t -= 1
        arr = list(map(int,
                       input().strip().split())
                   )  # Read the array as space-separated integers
        ob.sort012(arr)  # Sort the array

        print(' '.join(map(str, arr)))  # Print the sorted array
        print("~")

if __name__ == "__main__":
    main()

# } Driver Code Ends
