import pyrebase
firebaseConfig = {
    "apiKey": "AIzaSyBzkD66TTPeq8-udcty8vXaThiJojugCb8",
    "authDomain": "meet-u-ac8ef.firebaseapp.com",
    "projectId": "meet-u-ac8ef",
    "storageBucket": "meet-u-ac8ef.appspot.com",
    "messagingSenderId": "1052926555635",
    "appId": "1:1052926555635:web:6cedfd8ca43e913a9e8e86",
    "measurementId": "G-NZ1B134X0D",
    'databaseURL': 'https://meet-u-ac8ef.firebaseio.com'
  }
firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()
def insert():
    
    data={"name":"Neeraj R Prajapati","password":"1234"}
    db.push({"neerajrp1999.@gmail":data})
insert()



