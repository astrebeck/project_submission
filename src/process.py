import glob, os

#used to create test.txt and train.txt
#

# Current directory
current_dir = 'C:/Users/Smartsrc-alex/Documents/ML_class/project_submission/src/darknet/build/darknet/x64/data/Invert'

# Directory where the data will reside, relative to 'darknet.exe'
path_data = 'data/Invert/'

# Percentage of images to be used for the test set
percentage_test = 10

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')  
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)

for pathAndFilename in glob.glob(os.path.join(current_dir, "*.jpg")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test:
        counter = 1
        file_test.write(path_data + title + '.jpg' + "\n")

    else:
        file_train.write(path_data + title + '.jpg' + "\n")
        counter = counter + 1


for pathAndFilename in glob.glob(os.path.join(current_dir, "*.JPEG")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test:
        counter = 1
        file_test.write(path_data + title + '.JPEG' + "\n")

    else:
        file_train.write(path_data + title + '.JPEG' + "\n")
        counter = counter + 1