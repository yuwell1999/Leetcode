import numpy as np


class Solution:
    # @staticmethod
    # def calcStep(a[],b[]):
    #     #min = min(np.abs(x-a),np.abs(y-b))
    #     return max = max(np.abs(a[0]-b[0]),np.abs(a[1]-b[1]))

    def minTimeToVisitAllPoints(self, points):
        time = 0
        for i in range(0, len(points) - 1):
            time += max(np.abs(points[i][0] - points[i + 1][0]), np.abs(points[i][1] - points[i + 1][1]))
        return time
