class Get_number:
      def __init__(self):
            self.__value =100

      @property
      def height(self):
            return self.__value
      @height.setter
      def height(self, value):
            self.__value =value
            return 

first_number = Get_number()
print(first_number.height)
      
      