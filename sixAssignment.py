class Node:
    def __init__(self, data):
        self.node = data
        self.children = []

    def __repr__(self):
        return "["+str(self.node)+"]"

    def getData(self):
        return self.node

    def setData(self, data):
        self.node = data

    def addChild(self, data):
        if type(data) == Node:
            self.children.append(data)
        else:
            newChild = Node(data)
            self.children.append(newChild)

    def getChildren(self):
        return self.children

class Tree:
    def __init__(self):
        self.root = None
        self.currentNode = self.root

    def __repr__(self):
        visual = ""
        nodes = [self.root]
        while nodes != []:
            newnodes = []
            for node in nodes:
                visual += "[" + str(node.getData()) + "]"
                for n in node.getChildren():
                    newnodes.append(n)
                nodes = newnodes
            visual += "\n"
        return visual

    def getCurrentNode(self):
        current = "Current Node:\n"
        current += self.currentNode.__repr__() + "\n"
        current += "Children:\n"
        current += "["
        for n in self.currentNode.getChildren():
            current += n.__repr__()
        current += "]"
        return current
    
    def setCurrentNode(self, target):
        for n in self.currentNode.getChildren():
            if n.getData() == target:
                self.currentNode = n
                return
        change = input("Node not found.\nEnter 1 to set current to root, or press ENTER to remain at current node.\n")
        if change == "1":
            self.currentNode = self.root
        else:
            return

    def add(self, item):
        newNode = Node(item)
        if self.root == None:
            self.root = newNode
            self.currentNode = self.root
        else:
            self.currentNode.addChild(item)

    def search(self, item):
        currentSelection = [self.root]
        while currentSelection != []:
            nextLevel = []
            for node in currentSelection:
                if node.getData() == item:
                    return True
                for n in node.getChildren():
                    nextLevel.append(n)
            currentSelection = nextLevel
        return False

    def isEmpty(self):
        return self.root == None

class Vertex:
    def __init__(self, data):
        self.vertex = data
        self.directedEdges = []

    def __repr__(self):
        return "["+str(self.vertex)+"]"

    def getData(self):
        return self.vertex

    def setData(self, data):
        self.vertex = data

    def addEdge(self, data):
        if type(data) == Vertex:
            self.directedEdges.append(data)
        else:
            newEdge = Vertex(data)
            self.directedEdges.append(newEdge)

    def getEdges(self):
        return self.directedEdges

class DirectedGraph:
    def __init__(self):
        self.vertexList = []

    def __repr__(self):
        visual = ""
        vertices = []
        while vertices != []:
            newnodes = []
            for node in vertices:
                visual += "[" + str(node.getData()) + "]"
                for n in node.getChildren():
                    newnodes.append(n)
                vertices = newnodes
            visual += "\n"
        return visual

    def getVertex(self, vert):
        if vert in self.vertexList:
            current = "Current Node:\n"
            current += vert.__repr__() + "\n"
            current += "Directed:\n"
            current += "["
            for n in self.currentNode.getEdges():
                current += n.__repr__()
            current += "]"
            return current

    def point(self, vert1, vert2):
        if type(vert1) != Vertex:
            raise("vert1 should be a vertex!")
        if vert1 in self.vertexList:
            vert1.addEdge(vert2)
        else:
            

    def search(self, item):
        currentSelection = self.currentVertex
        while currentSelection != []:
            nextLevel = []
            for vertex in currentSelection:
                if node.getData() == item:
                    return True
                for n in node.getChildren():
                    nextLevel.append(n)
            currentSelection = nextLevel
        return False

    def isEmpty(self):
        return self.currentVertex == None

def main():
    #------------Tree--------------#
    # sampleroot = Node(24)
    # print(sampleroot)
    # tree1 = Tree()
    # tree1.add(24)
    # tree1.add(13)
    # tree1.add(5)
    # print(tree1.getCurrentNode())
    # tree1.setCurrentNode(13)
    # print(tree1.getCurrentNode())
    # tree1.add(8)
    # print(tree1)
    # print(tree1.search(8))
    # print(tree1.search(24))

    # Tree's search runs in O(n) time because its worst case is
    # searching the entirety of the tree (length n), checking all of the rows
    # and finding no match.

    #--------Directed Graph--------#
    sampleVertex = Vertex(10)
    directed1 = DirectedGraph()
    directed1.add(sampleVertex)
    directed1.add(12)
    directed1.add()
    

if __name__ == "__main__":
    main()