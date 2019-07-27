print('******** Welcome To The World Of CLASSES ********')
class abc:
    a=100
    def __init__(self):
        print("Hii..Deepesh")

    def abc(self,c):
        self.b=200
        self.d = self.a + c
        print("Hello World",self.b,self.a,self.d)

    def xyz(self):
        print('hii',self.b,self.a,self.d)

a = abc()
a.abc(300)
a.xyz()



