import os
import sys

# 操作一：使用protoc命令生成test001_pb2.py文件
proto_file = 'test001.proto'
python_out = '.'

protoc_command = f'protoc --proto_path=. --python_out={python_out} {proto_file}'
os.system(protoc_command)

# 操作二：导入test001_pb2模块，解析数据并添加一条新的记录，然后将其写入二进制文件，并读取出来
import test001_pb2

# 创建一个新的AddressBook对象
address_book = test001_pb2.AddressBook()

# 创建一个新的Person对象并添加到AddressBook中
person = address_book.people.add()
person.name = "John Smith"
person.id = 1234
person.email = "john.smith@example.com"

# 创建一个新的PhoneNumber对象并添加到Person中
phone_number = person.phones.add()
phone_number.number = "555-1234"
phone_number.type = test001_pb2.Person.HOME

# 将AddressBook序列化为二进制数据
binary_data = address_book.SerializeToString()

# 将二进制数据写入文件
with open('addressbook.bin', 'wb') as f:
    f.write(binary_data)

# 从文件中读取二进制数据并解析为AddressBook对象
with open('addressbook.bin', 'rb') as f:
    binary_data = f.read()
    address_book = test001_pb2.AddressBook()
    address_book.ParseFromString(binary_data)

# 打印读取的数据
for person in address_book.people:
    print("Name:", person.name)
    print("ID:", person.id)
    print("Email:", person.email)
    for phone_number in person.phones:
        print("Phone number:", phone_number.number)
        print("Phone type:", phone_number.type)