import TestClass
import ClassToJson
import JsonToClass

if __name__ == '__main__':
    user1 = TestClass.UserInfo("A", 10, 100, 50, 2340)
    user2 = TestClass.UserInfo("B", 32, 750, 250, 15902)

    userlist = []
    userlist.append(user1)
    userlist.append(user2)

# Make Class Type To Json File
    ClassToJson.make(userlist)
# Create Item Class
    item = TestClass.Item("Sword", 1500)
# Get Json From Item Class And Pass Over
    JsonToClass.make(ClassToJson.get(item))

