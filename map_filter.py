

my_list=[1,2,3,10,20]

def duplicate(number):
    if number>=11:
        return True

print(list(filter(duplicate,my_list)))
