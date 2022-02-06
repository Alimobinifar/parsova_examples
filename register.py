
import datetime


class Ali:

    def __init__(self) -> None:
        print('hi')
        
    def mein(x):
        print('hello ')
        return x

def pl():
    Username=input('please enter your username : ')

    Password =input('please enter ypur pass word : ')

    file_url='register.txt'

    with open (file_url , 'a') as f:
        curret_time=str(datetime.datetime.now())
        try:
            f.writelines([Username,' ',Password,' ',curret_time,'\n'])
        except:
            'Error in internal server '

