# import json
# # person is our python dictionary 
# person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}
# # (dumps) stand for dict string convertor because dumps(s)stands for string
# personJSON = json.dumps(person, indent=3) # in this way can convert dictonary into jSON(dumps means converting into)
# # print(personJSON)


# # with open('person.json','w') as file:  # (w) stands for write function
# #     json.dump(person, file, indent=4)

# person = json.loads(personJSON) # in this way we can convert json dictionary into our python dictionary
# # print(person)

# # if we want to convert json file into python file
# # r is stand read 
# # in this way we can convert json file into our python file
 
# with open('person.json','r') as file:
#     person = json.load(file)
#     print(person)
    
import json

# we create a json class
class user:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        
        
user = user('max',27) # after that gave him a data

# json class is do not working directly that's why we create a encode function 
def encode_user(o):
    if isinstance(o, user):
        return{'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('object of type user is not JSON serializable')
    
    
# we can also encode json class with its own encoder or import its own encoder
from json import JSONEncoder
class userEncoder (JSONEncoder):
    
    def default(self, o):
        if isinstance(o, user):
            return{'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

        
        
    

userJSON = json.dumps(user, cls=userEncoder)
userJSON = userEncoder.encode(user)
# print(userJSON)

# we can convert json dictionary into class if we want the the single variable output like(name)
def decode_user(dct):
    if user.__name__ in dict:
        return user(name=dct['name'], age=dct['age'])
    return dct
    
user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)
    
