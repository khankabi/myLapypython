def welcome():
    ''' this is my own module
    '''
    print("hello guys")
    print(__name__)


if __name__=="__main__":
    print(__name__)
    welcome()
    print(welcome.__doc__)