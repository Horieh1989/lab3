import urllib.request
import matplotlib.pyplot as plt
import numpy as np
import csv
import os

data_url="https://raw.githubusercontent.com/Horieh1989/lab3/refs/heads/master/Datas/unlabelled_data.csv"

#download data
try:
    urllib.request.urlretrieve(data_url, "unlabelled_data.csv")
except Exception as e:
    print(f"Fail to download datapoints.txt: {e}")


#open data in a list
response = urllib.request.urlopen(data_url)
lines = [line.decode('utf-8') for line in response]  # decode bytes to string
csv_reader = csv.reader(lines)#csv_reader is an irritator


x_data=[]
y_data=[]

for row in csv_reader:
    x_data.append(float(row[0]))#colimns[0]
    y_data.append(float(row[1]))#columns[1]
    
    
x_data=np.array(x_data)
y_data=np.array(y_data)
#plot 
plt.scatter(x_data, y_data)

plt.title("plt for datas")
plt.xlabel("colum(0)")
plt.ylabel("colun(1)")
plt.show()
    

    
    








    
