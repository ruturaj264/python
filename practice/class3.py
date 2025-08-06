class number():

    def __init__(self, num):
        if type(num) == type(1) or (type(num) == type('1') and num.isnumeric()):
            print('Valid Number')
            self.value = int(num)
        else:
            print('Invalid Number')

    def sqaure(self):
        return self.value ** 2
    
    def cube(self):
        return self.value ** 3
    
    def factorial(self):

        fact = 1
        for i in range(1,self.value+1):
            fact *= i

        return fact
    
    def __str__(self):
        return str(self.value)
    
    def __len__(self):
        return(len(str(self.value)))
    

mynum = number('7')

# print(mynum.cube())

class Array():

    def __init__(self, *args):
        self.entities = list(args)

    def opposite(self):

        temp = []
        for entity in self.entities:
            temp.insert(0,entity)

        self.entities = temp

    def minus(self, *args):

        for item in args:
            if item in self.entities:
                self.entities.remove(item)

    def __str__(self):
        return str(self.entities)
    
    def __len__(self):
        return len(self.entities)
    
a = Array(1,True,2,'a',3,'b')

a.opposite()
a.minus('a','b',8)
print(a)



