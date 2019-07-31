# Training-Data_Splitter

## A simple python module to split image training data into training, test, and evaluation directories.

I have used this for
training a YOLOv3 model. Data must be split into directories by class. The root directory shall contain one images directory
for each class and one labels directory for each class. The name of the labels directory shall be the same as the image
directory with '_labels' appended to the end, like this:

images directory name for a single class: class1
labels directory name for a single class: class1_labels

The data will be organized into directories called 'images' and 'labels' with subdirectories for train, test, and validation
sets.

Sample execution:

`python3 org_data.py`
