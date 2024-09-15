'''import os
def filegenerator(data):
    print(data)
    path = 'files'
    filename = data['form']
    isExist = os.path.exists(path)
    print(isExist)
    if isExist == False:
        os.mkdir(path)
        print("Path Created")
    else:
        print("ok")
        dir_list = os.listdir(path)
        print(dir_list)
        if filename not in dir_list :
            print("File need to created")
            path = 'files'
            try:
                with open(os.path.join(path,filename),'w') as fp:
                    fp.write(data)
                    print("done")
            except Exception as e:
                print(e)
'''
import os
import json

def filegenerator(data, path="files", filename=None, mode="w"):

    if not filename:
        filename = data['form']
        print(filename)

    if not os.path.exists(path):
        os.mkdir(path)

    file_path = os.path.join(path, filename)
    print(file_path)

    try:
        with open(file_path, mode) as f:
            json.dump(data, f, indent=4)
        print("Data written to file:", file_path)
    except Exception as e:
        print("Error creating or writing to file:", e)
    
    return file_path


def path_creation(path="files"):
    if not os.path.exists(path):
        os.mkdir(path)

