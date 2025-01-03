class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        near_xaxis = max(x1, min(x2, xCenter))
        near_yaxis = max(y1, min(y2, yCenter))

        distx = near_xaxis - xCenter
        disty = near_yaxis - yCenter

        if(distx ** 2 + disty ** 2 <= radius ** 2):
            return True
        else: 
            return False
        