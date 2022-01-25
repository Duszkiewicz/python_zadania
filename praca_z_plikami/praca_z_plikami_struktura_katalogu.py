import os

for root, directories, files in os.walk("C://Users//duszk//PycharmProjects//python_zadania//dev"):
   for name in files:
      print(os.path.join(root, name))
   for name in directories:
      print(os.path.join(root, name))