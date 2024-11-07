import math
import os
import random
import re
import sys

class Solution:
    def breakingRecords(self, scores):
        l = len(scores)
        minimum = scores[0]
        maximum = scores[0]
        minCount = 0
        maxCount = 0
        for i in range (1, l):
            if scores[i] > maximum:
                maximum = scores[i]
                maxCount += 1
            elif scores[i] < minimum:
                minimum = scores[i]
                minCount += 1
        return [maxCount, minCount]

test1 = Solution()
print(test1.breakingRecords([10,5,20,20,4,5,2,25,1]))