#import matplotlib.pyplot as plt
import csv

#user input:
print('What state do you live in?')
stateName = input()

#read states file:
legalNameStates = open(r"C:\Users\carly\Downloads\Computer Science\states.txt")
avg_list_maker3 = csv.reader(legalNameStates)
for row in avg_list_maker3:
    position = row.index(stateName)
    print(position)

#electricity usage list:
usageList = open(r"C:\Users\carly\Downloads\Computer Science\newUsage.txt")
avg_list_maker = csv.reader(usageList)

usageList = []
for row in avg_list_maker:  #ensures the data correctly gets put in list
    usage = row
    print(f'{row}')
    for num in row:
        finalNum = int(num)
        usageList.append(finalNum)
    print(usageList)


#states list:
statesList = open(r"C:\Users\carly\Downloads\Computer Science\stateAbbreviations.txt")
avg_list_maker2 = csv.reader(statesList)

for row in avg_list_maker2:  #ensures the data correctly gets put in list
    states = row
    print(f'{row}')



#graphing:
import matplotlib.pyplot as plt

plt.plot(states, usageList, 'c', alpha=0.5)

#graphing labels:
plt.xlabel('States')
plt.ylabel(f'Monthly Avg Electricity\n Usage per Household (kWh)')
plt.title("States' Monthly Average Electricity Usage")

#point on graph that highlights the user's state and it's
#electricity usage:
plt.annotate(f'{stateName}: {usageList[position]} kWh',
             xy=(states[position], usageList[position]),
             xytext=(states[position + 1], usageList[position]))
plt.plot(states[position], usageList[position], 'mo')

plt.show()
