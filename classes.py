# class
class myClass:
    def __init__(self,nums):
        #create member variables
        self.mums = nums
        self.size = len(nums)

        # self key word required as a param
        def getLength(self):
            return self.size
        
        def getDoubleLength(self):
            return 2 * self.getLength()

        