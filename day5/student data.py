class ece:
    def section1(self,name,rollno):
        self.name=name
        self.rollno=rollno
        print(name,rollno)
    def section2(self,n,age,rollno):
        self.n=n
        self.age=age
        self.rollno=rollno
        print(n,age,rollno)
obj=ece()
obj.section1("klin kara","34")
obj.section2("ayaan",89,1)
