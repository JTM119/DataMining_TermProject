import os
from PIL import Image


leaf_list = [
    "apple",
    "banana",
    "cherry",
    "corn",
    "grape",
    "orange",
    "pepper",
    "potato",
    "strawberry",
    "tea",
    "tomato",
]
for plant in leaf_list:
    fruit_path = os.path.join("fruit_class_edges", plant)
    os.makedirs(fruit_path, exist_ok=True)

old_location = "processed"
for dir in os.walk(old_location):
    print(dir[0])
    for plant in leaf_list:
        if plant in dir[0]:
            print(plant)
            dir_path = os.path.join("fruit_class", plant)
            for i in os.listdir(dir[0]):
                im = Image.open(os.path.join(dir[0], i))
                im.save(os.path.join(dir_path, i))
        else:
            continue
    print("-" * 100)
