import firebase_admin
from google.cloud.firestore import ArrayUnion, ArrayRemove
#custom_token = auth.create_custom_token(uid)
from firebase_admin import auth, messaging, credentials,firestore,db
import socket


cred = credentials.Certificate("a.json")
firebase_admin.initialize_app(cred,{
      "databaseURL": "https://meet-u-ac8ef-default-piprtdb.asia-southeast1.firebasedatabase.app/user1"
})
db=firestore.client()


def getIpAddress(user):
    return db.collection("Users").document(user).get().get("IPAddress")
    
def updateIpAddress(user):
    IPAddr = socket.gethostbyname(socket.gethostname())
    db.collection("Users").document(user).update({"IPAddress": IPAddr})
def getStatus(user):
    return db.collection("Users").document(user).collection("receivingCall").document("call").get().get("is")
def getReceivingCall_Call(user):
    try:
        d=db.collection("Users").document(user).collection("receivingCall").document("call").get()
        if(d.exists):
            return True if(d.get("is")=="1") else False
        return False
    except:
        return False

#name problem    
def sendCallRequest(user,another_user,name_another_user):
    db.collection("Users").document(another_user).collection("receivingCall").document("call").set({'is':"1",'who':user,"name":name_another_user})

def getReceivingCall_CallData(user):
    d=db.collection("Users").document(user).collection("receivingCall").document("call").get()
    if(d.exists):
        return [d.get("who"),d.get("name")]
def ReceivingCall_CallDataUpdate(user,data):
    CallDataUpdate(user,data)

def CallDataUpdate(user,data):
    db.collection("Users").document(user).collection("receivingCall").document("call").update({'is':data})

def createToken(user):
    return auth.create_custom_token(user)

def AddContactListOfUser(user,another_user,another_user_name):
    db.collection("Users").document(user).update({"contact": firestore.ArrayUnion([{another_user:another_user_name}])})

def RemoveContactListOfUser(user,another_user,another_user_name):
    db.collection("Users").document(user).update({"contact": firestore.ArrayRemove([{another_user:another_user_name}])})

def getContactListOfUser(user):
    try:
        data= [d for d in db.collection("Users").document(user).get().get('contact')]
    except:
        data=[]
    return data
def isAnotherUserAlreadyExistInContactListOfUser(user,another_user):
    d=[d for d in db.collection("Users").document(user).get().get('contact')]
    for i in d:
        if another_user in i:
            return True
    return False

def Authenticate(user,password):
    d=db.collection("Users").document(user).get()
    if(d.exists):
        return 2 if password==d.get('password') else 1
    else:
        return 0

def IsUserAlreadyExist(user):
    return True if db.collection("Users").document(user).get().exists else False

def InsertNewUser(gmail,password,name):
    db.collection("Users").document(gmail).set({"name":name,"password":password})

def insert():
    data={"name":"Neeraj R Prajapati","password":"1234"}
    data1={"contact":[{"nnnn.gmail.com":"hh"}]}
    doc_ref=db.collection("Users").document("neerajrp1999@gmail.com").get()
    d= [d for d in db.collection("Users").document("neerajrp1999@gmail.com").get().get('contact')]
    for i in d:
        if "nnnfgn.gmail.com" in i:
            print(True)
        else:
            print(False)
    #doc_ref = db.collection("users").document("alovelace")
    #doc_ref.update({"contact": firestore.FieldValue.arrayUnion([{"nnnn.gmail.com":"hah"}])})
    #a=doc_ref.update({u'contact': firestore.ArrayUnion([{"nnnfgn.gma1il.com":"hh"}])})
    #print(a)
    #ref=db.reference("/neerajrp1999@gmail.com")
    #ref.set(data)
#Authenticate("neerajrp1999@gmailcom","j")


















