# Python dictionary is an ordered collection of items. {key:value}
# Dictionaries are optimized for retrieving data. They have a key-based index, not an index-based index. 

my_dict = {'name': 'John', 1: [2, 4, 3]}
print(type(my_dict))                # <class 'dict'>

# Accessing values by their keys
print(my_dict['name'])              # John
print(my_dict[1])                # [2, 4, 3]

# Adding new item to the dictionary
my_dict['age'] = 25                   # Adds a new key-value pair
print(my_dict)                        # {'name': 'John', 1: [2, 4, 3], 'age': 25}
# Updating existing value
my_dict['name'] = 'Jane'              # Updates the value of the key 'name'
print(my_dict)                        # {'name': 'Jane', 1: [2, 4, 3], 'age': 25}

# Removing items from the dictionary using pop() method
removed_item = my_dict
# It stores elements in key/value pairs. 

#create a dictionary named capital_city
capital_city = {'India': 'New Delhi', 'USA': 'Washington D.C.', 'UK': 'London', 'France': 'Paris'}
print(type(capital_city)) # <class 'dict'>
print(capital_city) # {'India': 'New Delhi', 'USA': 'Washington D.C.', 'UK': 'London', 'France': 'Paris'}

#Accessing the value corresponding to a particular key:
country = 'India'
print('Capital of %s is %s' % (country, capital_city[country])) # Capital of India is New Delhi

#To check if a key exists in the dictionary or not:
if 'Japan' in capital_city:
    print('Capital of Japan is', capital_city['Japan'])
else:
    print('Japan is not present in the dictionary')

#You can also use get() method for accessing the value of a key. If the key is not present, it will return None.
print('Capital of Japan is', capital_city.get('Japan')) # Capital of Japan is None
print('Capital of Japan is', capital_city.get('Japan', 'Tokyo')) # Capital of Japan is Tokyo

#Adding new item to the dictionary:
capital_city['Germany'] = 'Berlin'
capital_city["Kenya"] = "Nairobi"
print(capital_city) # {'India': 'New Delhi', 'USA': 'Washington D.C.', 'UK': 'London', 'France': 'Paris', 'Germany': 'Berlin', 'Kenya': 'Nairobi'}  

#Removing an item from the dictionary:
del capital_city['USA']
print(capital_city) #{'India': 'New Delhi', 'UK': 'London', 'France': 'Paris', 'Germany': 'Berlin', 'Kenya': 'Nairobi'}

#Using for loop to iterate over the keys and values of the dictionary:
for country, city in capital_city.items():
    print('Capital of %s is %s' % (country, city)) 
# Capital of India is New Delhi
# Capital of Germany is Berlin
# Capital of France is Paris
# Capital of Kenya is Nairobi
    
#Creating an empty dictionary:
empty_dict = {}
print(empty_dict) #{}

#Checking whether a dictionary is empty or not:
print(len(capital_city)) # 4
print(not capital_city)   # False
print(bool(capital_city)) # True    
print(len(empty_dict))    # 0
print(not empty_dict)      # True
print(bool(empty_dict))    # False

#Removing all items from the dictionary:
capital_city.clear()
print(capital_city) # {}

#Deleting the dictionary:
del capital_city # The dictionary is deleted and trying to access it will raise an error.
# print(capital_city) # NameError: name 'capital_city' is not defined

#You can also pass a dictionary to a function as an argument. Here we are passing the "capital_city" dictionary to the "display_capital()"

def display_capital():
    """This function displays the capital cities of different countries."""
    capital_city = {'India': 'New Delhi', 'USA': 'Washington D.C.', 'UK': 'London', 'France': 'Paris'}
    print("Country\tCapital")
    for country, capital in capital_city.items():
        print("%s\t%s" % (country, capital))
        
display_capital() # Country	Capital
                  # India	New Delhi
                  # USA	Washington D.C.
                  # UK	London
                  # France	Paris

#You can also return a dictionary from a function. Here we are returning the "capital_city" dictionary from the "get_capital()" function.
def get_capital():
    """This function returns a dictionary containing the capital cities of different countries."""
    capital_city = {'India': 'New Delhi', 'USA': 'Washington D.C.', 'UK': 'London', 'France': 'Paris'}
    return capital_city

countries_cities = get_capital()
print(countries_cities['UK']) # London

#You can also use the dict() constructor to create a dictionary.
# The dict() constructor builds dictionaries directly from sequences of key-value pairs.
# Here we are creating a dictionary from a list of tuples.
key_values = [('Germany','Berlin'), ('Spain','Madrid'), ('Italy','Rome')]
countries_cities = dict(key_values)
print(countries_cities)   #{'Germany': 'Berlin', 'Spain': 'Madrid', 'Italy': 'Rome'}

#To add new entries to a dictionary you can use the update() method or the ** operator. 
#The update() method adds element(s) to the dictionary if the key is not present.
# If the key is already in the dictionary, it updates the value.
countries_cities.update({'UK':'London'})
print(countries_cities)    #{'Germany': 'Berlin', 'Spain': 'Madrid', 'Italy': 'Rome', 'UK': 'London'}

