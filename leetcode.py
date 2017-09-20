class Solution:
    #1.Two Sum
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    print([i,j])
                    
    def twoSum2(self, nums, target):
        dict={}
        for idx1,n1 in enumerate(nums):
            dict[n1]= idx1
            n2= target-n1
            if n2 in dict:
                print(sorted([idx1, dict[n2]]))
            
ans=Solution()
ans.twoSum(nums=[2,7,11,15], target=9)
ans.twoSum2(nums=[2,7,11,15], target=9)

#2. Add Two Numbers
def addTwoNumbers(l1, l2):
    n=max(len(l1), len(l2))
    a=[0]*(n-len(l1))+l1
    b=[0]*(n-len(l2))+l2
    add=0; sums=[0]*n
    for idx in range(1,n+1):
        sum= a[-idx]+b[-idx]+add
        if sum>=10:
            sum=sum-10
            add=1
        else: add=0
        sums[-idx]=sum
    if add==1:
        sums=[1]+sums
    print(sums)
 
addTwoNumbers(l1=[2,4,3],l2=[5,6,4])
addTwoNumbers(l1=[5,0,0], l2=[1,5,0,0])

#3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self,s):
        length=0
        for i in range(len(s)-1):
            for j in range(i+1,len(s)+1):
                #use set to eliminate multiplility and get unique alphabets in the string
                sset=set(s[i:j])
                if len(sset)!=(j-i): break
                elif length<(j-i):
                    char=s[i:j]
                    length=j-i
        print(char)
ans=Solution()
ans.lengthOfLongestSubstring('abcabcbb')
ans.lengthOfLongestSubstring("bbbbb")
ans.lengthOfLongestSubstring("pwwkew")

#4. Median of Two Sorted Arrays                
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums=nums1+nums2
        import numpy as np
        print(np.median(nums))

ans=Solution()
ans.findMedianSortedArrays([1,2],[3,4])

#5. Longest Palindromic Substring
class Solution:
    def isPalindromic(self,string):
        judge= 1
        n= round(len(string)/2)
        for i in range(n):
            if string[i]!=string[-(i+1)]:
                judge=0
        return judge
                
    def longest(self, s):
        length=0
        for i in range(len(s)-1):
            for j in range(i+1,len(s)+1):
                if self.isPalindromic(s[i:j])==1 and length<(j-i):
                    char=s[i:j]
                    length=j-i
        return char
    
ans=Solution()
ans.longest('babad')

#6. ZigZag Conversion
class Solution(object):
    def convert(self, s, numRows):
        n=len(s); c=0;
        re= ['']*numRows
        i=0;c=0;a=0
        while(c<n):
            if i==0: a=1
            re[i]=re[i]+s[c]
            c=c+1
            if i==numRows-1: a=-1 #reverse the index number when reaching the boundary
            i=i+a
        answer=''
        for i in range(len(re)): answer= answer+re[i]
        return(answer)
        
ans=Solution()
ans.convert("PAYPALISHIRING",3)

