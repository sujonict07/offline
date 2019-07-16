a = { "key1": 1,
      "key2": { 
            "key3": 1, 
            "key4": {
                  "key5": 4
                  }
             }
      }

  
def find_depth(nested_object, depth=1):
    for key in nested_object:        
        print(key, depth)        
        if type(nested_object.get(key)) is dict:
            new_dict = nested_object.get(key)                        
            find_depth(new_dict, depth+1)    
                   
            
if __name__ == "__main__":
    find_depth(a)
