# program to manage libra book returned book and borrowing request
from collections import deque

librarybooks_list = deque(["Maths","biology","chemistry","IT","database"])

def returnedBooks():
    if librarybooks_list:
        librarybooks_list.pop()
    else:
        print("No item Found")

def borrowingRequest():
    if librarybooks_list:
        librarybooks_list.popleft()
    else:
        print("No Item Found")

returnedBooks()
borrowingRequest()

print(librarybooks_list)