# Week 10: (Lab Day) Practice with Classes and Objects

"""
PROBLEM 1: Design Parking System

https://leetcode.com/problems/design-parking-system/description

"""
#my solution:

class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.big = big
        self.medium = medium
        self.small = small
        

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if carType == 1:
            if self.big >= 1:
                self.big -= 1
                return True
            else:
                return False
        elif carType == 2:
            if self.medium >= 1:
                self.medium -= 1
                return True
            else:
                return False
        elif carType == 3:
            if self.small >= 1:
                self.small -= 1
                return True
            else:
                return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

#optimized solution
class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.parking_lot = {1: big, 2: medium, 3: small}       

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if self.parking_lot[carType] > 0:
            self.parking_lot[carType] -= 1
            return True
        else:
            return False


"""
PROBLEM 2: Design a Stack With Increment Operation

https://leetcode.com/problems/design-a-stack-with-increment-operation/description/ 

"""
class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.stack = []
        self.max_Size = maxSize        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) < self.max_Size:
            self.stack.append(x)


    def pop(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack.pop()
        else:
            return -1
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        max_increment = 0
        if len(self.stack) < k:
            max_increment = len(self.stack)
        else: max_increment = k

        for i in range(max_increment):
                self.stack[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)