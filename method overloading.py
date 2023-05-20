class A:
    def view(self):
        print("helo")

    def view(self,firstname=""):
        print('helo',firstname)

    def view(self,firstname='',lastname=''):
        print('helo',firstname,lastname)


obj=A()
obj.view()
obj.view('Jayakumar')
obj.view('Jayakumar','M')