#Using the ** operator allows you to pass a dictionary of keyword arguments to a function.
# In this case, we have a function named "my_func()" that takes two positional arguments and a variable number of keyword arguments.

 
# The ** operator unpacks dictionaries into keyword arguments which are then used to add elements to the dictionary.
#If you want to ignore duplicate keys, use the update() method with the replace=True argument.

countries_cities.update({'Germany':'Frankfurt'},replace=True)
print(countries_cities)     #{'Germany': 'Frankfurt', 'Spain': 'Madrid', 'Italy': 'Rome'}

#Using the ** operator allows you to pass a dictionary of keyword arguments to a function.
#In this case, the keywords are the dictionary keys and the values are the corresponding items.

def my_func(a,b,**kwargs):
    print(a,b,kwargs)

my_func(10,'Hello',name='John Doe',age=30) # 10 Hello {'name': 'John Doe', 'age': 30}   

#Dictionaries have several built-in methods that allow you to manipulate them:

#clear() - removes all items from the dictionary.
#copy() - returns a copy of the dictionary.
#get() - returns the value for a given key, if the key is in the dictionary. If not, it returns a default value (if provided).
#items() - returns a list of key-value pairs in the dictionary.
#keys() - returns a list of the dictionary’s keys.
#values() - returns a list of the dictionary’s values.

d={'a':1,'b':2,'c':3}
print(d.keys())        #dict_keys(['a', 'b', 'c'])
print(d.values())      #[1, 2, 3]
print(d.items())       #[('a', 1), ('b', 2), ('c', 3)]

#pop() - remove specified key & return the value. If the key is not found, it raises a KeyError.
#popitem() – Return and remove a (key, value) pair from the dictionary. The pairs are returned in LIFO order.
# If default is given, it is returned if the dictionary is empty; otherwise, KeyError is raised.
x = {1:100, 2:200, 3:300}
print(x.pop(2))         #200
print(x)                #{1: 100, 3: 300}

try:
    print(x.pop(4))     #KeyError: 4
except KeyError as e:
    print(e)            #4

print(x.get(1))          #100
print(x.get(4))          #None
print(x.get(4,99))       #99

#setdefault() – If key is in the dictionary, return its value. If not, insert key with a value of default and return default.
#update() – Update the dictionary with the key/value pairs from other, overwriting existing keys.
#If other is a dict subclass, then does nothing. If other is a sequence of (key, value) pairs, then does same as dict.update(dict(seq)).
#If keyword arguments are specified, the dictionary is then updated with those key-value pairs.
y = {'x':'100','y':'200'}
z = {'y':'300','z':'400'}

print(y.update(z))      #{'x': '100', 'y': '300', 'z': '400'}
                         #None
print(y)                #{'x': '100', 'y': '300', 'z': '400'}

print(y.update({'x':'500'}, y='600'))  #{'x': '500', 'y': '600', 'z': '400'}    
print(y)                #{'x': '500', 'y': '600', 'z': '400'}

#setdefault() – Insert key with value, if key is not already in the dictionary. Otherwise, just return the value for the key.

print(y.setdefault('a','700'))  #700
print(y)                         #{'x': '500', 'y': '600', 'z': '400', 'a': '700'}

print(y.setdefault('x'))         #500
print(y)                         #{'x': '500', 'y': '600', 'z': '400', 'a': '700'}

#popitem() – Remove and return a (key, value) pair from the dictionary. Pairs are returned in LIFO order.
# If the dictionary is empty, it raises a KeyError.
w = dict([('A',1),('B',2),('C',3)])
print(w.popitem())             #('C', 3)
print(w)                        #{'A': 1, 'B': 2}

#The clear() method removes all items from the dictionary. It does not modify indices or references.
v = w.copy()
print(v)                        #{'A': 1, 'B': 2, 'C': 3}
v.clear()
print(v)                        #{} #{'A': 1, 'B': 2, 'C': 3}   

#The copy() method returns a shallow copy of the dictionary. It does not modify indices or references. 
u = v.copy()
print(id(u)) == print(id(v))   #False
print(u)                        #{'A': 1, 'B': 2, 'C': 3}
print(u is v)                  #False   

#The fromkeys() method returns a new dictionary with the specified keys and the specified value. The value defaults to None.
keys = {'a', 'b', 'c', 'd'}
values = [1, 2, 3, 4]
new_dict = dict.fromkeys(keys)  
print(new_dict)               #{'a': None, 'b': None, 'c': None, 'd': None}

print(dict.fromkeys(keys, values))  #{'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(len(dict()))            #0

#Test for unhashable type: list
try:
    print(dict.fromkeys([1,2,3]))  #TypeError: unhashable type: 'list'
except TypeError as e:
    print(e)                      #unhashable type: 'list'
    
#The setdefault() method returns the value of a key (if the key is in the dictionary).
# If not, then it inserts the key with the specified value (also default value if given) and returns the value. 
