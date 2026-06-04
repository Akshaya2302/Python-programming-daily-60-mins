class rectange:
    def __init__(self,l,b):
        self.l=l
        self.b=b
        
    def area(self):
        return self.l*self.b
    
    def perimeter(self):
        return 2*(self.l+self.b)
        
class time:
    def __init__(self,h,m):
        self.h=h
        self.m=m
        
    def add(self,other):
        total_m=self.m+other.m
        total_h=self.h+other.h+total_m//60
        total_m=total_m%60
        return time(total_h,total_m)
        
    def display(self):
        print(self.h,"hours",self.m,"Minutes")
        
        
r=rectange(5,3)

print("Area:",r.area())
print("Perimeter",r.perimeter())

t1=time(5,45)
t2=time(3,50)

t3=(t1.add(t2))

t3.display()