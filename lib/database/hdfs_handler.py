from hdfs.client import Client

client = Client("http://192.168.1.197:50070", root="/", timeout=100, session=False)
print client.list("/topics")
# with client.read("/topics") as reader:
#     print reader.read()

