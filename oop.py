

#multi inheritance 

class dad :
    
    def __init__(self, dad_name) :
        self.dad_name=dad_name

    def father(self):
        return self.dad_name


class mom :

    def __init__(self, mom_name) :
        self.mom_name=mom_name
    
    def mother(self):
        return self.mom_name


class child(dad,mom):

    def __init__(self, child_name, dad_name, mom_name):
        self.child_name=child_name
        dad.__init__(self, dad_name)
        mom.__init__(self, mom_name)
    
    @property
    def say_inf(self):
        return f"my name is : {self.child_name} and my dad is : {self.dad_name}  adn my mom is : {self.mom_name}"
    

jack=child('jack','peter','angel')

print(jack.say_inf)
print(jack.father())
print(jack.mother())
    




# Another example of multi inheritance

class A:
    def __init__(self, name):
        self.name=name
    
    def say_inf_a(self):
        return self.name

class B(A):
    
    def __init__(self,name ,family):
        self.family=family
        super().__init__(name)
    
    def say_inf_b(self):
        return self.family , self.name    

class C(B):
    
    def __init__(self,name,family,age):
        self.age=age    
        super().__init__(name,family)
    def say_inf_c(self):
        return self.name , self.family , self.age 

D=C('ali' , 'mobinifar', 25)



