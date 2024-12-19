class branch:
    def __init__(self,branch,sec,year,name):
        self.branch=branch
        self.sec=sec
        self.year=year
        self.name=name
        self.age=19
    def print(self):
        print(self.name,self.branch,self.year,self.sec)
    def compare(self,other):
        if self.year==other.year:
            print("same year")
        else:
            print("not same year")
rakshi=branch("cse","d","E2","rakshi")
sri=branch("ECE","b","E2","sri")
rakshi.print()
sri.print()
print(id(rakshi))
print(sri.age)
sri.year="E3"
rakshi.compare(sri)