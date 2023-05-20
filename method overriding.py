class Parent:
    def view(self):
        print("this is Parent")

class Child(Parent):
    def view(self):
        super().view()
        print('this is Child')

obj=Child()
obj.view()
