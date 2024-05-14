class MYclass:
    __hiddenvariable =0            #This are the hidden variable

    def add(self, increment):
        self.__hiddenvariable+= increment
        print(self.__hiddenvariable)

Obje1=MYclass()
Obje1.add(5)
print(Obje1.__hiddenvariable)
