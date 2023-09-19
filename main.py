import TestClass
import ClassToJson

if __name__ == '__main__':
    user1 = TestClass.UserInfo("A", 10, 100, 50, 2340)

# Make Class Type To Json File
    ClassToJson.make(user1)


