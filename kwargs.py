def myFun(*args):
    for arg in args:
        print (arg)
   
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


 
def myFun(**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))
 
# Driver code
myFun(first ='Geeks', mid ='for', last='Geeks')   

# **kwargs ===== > is just for duictionariesv '
# *args >>>>>>>>>>>> is for tuple

print('Now')