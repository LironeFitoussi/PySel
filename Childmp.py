from OopsDemo import Calculator

class ChildImpl(Calculator):
    def __init__(self, name, version):
        super().__init__(name, version)
        print("ChildImpl is initialized with name:", name, "and version:", version)
    
    def sum_multiply(self, a, b):
        return self.multiply(a, b) + self.add(a, b)
    
    def sum_subtract(self, a, b):
        return self.subtract(a, b) + self.add(a, b)

    def print_info(self):
        print("Name:", self.name, "Version:", Calculator.version)
    