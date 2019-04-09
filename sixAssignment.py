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
            self.children.append(data)

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
            visual += "\n"
            for node in nodes:
                visual += str(node.getData())
                nodes.remove(node)
                for n in node.getChildren():
                    nodes.append(n)
        return visual

    def getCurrentNode(self):
        current = "Current Node:\n"
        current += str(self.currentNode.getData()) + "\n"
        current += "Children:\n"
        current += "["
        for n in self.currentNode.getChildren():
            current += n.getData()
        current += "]"
        return current
    
    def setCurrentNode(self):
        return

    def add(self, item):
        newNode = Node(item)
        if self.root == None:
            self.root = newNode
            self.currentNode = self.root
        else:
            self.currentNode.addChild(item)

	# def search(self, item):
	# 	currentSelection = self.root
	# 	while currentSelection.getData() != item:
	# 		if currentSelection.getNextNode() == None:
	# 			return False
	# 		currentSelection = currentSelection.getNextNode()
	# 	return True

    def isEmpty(self):
        return self.root == None

def main():
    # sampleroot = Node(24)
    # print(sampleroot)
    tree1 = Tree()
    tree1.add(24)
    tree1.add(13)
    tree1.add(5)
    tree1.getCurrentNode()
    # print(tree1)

if __name__ == "__main__":
    main()