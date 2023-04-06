import csv
import matplotlib.pyplot as plt
import tkinter
from tkinter import *
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image


#This is the function for when the "ENTER" button
# is clicked on the GUI.
#When the button is clicked, the state name that
# the user has entered is compared against a file that
# contains state names.
#A graph of all of the states' average monthly electricity
# usage (also, within its own respective file)
# is then pulled up with the user's state highlighted
# on the graph.
def btn_clicked(): #all of btn_clicked() by Carly
    stateName = name.get() #retrieves the user's input of their state
    #read states file:
    legalNameStates = open('states.csv')
    avg_list_maker3 = csv.reader(legalNameStates) #converts States File into list of states
    for row in avg_list_maker3: #checking if the state input is in our States File
        if stateName not in row:
            stateInputLabel['text'] = 'Please input a valid state with the format: "State"'
            enterButton() #resets the ENTER button for a new state input
        position = row.index(stateName) #saves the index position of the entered state so that the
                                        #correct state electricity usage can be pulled from the
                                        #Usage File


    #formats State Electricity Usage File into list:
    usageList = open('newUsage.csv')
    avg_list_maker = csv.reader(usageList)
    usageList = []

    for row in avg_list_maker:  #ensures the data correctly gets put in list
        usage = row
        for num in row:
            finalNum = int(num)
            usageList.append(finalNum)


    #Imports a file of state abbreviations and converts it
    # to a list in order to later use the abbreviations as
    # the labels for the x-axis on the graph of States' Monthly
    # Avg Electricity Usage:
    statesList = open("stateAbbreviations.csv")
    avg_list_maker2 = csv.reader(statesList)

    for row in avg_list_maker2:  #ensures the data correctly gets put in list
        states = row


    #Graphing the States' Monthly Avg Electricity Usage using
    # state abbreviations list (states) as the x-axis values
    # and the states' electricity usage (usageList) as the
    # y-values
    plt.plot(states, usageList, 'c', alpha=0.5)

    #x,y, and title labels on the graph:
    plt.xlabel('States')
    plt.ylabel(f'Monthly Avg Electricity\n Usage per Household (kWh)')
    plt.title("States' Monthly Average Electricity Usage")

    #point on graph that highlights the user's state and its
    #electricity usage:
    plt.annotate(f'{stateName}: {usageList[position]} kWh',
                 xy=(states[position], usageList[position]),
                 xytext=(states[position + 1], usageList[position])) #labels the dot
    plt.plot(states[position], usageList[position], 'mo') #makes the dot on the state usage

    plt.show() #function that actually displays the graph


    #Label on GUI that prints the user's state's avg electricity usage:
    avgStateUsage['text'] = f"{stateName}'s average monthly electricity usage is {usageList[position]} kWh."

    #Label on GUI that prints a statement prepping the user to enter their own electricity usage
    ask4yours = Label(root, text=f"Let's see how your electricity usage compares!", font=("calibre", 35))
    ask4yours.grid()
    ask4yours.place(x=750, y=570, anchor="center")

    # Carly: calls the NEXT button function so that the button
    # appears and operates on the GUI; button opens new frame
    # asking for user's personal energy usage
    next1Button()

def next_clicked():
    framePersonalUsage = Frame(root, width=1500, height=800)
    framePersonalUsage.grid()




#Carly: GUI base
root = tkinter.Tk()
root.title('GUI')
root.geometry('1500x800')

#Carly: GUI intro title --> tells the user what the program is going to do:
titleLabel = Label(root, text = "Let's reduce your carbon footprint!", font=("calibre", 45))
titleLabel.grid()
titleLabel.place(x = 750, y = 50, anchor="center")

#Carly: Empty GUI label for the print statement of the state energy usage.
#I made this so that if the user wants to try to input different states,
#the print statement saying the energy usage will actually change rather
#than printing another label on top
avgStateUsage = Label(root, text=f"", font=("calibre", 35))
avgStateUsage.grid()
avgStateUsage.place(x=750, y=500, anchor="center")

#Carly: declaring string variable for storing stateName
name = tkinter.StringVar(root)


#Carly: GUI entry box that asks for user input:
    #the question:
stateInputLabel = Label(root, text = "What state do you live in?", font=("Arial", 35))
stateInputLabel.grid()
stateInputLabel.place(x = 750, y = 320, anchor="center")
    #the box itself:
stateNameInput = Entry(root, textvariable = name, bd = 5, width=50, relief="sunken", font=("calibre"))
stateNameInput.grid(column =1, row =1)
stateNameInput.place(x = 750, y = 390, anchor = "center", height= 50)


#Carly: function for the ENTER button to submit state name!
def enterButton():
    btn = tkinter.Button(text = 'ENTER', bd = 5, command=(lambda: btn_clicked()))
    btn.place(x = 750, y = 450, anchor = 'center')


#Carly: not finished, but the function for the NEXT button that will
#pull up a request for the user's own electricity usage
def next1Button():
    btn2 = tkinter.Button(text = 'NEXT', bd = 5, command=(lambda: next_clicked()))
    btn2.place(x = 750, y = 625, anchor = 'center')


#Noah: going to create a function that labels the state as
#northern or southern --> will be called for within
#enterButton() so the user's state input can apply to it


#Nathan: going to create a function that compares the user's
#inputted electricity usage against their state's electricity
#usage.

#Julia: If user's usage higher than the state's, run a function
# that asks the user to check boxes if they do certain energy
# wasting habits, kind of like a mini survey.
# Based on these results and whether the state is northern or southern
# (maybe time of year as well if we end up making a function for that),
# print ways to reduce these habits and their overall energy usage.
#If user's usage lower than the state's, congratulate the user and ask
#if they want to find out some ways they can reduce their usage even more.
#If yes, refer to the function that runs when the user's usage is higher.


#Carly: calls the ENTER button function so that the button
# appears and operates on the GUI
enterButton()





#Carly: makes sure the window displays in an infinite loop
# until closed out by user
root.mainloop()

