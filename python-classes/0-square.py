class Square:
    def __init__(self, size):
        self.__size = size

    def get_size(self):
        return self.__size

    def set_size(self, size):
        if size < 0:
            raise ValueError("Size must be non-negative")
        self.__size = size