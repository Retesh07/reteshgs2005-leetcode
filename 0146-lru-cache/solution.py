class Node:
    def __init__(self,key,val):
        self.key,self.val=key,val
        self.prev=self.next=None


class LRUCache:

    def __init__(self, capacity: int):
        self.mp={}
        self.cap=capacity
        self.head,self.tail=Node(0,0),Node(0,0)
        self.head.next,self.tail.prev=self.tail,self.head
    def remove(self,node):
        p,nxt=node.prev,node.next
        p.next,nxt.prev=nxt,p
    def insert(self,node):
        p=self.tail.prev
        p.next=node
        node.prev=p
        node.next=self.tail
        self.tail.prev=node
    

    def get(self, key: int) -> int:
        if key in self.mp:
            self.remove(self.mp[key])
            self.insert(self.mp[key])
            return self.mp[key].val
        
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.remove(self.mp[key])
        self.mp[key]=Node(key,value)
        self.insert(self.mp[key])

        if len(self.mp)>self.cap:
            lru=self.head.next
            self.remove(lru)

            del self.mp[lru.key]
            



        
