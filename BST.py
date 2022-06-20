class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self,value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return  self

    def insert2(self,value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert2(value)

        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert2(value)

        return self

    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False

    def contains2(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return  self.left.contains(value)
        elif value> self.value:
            if self.right is None:
                return  False
            else:
                return  self.right.contains(value)
        else:
            return True

    def getMin(self):
        currentNode = self
        while currentNode is not None:
            currentNode = currentNode.left
        return  currentNode.value

    def remove(self, value, parentNode = None):

        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMin()
                    currentNode.right.remove(currentNode.value, currentNode)
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.right = currentNode.right.right
                        currentNode.left = currentNode.right.left
                    else:
                        pass
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.right if currentNode.right is not None else currentNode.left
                break
        return self

    def getMin2(self):
        if self.left is not None:
            return self.left.getMin2()
        else:
            return self.left.value

    def remove2(self,value,parentNode = None):
        if value<self.value:
            self.left.remove2(value,self)
        elif value > self.value:
            self.right.remove2(value,self)
        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.getMin2()
                self.right.remove2(value,self)
            elif parentNode is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.left= self.left.left
                    self.right = self.left.right
                elif self.right is not None:
                    self.value = self.right.value
                    self.right = self.right.right
                    self.left = self.right.left
                else:
                    pass
            elif parentNode.left == self:
                parentNode.left = self.left if self.left is not None else self.right
            elif parentNode.right == self:
                parentNode.right = self.right if self.right is not None else self.left
        return self




root = BST(10)

root.insert(5).insert(12).insert(13)

root.remove2(12)

print(root.contains(12))

