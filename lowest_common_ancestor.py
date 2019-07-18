
class Node(object):
    def __init__(self,value, parent):
        self.value = value
        self.parent = parent

root = Node(1,None)
two = Node(2,root)
three = Node(3,root)
four = Node(4,two)
five = Node(5,two)
six = Node(6,three)
seven = Node(7, three)
eight = Node(8,four)
nine = Node(9,four)

def lca(node1,node2):
    list1 = []
    list2 = []
    
    while node1.parent:
        list1.append(node1.value)
        node1 = node1.parent
    list1.append(node1.value)
        
    while node2.parent:
        list2.append(node2.value)
        node2 = node2.parent
    list2.append(node2.value)
    
    common_ancestor = next((ancestor for ancestor in list1 if ancestor in list2),None)
        
    return common_ancestor

if __name__ == "__main__":
    print(lca(five, eight))
