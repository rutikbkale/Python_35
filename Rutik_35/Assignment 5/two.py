# Define a class Batsman with following function.

class Batsman:
    def __init__(self, bcode, bname, innings, notout, runs):
        self.bcode = bcode
        self.bname = bname
        self.innings = innings
        self.notout = notout
        self.runs = runs

    def calAvg(self):
        avg = self.runs/(self.innings-self.notout)
        return avg
    
    def displayData(self):
        print("Batsman code : ",self.bcode)
        print("Batsman name : ",self.bname)
        print("Batsman Total Innings : ",self.innings)
        print("Batsman Notout Innings : ",self.notout)
        print("Batsman Total runs : ",self.runs)
        print("Batsman Batting Average : ",self.calAvg())

bcode = int(input("Enter the batsman code : "))
bname = input("Enter the batsman name : ")
innings = int(input("Enter the batsman innings : "))
notout = int(input("Enter the batsman notout innings : "))
runs = int(input("Enter the batsman total runs : "))

obj = Batsman(bcode, bname, innings, notout, runs)
obj.displayData()