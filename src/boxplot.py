from sklearn.datasets import fetch_california_housing
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load California Housing dataset
housing = fetch_california_housing(as_frame=True)

# Features + target as a single DataFrame
df = housing.frame

##########################################################################################
# Quick check
"""
print(df.head())
print(df.shape)

# check the column header
print(df.columns)
#check null value in the dataset and data type in each column
print("\n")
print(df.info())
print("\nNumber of duplicated records in the dataset:",df.duplicated().sum())

#check the correlation between each column
df.corr()

# some descriptive statistics for the dataset
df.describe()

# calculate the variance for each columns in 2 decimal places
round(df.var(),2)

# show the data distributuon for each column, except latitude and longitude column

for i in df.columns:
  if i== "Latitude" or i=="Longitude":
    continue
  else:
    sns.histplot(df[i],kde=True)
    plt.title(f"Histogram for column:{i}")
    plt.show()"""
#############################################################################################

#Creating Box plot for each column, except latitude and longitude column
'''print("\n")
print("Generating the Box plot for each column, except latitude and longitude column")
for i in df.columns:
  if i =="Latitude" or i=="Longitude":
    continue
  else:
    sns.boxplot(df[i])
    plt.savefig(f"./figs/Box Plot_{i}.png")
    plt.title(f"Box Plot for column:{i}")
    plt.show()'''

############################################################################################
#Assignment Solution
print("\n")
print("\n")
print("These are the columns in dataset, you can type all to get box plot for all columns, except latitude and longitude column.")
print("You also can use the number before column header to choose a particular column.")
print("Type exit to quit the program.")
print("\n")
print("These are the columns in dataset:")
number=0
for i in df.columns:
  print(number,".",i)
  number=number+1
print("\n")

choice=True
while choice !=False:
  print("Which column would you like to choose for Box Plot?")
  userinput =input()
  if userinput=='exit':
    print("You quit this program.")
    break
  if userinput=='all':
    print("\n")
    print("Generating the Box plot for each column, except latitude and longitude column")
    print("\n")
    for i in df.columns:
      if i =="Latitude" or i=="Longitude":
        continue
      else:
        sns.boxplot(df[i])
        plt.savefig(f"./figs/Box Plot_{i}.png")
        plt.title(f"Box Plot for column:{i}")
        plt.show()   
  else:
        choice=int(userinput)
        if choice < 0 or choice > (len(df.columns)-1):
              print("Please provide a correct number.")
              print("\n")
              continue
        else:
              sns.boxplot(df[df.columns[choice]])
              plt.savefig(f"./figs/Box Plot_{df.columns[choice]}.png")
              plt.title(f"Box Plot for column:{df.columns[choice]}")
              plt.show()
              print("\n")
              continue


