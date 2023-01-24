class Shark:

    def __init__(self,name= None):
        self.followers = []

    def listing(self, list):
        self.followers = list

    def print(self):
        dict ={}
        for i in range(len(self.followers)):
            print(self.followers)


    def __del__(self):
        print("Destructor called")


new_shark = Shark()
new_shark.listing([1,2,3,1,5,62])
new_shark.print()