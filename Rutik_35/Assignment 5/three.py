# Define a class test with following attributes.

class Test: 
    def __init__(self, testCode, desc, noCand):
        self.testCode = testCode
        self.desc = desc
        self.noCand = noCand

    def calCenter(self):
        noCenter = (self.noCand/100)+1
        return noCenter
    
    def dispTest(self):
        print("Test code is : ", self.testCode)
        print("Test description is : ", self.desc)
        print("Number of candidates is : ", self.noCand)
        print("Number of required centers is : ", self.calCenter())

testCode = int(input("Enter the test code : "))
desc = input("Enter the test description : ")
noCand = int(input("Enter the number of candidates : "))

obj = Test(testCode, desc, noCand)
obj.dispTest()