class Node:
    def __init__(self):
        self.content = ""
        self.children = {}
        self.isFile = False


class FileSystem:

    def __init__(self):
        self.root = Node()

    def ls(self, path: str) -> List[str]:
        path_list = path.split("/")
        cur = self.root
        for p in path_list:
            if not p: continue
            if p not in cur.children: cur.children[p] = Node()
            cur = cur.children[p]
        if cur.isFile: return [p]
        return sorted(cur.children.keys())

    def mkdir(self, path: str) -> None:
        path_list = path.split("/")
        cur = self.root
        for p in path_list:
            if not p: continue
            if p not in cur.children: cur.children[p] = Node()
            cur = cur.children[p]

    def addContentToFile(self, filePath: str, content: str) -> None:
        path_list = filePath.split("/")
        cur = self.root
        for p in path_list:
            if not p: continue
            if p not in cur.children: cur.children[p] = Node()
            cur = cur.children[p]
        cur.content += content
        cur.isFile = True

    def readContentFromFile(self, filePath: str) -> str:
        path_list = filePath.split("/")
        cur = self.root
        for p in path_list:
            if not p: continue
            if p not in cur.children: cur.children[p] = Node()
            cur = cur.children[p]
        return cur.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)