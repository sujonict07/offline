
#### 1) [Write the following function’s body. A nested dictionary is passed as parameter. You need to print all keys with their depth](https://github.com/sujonict07/offline/blob/master/find_nested_depth.py).

### Sample Input:

```
{ "key1": 1, 
  "key2": { "key3": 1, 
            "key4": {
                      "key5": 4
                    }
          }
}
```

### Sample Output:
```
key1 1
key2 1
key3 2
key4 2
key5 3
```

#### 2) [ Write a new function with same functionality from Question 1, but it should be able to handle a Python object in addition to a dictionary from Question 1](https://github.com/sujonict07/offline/blob/master/find_nested_depth_with_class_objects.py).

### Sample Input:

```
class Person(object):
	def __init__(self, first_name, last_name, father):
		self.first_name = first_name
		self.last_name = last_name
		self.father = father

person_a = Person("User", "1", None)
person_b = Person("User", "2", person_a)

{ "key1": 1, 
  "key2": { "key3": 1, 
            "key4": {
                      "key5": 4,                      
                      "user": person_b,
                    }
          }
}
```

### Sample Output:
```
key1 1
key2 1
key3 2
key4 2
key5 3
user 3
first_name 4
last_name 4
father 4
first_name 5
last_name 5
father 5
```
