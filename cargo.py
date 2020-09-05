from subprocess import check_output
from os import pipe,write,close
def cargo(path,args=False):
    if args==False:
        data=None
    else:
        data, temp = pipe() 
        write(temp, bytes(args, "utf-8")); 
        close(temp) 
    s = check_output("cd "+path+";cargo run", stdin = data, shell = True) 
    return s.decode("utf-8")

#HOW TO USE:
#the first argument is the path
#the second are argument seperated by \n
"""
print(cargo("/home/parsa/AAA_RUST/hello_world","a\nb\n12"))
"""
#arguments can be ignored if there is no
"""
print(cargo("/home/parsa/AAA_RUST/hello_world"))
"""
#returns a string seperated by \n