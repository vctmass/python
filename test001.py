import os
import sys

#自动protoc命令
proto_file = 'test001.proto'
python_out = '.'

protoc_command = f'protoc --proto_path=. --python_out={python_out} {proto_file}'
os.system(protoc_command)

# 导入上一步生成test001_pb2
import test001_pb2

# 新的AddressBook对象
address_book = test001_pb2.AddressBook()

# 创建Person
person = address_book.people.add()
person.name = "John Smith"
person.id = 1234
person.email = "john.smith@example.com"

# 创建PhoneNumber
phone_number = person.phones.add()
phone_number.number = "555-1234"
phone_number.type = test001_pb2.Person.HOME

#序列化
binary_data = address_book.SerializeToString()

# 写入文件
with open('addressbook.bin', 'wb') as f:
    f.write(binary_data)

# 解析为AddressBook
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