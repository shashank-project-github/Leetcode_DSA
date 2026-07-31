class Solution(object):
    def getIntersectionNode(self, headA, headB):


        point1 = headA
        point2 = headB

        while point1 != point2:
            if point1:
                point1 = point1.next
            else:
                point1 = headB

            if point2:
                point2 = point2.next
            else:
                point2 = headA

        return point1