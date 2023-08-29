class Employee: #base class
    def __init__(self,name):
        print("constructor is called")
        self.name=name

    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
            return i
    def __str__(self):
       return (f"str :  {self.name}")
    def __repr__(self):
        return (f"repr :  {self.name}")
    def __call__(self):
        return  (f"caller :  {self.name}")


class emp2(Employee):
   pass

obj=emp2("sonu")
print(obj.name)