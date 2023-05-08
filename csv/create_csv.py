import csv
import os

# Relative path
path = 'empty_csv.csv'
# Absolute path
path = os.path.join(os.getcwd(),'empty_csv.csv')

# Write
file = open(path,'w')
writer = csv.writer(file,delimiter=',')
file.close()