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


    


def y_line(x, slope, intercept):
    return slope * x + intercept



#splli the line    
def calculate_split_line(x_data,y_data):
    slope=-1
    intercept=np.median(x_data+ y_data)
    x_values= np.array([np.min(x_data),np.max(x_data)])
    y=y_line( x_values,slope ,intercept)
    
    return x_values, y,intercept, slope

   


x_values,y,intercept,slope=calculate_split_line(x_data,y_data)






def list_point(x_data,y_data,slope,intercept):
    
    y_line_values=y_line(x_data,slope ,intercept)
    
    above_list=[(x_data[i],y_data[i])for i in range(len(x_data)) if y_data[i]>  y_line_values[i] ]
    under_list=[(x_data[i],y_data[i]) for i in range(len(x_data)) if y_data[i] <  y_line_values[i]]
 
    
    return np.array(above_list), np.array(under_list)

#test the list just the firs 5
above, below = list_point(x_data, y_data, slope, intercept)
print("Above:", above[:5])  # show first 5
print("Below:", below[:5])


# make a plot


    
def Csv_file(above_list,under_list):
    with open ("labelled_data.csv" ,"w") as file:
        for dot in above_list:
            file.write(f"{dot[0]},{dot[1]},1\n")
        for dot in under_list:
            file.write(f"{dot[0]},{dot[1]},0\n")
            
# Plot data dotss
def plot_data(above_list, under_list, x_values, y):

    # plot dotss above the line
    plt.scatter(above_list[:, 0], above_list[:, 1], s=10, color="blue", label=f"{len(above_list)} Points Above Line")

    # plot dots below the line
    plt.scatter(under_list[:, 0], under_list[:, 1], s=10, color="yellow", label=f"{len(under_list)} Points Below Line")
   

    plt.plot(x_values, y, color="r", linewidth=2)

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title(f"Data Points")
    plt.legend()
    plt.grid()
    plt.show()
    
Csv_file(above, below)
plot_data(above, below, x_values, y)