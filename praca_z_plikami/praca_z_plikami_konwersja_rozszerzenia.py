from PIL import Image
import os
target = '.png'
path = "C://Users//duszk//PycharmProjects//python_zadania//images"
files_in_dir = os.listdir(path)
print(files_in_dir)

for i in range(4):
    im = Image.open(os.path.join(path, files_in_dir[i]))
    im.save(files_in_dir[i] + "_to_" + target)
