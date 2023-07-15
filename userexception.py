class myError(Exception):
    def __init__(self,value):
        self.value = value
        
try:
    raise myError("error raised")
except myError as err:
    print("a new error occured")

# class MyError(Exception):
#     def __init__(self, value):
#         self.value = value
#     def __str__(self):
#         return((self.value))
    
# try:
#     raise(MyError(3*2))
# except MyError as error:
#     print('A New Exception occurred: ', error.value)