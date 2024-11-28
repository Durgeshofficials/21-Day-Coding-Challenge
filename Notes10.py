'''
Problem statement

You have been given an array ‘a’ of ‘n’ unique non-negative integers.
Find the second largest and second smallest element from the array.
Return the two elements (second largest and second smallest) as another array of size 2.

Example :
Input: ‘n’ = 5, ‘a’ = [1, 2, 3, 4, 5]
Output: [4, 2]
The second largest element after 5 is 4, and the second smallest element after 1 is 2.
'''
def getSecondOrderElements(n,a):
    # Write your code here.
    a.sort()
    
    second_largest = a[-2]
    second_smallest = a[1]

    return [second_largest,second_smallest]

n = 5 
a =[1,2,3,4,5]
print(getSecondOrderElements(n,a))