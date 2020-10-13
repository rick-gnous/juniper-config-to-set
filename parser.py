# Tom Price writes the program in PHP here : https://github.com/pgnuta/juniper-config-to-set
# I adapt it in Python and add some enhancements
__author__ = "Tim Price | rick@gnous.eu"
__licence__ = "GPL3"

class ParserJuniper:
    def __init__(self):
        self.tree = []

    def resetTree(self):
        self.tree = []

    def printTree(self, tree):
        return ''.join(map(str, tree))

    def parse(self, line):
        """
        Parse a line of conf

        :param line str: line will be parse
        :ret str: a parse string, empty if its a comment
        """
        ret = ""
        line = line.strip()
        if not line.startswith('#'):
            if '#' in line:
                line, comment = line.split('#', 1)
                line = line.strip()

            if line.endswith(';'):
                line = line[:-1]
                 
                if not self.tree:
                    ret = "set " + line
                else:
                    ret = "set " + self.printTree(self.tree) + line
             
            if line.endswith('{'):
                line = line[:-1]
                self.tree.append(line)

            if line.endswith('}'):
                self.tree.pop()

        return ret
    
    def parseFile(self, path):
        """
        parse a file and return the commands

        :param path str: the path to file
        :ret str: the series of set commands
        """
        ret = ""
        with open(path, 'r') as file:
            self.resetTree()
            for line in file:
                lineConf = self.parse(line)
                if lineConf:
                    ret += lineConf + "\n"
        return ret

#parser = ParserJuniper()
#parser.parseFile("test")
