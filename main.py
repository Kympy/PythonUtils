import TestClass
import ClassToJson
import JsonToClass
import ImageFilter


if __name__ == '__main__':

# Create user info data
    user1 = TestClass.UserInfo("A", 10, 100, 50, 2340)
    user2 = TestClass.UserInfo("B", 32, 750, 250, 15902)

    userlist = []
    userlist.append(user1)
    userlist.append(user2)

# Make Class Type To Json File
    ClassToJson.make(userlist)

# Create Test Class
    class Test:
        def __init__(self, value):
            self.value = value

    testclass = Test(100)

# Get Json From Item Class And Pass Over : Make Test.py
    JsonToClass.make(ClassToJson.get(testclass), type(testclass).__name__)
    print(testclass.value)

# Load Image And Set Filter
    ImageFilter.negative("TestImage.jpg")
    ImageFilter.custom_gray_scale("TestImage.jpg")
