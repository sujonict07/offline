class Person(object):
	def __init__(self, first_name, last_name, father):
		self.first_name = first_name
		self.last_name = last_name
		self.father = father

person_a = Person("User", "1", None)
person_b = Person("User", "2", person_a)
a = { "key1": 1, "key2": { "key3": 1, "key4": {"key5": 4,"user": person_b}}}

def print_depth(a, depth=1):
    for key in a:        
        print(key, depth)        
        if type(a.get(key)) is dict:
            new_dict = a.get(key)                        
            print_depth(new_dict, depth+1)    
        elif type(a.get(key)) is Person:
            new_dict = a.get(key).__dict__
            print_depth(new_dict, depth+1)
                   
            
if __name__ == "__main__":
    print_depth(a)
