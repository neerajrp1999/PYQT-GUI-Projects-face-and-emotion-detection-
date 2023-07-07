import firebase_admin
from firebase_admin import credentials,firestore,db
from google.cloud.firestore import ArrayUnion, ArrayRemove

cred = credentials.Certificate("a.json")
firebase_admin.initialize_app(cred,{
      "databaseURL": "https://meet-u-ac8ef-default-piprtdb.asia-southeast1.firebasedatabase.app/user1"
})
db=firestore.client()

def getContactListOfUser(user):
    return [d for d in db.collection("Users").document(user).get().get('contact')]

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
    db.reference("/"+gmail).set({"name":name,"password":password})

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







