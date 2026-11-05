class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count=0
        for i in arr1:
            temp=0
            for j in arr2:
                if abs(i-j)<=d:
                    temp=1
                    break
            if temp==0:
                count+=1
        return count