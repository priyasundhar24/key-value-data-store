#use python version 3 and above
import time
import threading

dic={}

#'dic' is the dictionary in which we store the datas

#for create operation use syntax "create(key_name,value,timeout_value)" timeout is optional you can continue by passing two arguments without timeout

def create(k,val,timeout=0):
    if k in dic:
        print("error message: this key already exist!") #error message
    else:
        if(k.isalpha()):
            if len(dic)<(1024*1024*1024) and len(val)<=(16*1024*1024): #constraints for file size should be less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l=[val,timeout]
                else:
                    l=[val,time.time()+timeout]
                if len(k)<=32: #constraints for input key_name should be in capital at 32chars
                    dic[k]=l
                    print ("key created")
            else:
                print("error message: Memory limit exceeded!! ")#error message
        else:
            print("error message: key_name is invalid! key_name must contain only alphabets")#error message

#for read operation use syntax "read(key_name)"
            
def read(k):
    if k not in dic:
        print("error: key not found in database. Please enter a valid key again") #error message4
    else:
        b=dic[k]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                str_i="{"+str(k)+":"+str(b[0])+"}" #for returning the value in the format of JasonObject i.e.,"key_name:value"
                print( stri)
            else:
                print("error: time-to-live of",k,"has expired") #error message
        else:
            str_i="{"+str(k)+":"+str(b[0])+"}" 
            print(str_i)

#for delete operation use syntax "delete(key_name)"

def delete(k):
    if k not in dic:
        print("error: key not found in database. Please enter a valid key") #error message
    else:
        b=dic[k]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del dic[k]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",k,"has expired") #error message
        else:
            del dic[k]
            print("key is successfully deleted")

begin=0
while(begin!=1):
    num=int(input("Enter 1 to create\n Enter 2 to read\n Enter 3 to delete:"))
    if(num==1):
        #create
        k=input("Enter the key :")
        val=input("Enter the value: ")
        ttl=int(input("Enter Time to live (in seconds):")) #enter 0 to disable time to live property
        t1=threading.Thread(target=(create),args=(k,val,ttl))   #creating a key-value in the datastore
        t1.start()
        t1.join()
        begin=int(input('Do you want to stop the process ?'))
    if(num==2):
        #read
        k=input("Enter the key:")
        t2=threading.Thread(target=(read),args=(k,))   #creating a key-value in the datastore
        t2.start()
        t2.join()
        begin=int(input('Do you want to stop the process ?'))
    if(num==3):
        #delete
        k=input("enter the key:")
        t3=threading.Thread(target=(delete),args=(k,))   #creating a key-value in the datastore
        t3.start()
        t3.join()
        begin=int(input('Do you want to stop the process ?')) #enter 1 or 0 to continue or stop respectively
