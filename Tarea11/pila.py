class Stack:
    def __init__(self):
        self.__data = list()

    def is_empty(self):
        return len(self.__data) == 0

    def length(self):
        return len(self.__data)

    def pop(self):
        if self.is_empty():
            print('pila vacia')
        else:
            return self.__data.pop()

    def push(self, value):
        self.__data.append(value)

    def peek(self):
        return self.__data[ len(self.__data) -1 ]

    def to_string(self):
        print("----------------")
        for item in self.__data:
            print(f"| {item} |")
            print(" ----- ")
