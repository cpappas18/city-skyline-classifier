import os
import math
import random

num_toronto = len([name for name in os.listdir('./toronto_images') if os.path.isfile(os.path.join('./toronto_images', name))]) # 1395
num_nyc = len([name for name in os.listdir('./new_york_images') if os.path.isfile(os.path.join('./new_york_images', name))]) # 1237
num_paris = len([name for name in os.listdir('./paris_images') if os.path.isfile(os.path.join('./paris_images', name))]) # 1315

num_toronto_train = math.floor(num_toronto*0.8) # 1116
num_nyc_train = math.floor(num_nyc*0.8) # 989
num_paris_train = math.floor(num_paris*0.8) # 1052

train_list = []; # len = 3157
test_list = []; # len = 790

# creating training and testing lists of the form (image path, label)
for path, dirs, files in os.walk("./toronto_images"):
   for filename in files[0:num_toronto_train]:
      train_list.append(("toronto_images/" + filename, 'toronto'))
   for filename in files[num_toronto_train:]:
      test_list.append(("toronto_images/" + filename, 'toronto'))

for path, dirs, files in os.walk("./new_york_images"):
   for filename in files[0:num_nyc_train]:
      train_list.append(("new_york_images/" + filename, 'new york'))
   for filename in files[num_nyc_train:]:
      test_list.append(("new_york_images/" + filename, 'new york'))
        
for path, dirs, files in os.walk("./paris_images"):
   for filename in files[0:num_paris_train]:
      train_list.append(("paris_images/" + filename, 'paris'))
   for filename in files[num_paris_train:]:
      test_list.append(("paris_images/" + filename, 'paris'))   

random.shuffle(train_list)
random.shuffle(test_list)

# write training list to csv 
with open('./train_data.csv', 'w+') as f:
   for (path, label) in train_list:
      f.write('%s,%s\n'%(path,label))

f.close()

# write testing list to csv   
with open('./test_data.csv', 'w+') as f:
   for (path, label) in test_list:
      f.write('%s,%s\n'%(path,label))
      
f.close()