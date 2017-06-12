import os
import shutil
import random

cwd = os.getcwd()

path_test = os.path.join(cwd, 'test')

os.makedirs(path_test)

path_samples = os.path.join(cwd, 'samples')

os.chdir(path_samples)

list_of_samples = os.listdir()

random.shuffle(list_of_samples)

dictionary_file = open('dictionary.txt', 'w')
for i in range(len(list_of_samples)):
    dictionary_file.write(list_of_samples[i] + ' - ' + str(i) + '\n')

dictionary_file.close()

for i in range(len(list_of_samples)):
    shutil.copyfile(os.path.join(path_samples, list_of_samples[i]), os.path.join(path_test, (str(i) + "." + list_of_samples[i].split(".")[1])))

