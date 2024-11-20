'''class Class1:
    def x1(self):
        print("Class1" )
class Class2(Class1):
    def x2(self):
        super().x1()
        print("Class2" )
name = Class2()
name.x2()'''

'''try:
    print("start code")
    print(10 / 0)
    print("finish code with no errors")
except NameError:
    print("We have an NameError")

except ZeroDivisionError:
    print("We have an ZeroDivisionError")

print("The end.")'''

'''try:
    try:
        print("start code")
        print(error)
        print("No errors")
    except SyntaxError:
        print("Wrong Syntax")
except NameError as error:
    print(error)'''

try:
    print("Hello")
    print(error)
    print("No error")
except NameError as error:
    print(error)
else:
    print("No problems")
finally:
    print("Finally code")