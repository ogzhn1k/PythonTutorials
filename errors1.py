
# num = int(input("Please enter the number : "))

# try :
#    if num < 5 :
#       raise Exception("Number can not be lower than 5")

# except :
#     print("Number can not be lower than five")   


def check_password(psw) :
    import re # regular expression
    if len(psw) < 8 :
        raise Exception("Password length can not be lower than 8!!!")
    elif not re.search("[a-z]",psw) :
        raise Exception("Password has to contains lower case")
    
    elif not re.search("[A-Z]",psw) :
        raise Exception("Password has to contains upper case")  
          
    elif not re.search("[0-9]",psw) :
        raise Exception("Password has to contains number")    
    
    elif not re.search("[_$@]",psw) :
        raise Exception("Password has to contains alphanumeric character")    
        
    elif re.search("\s",psw) :
        raise Exception("Password has not to contains space character")       
    
    else :
        print("Password is valid")
 
password = "Alivelideli1907_"        

try:
    check_password(password)
except Exception as ex:
    print(ex)
else :
    print("Valid Password")    
finally :
    print("End of the control")    
    
class Person :
    def __init__(self, name):
      if len(name) > 10 :
          raise Exception("Length of the number must not be greater than 10!!!")   
      else :
          self.name
          
          
try :
    p = Person("Oguzhannnnnnn")
except Exception as ex :
    print(ex)     