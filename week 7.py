class graph:

    def __init__(self):

        self.adjacency = {}    # 

    def insertvertex (self, v):
        self.adjacency[v] = [] 


    def insertedge(self, v, e):
        if v in self.adjacency:
            self.adjacency[v].append(e)
            self.adjacency[e].append(v)

    def printadjacency (self):
        print (self.adjacency)

    def dfs (self, v):
        self.stack = []
        self.visited = []
        self.stack.append (v)
        while self.stack != []:
            value = self.stack.pop()
            if value not in self.visited:
                self.visited.append(value)
                for e in self.adjacency[value]:
                    self.stack.append(e)
        f = open("dfs.txt", "w")
        f.write("dfs traversal: %s " % self.visited )
        f.close()
        return self.visited

    def bfs (self,v):
        self.queue = []
        self.visited = []
        self.queue.insert(0,v)
        while self.queue != []:
            value = self.queue.pop ()
            if value not in self.visited:
                self.visited.append(value)
                for e in self.adjacency(value):
                    self.queue.insert(0,e)
        f = open("bfs.txt", "w")
        f.write("bfs traversal: %s " % self.visited )
        f.close()
        return self.visited
                    

    
                
    
g = graph()

g.insertvertex(1)
g.insertvertex(2)
g.insertvertex(3)
g.insertvertex(4)
g.insertedge(1,2)
g.insertedge(2,3)
g.insertedge(3,4)

