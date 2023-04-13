import csv
import matplotlib.pyplot as plt
import tkinter
from tkinter import *
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
import sv_ttk


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
    global stateName
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


    global avgStateEnergy
    avgStateEnergy = usageList[position]
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
    ask4yours = Label(root, text=f"Let's see how your electricity usage compares!", font=("sylfaen", 35))
    ask4yours.grid()
    ask4yours.place(x=750, y=460, anchor="center")

    # Carly: calls the NEXT button function so that the button
    # appears and operates on the GUI; button opens new frame
    # asking for user's personal energy usage
    next1Button()





def next_clicked():
    global framePersonalUsage
    framePersonalUsage = Frame(root, width=1500, height=800)
    framePersonalUsage.grid()
    personalEnergy = tkinter.StringVar(framePersonalUsage)

    # main title
    underline = Label(framePersonalUsage, text="_____________________________________________", font=("Castellar", 45))
    underline.grid()
    underline.place(x=750, y=70, anchor="center")
    titleLabel = Label(framePersonalUsage, text="Let's reduce your carbon footprint!", font=("Castellar", 45))
    titleLabel.grid()
    titleLabel.place(x=750, y=50, anchor="center")

    # Carly: GUI entry box that asks for user input:
    # the question:
    userEnergyLabel = Label(framePersonalUsage, text="What was your energy usage for this month?", font=("sylfaen", 35))
    userEnergyLabel.grid()
    userEnergyLabel.place(x=750, y=150, anchor="center")
    # the box itself:
    userEnergyInput = Entry(framePersonalUsage, textvariable=personalEnergy, bd=5, width=50, relief="sunken", font=("sylfaen"))
    userEnergyInput.grid(column=1, row=1)
    userEnergyInput.place(x=750, y=220, anchor="center", height=50)
    #energy units:
    units = Label(framePersonalUsage, text="kWh", font=("sylfaen", 20))
    units.grid()
    units.place(x=980, y=200)



    # Carly: ENTER button that pulls up the comparison of the user's personal energy
    # usage to that of their state's:
    def enterButtonUserEnergy():
        btn3 = tkinter.Button(text='ENTER', bd=5, command=(lambda: PowerBill(stateName)))
        btn3.place(x=750, y=280, anchor='center')

    # written by Nathan = compares the user's personal energy usage
    # to that of their state's so that they can get feedback on
    # if they need to reduce their carbon footprint more
    def PowerBill(stateIn):
        #defining variables in function by different titles, so we could work
        #on code separately
        power1 = personalEnergy.get()
        power = int(power1)
        state = stateIn
        average = avgStateEnergy

        #reprinting label for state's energy use
        stateAvgUsageLabel = Label(framePersonalUsage, text=(f"{state}'s Average Energy Usage: {average}kWh"),
                                   font=("sylfaen", 35))
        stateAvgUsageLabel.grid()
        stateAvgUsageLabel.place(x=750, y=350, anchor="center")

        #label for user's energy usage
        userUsageLabel = Label(framePersonalUsage, text=(f"Your Average Energy Usage: {power}kWh"),
                               font=("sylfaen", 35))
        userUsageLabel.grid()
        userUsageLabel.place(x=750, y=420, anchor="center")

        #comparing the user's personal energy usage to the state
        if power < average:
            comparisonLabel = Label(framePersonalUsage,
                                    text=(f"Monthly Energy Usage of {power}kWh is lower than state average."),
                                    font=("sylfaen", 30))
            comparisonLabel.grid()
            comparisonLabel.place(x=750, y=490, anchor="center")

            congratsLabel = Label(framePersonalUsage, text=(f"Good job! You are limiting CO2 output!"),
                                  font=("sylfaen", 30))
            congratsLabel.grid()
            congratsLabel.place(x=750, y=560, anchor="center")
            next2Button()
            framePersonalUsage.pack()


        elif power > average:
            comparisonLabel = Label(framePersonalUsage,
                                    text=(f"Caution! Monthly Power Usage of {power}kWh is higher than state average."),
                                    font=("sylfaen", 30))
            comparisonLabel.grid()
            comparisonLabel.place(x=750, y=490, anchor="center")
            fixLabel = Label(framePersonalUsage,
                             text=(f"Let's see what we can do to lower that usage!"),
                             font=("sylfaen", 30))
            fixLabel.grid()
            fixLabel.place(x=750, y=560, anchor="center")
            next2Button()
            framePersonalUsage.pack()


        else:
            comparisonLabel = Label(framePersonalUsage,
                                    text=(f"Monthly Power Usage of {power}kWh is equal to state average."),
                                    font=("sylfaen", 30))
            comparisonLabel.grid()
            comparisonLabel.place(x=750, y=490, anchor="center")
            next2Button()
            framePersonalUsage.pack()



    enterButtonUserEnergy()



#Carly: window for user's habits that eventually provides feedback
def next2_clicked():
    framePersonalUsage.destroy()
    frameHabits = Frame(root, width=1500, height=800)
    frameHabits.grid()
    frameHabits.tkraise()
    #frameHabits.root.grid_propagate(False)
    #personalEnergy = tkinter.StringVar(frameHabits)

    # main title
    underline = Label(frameHabits, text="_____________________________________________", font=("Castellar", 45))
    underline.grid()
    underline.place(x=750, y=70, anchor="center")
    titleLabel = Label(frameHabits, text="Let's reduce your carbon footprint!", font=("Castellar", 45))
    titleLabel.grid()
    titleLabel.place(x=750, y=50, anchor="center")


    # Carly: GUI entry box that asks for user input:
    # the question:
    instructionsLabel = Label(frameHabits, text="Check the boxes of habits that you do!", font=("sylfaen", 35))
    instructionsLabel.grid()
    instructionsLabel.place(x=750, y=150, anchor="center")
    frameHabits.pack()

    # Carly: GUI entry box that asks for user input:
    # the question:
    basedLabel = Label(frameHabits, text="We'll give you some feedback on how to reduce your energy usage based on your answers.", font=("sylfaen", 25))
    basedLabel.grid()
    basedLabel.place(x=750, y=220, anchor="center")

    def foot(image):
        img = Image.open(image)
        imageResize = img.resize((300,300), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(imageResize)

        imageLabel = Label(frameHabits, image=image)
        imageLabel.image = image
        imageLabel.place(x=150, y=450, anchor="center")
    foot(r'IMG_1041.PNG')



    #checkbox feedback
    def c1_On(xValue, yValue, button, feedbackPhrase):
        global footFill
        global c1Text
        habit1feedback = Label(frameHabits,
                               text="",
                               font=("sylfaen", 25))
        habit1feedback.grid()
        habit1feedback.place(x=xValue+400, y=yValue, anchor="center")
        def footfill():
            if footFill == 0:
                foot(r'IMG_1041.PNG')
            elif footFill == 1:
                foot(r'IMG_1042.PNG')
            elif footFill == 2:
                foot(r'IMG_1043.PNG')
            elif footFill == 3:
                foot(r'IMG_1044.PNG')
            else:
                foot(r'IMG_1045.PNG')

        if button['text']=='Yes':
            footFill -= 1
            button['text']='No'
            habit1feedback['text'] = "  " * len(feedbackPhrase)
            footfill()

        else:
            footFill += 1
            button['text']='Yes'
            habit1feedback['text'] = feedbackPhrase
            footfill()


    #1st checkbox
    global c1Text
    c1 = tkinter.Button(text=c1Text, bd=5, command=(lambda: c1_On(300,300,c1,'habit 1 feedback')), height = 2, width = 5)
    c1.place(x=300, y=300, anchor='center')
    c1QuestionLabel = Label(frameHabits,
                        text='habit 1?',
                        font=("sylfaen", 25))
    c1QuestionLabel.grid()
    c1QuestionLabel.place(x=400, y=300, anchor="center")

    #2nd checkbox
    global c2Text
    c2 = tkinter.Button(text=c2Text, bd=5, command=(lambda: c1_On(300, 400, c2,'habit 2 feedback')), height=2, width=5)
    c2.place(x=300, y=400, anchor='center')
    c2QuestionLabel = Label(frameHabits,
                            text='habit 2?',
                            font=("sylfaen", 25))
    c2QuestionLabel.grid()
    c2QuestionLabel.place(x=400, y=400, anchor="center")

    # 3nd checkbox
    global c3Text
    c3 = tkinter.Button(text=c3Text, bd=5, command=(lambda: c1_On(300, 500, c3, 'habit 3 feedback')), height=2, width=5)
    c3.place(x=300, y=500, anchor='center')
    c3QuestionLabel = Label(frameHabits,
                            text='habit 3?',
                            font=("sylfaen", 25))
    c3QuestionLabel.grid()
    c3QuestionLabel.place(x=400, y=500, anchor="center")

    # 4th checkbox
    global c4Text
    c4 = tkinter.Button(text=c4Text, bd=5, command=(lambda: c1_On(300, 600, c4, 'habit 4 feedback')), height=2, width=5)
    c4.place(x=300, y=600, anchor='center')
    c4QuestionLabel = Label(frameHabits,
                            text='habit 4?',
                            font=("sylfaen", 25))
    c4QuestionLabel.grid()
    c4QuestionLabel.place(x=400, y=600, anchor="center")







#Carly: GUI base
#root = ttkthemes.ThemedTk(theme='black')
root = tkinter.Tk()
sv_ttk.set_theme('dark')
root.title('GUI')
root.geometry('1500x800')



#Carly: GUI intro title --> tells the user what the program is going to do:
underline = Label(root, text = "_____________________________________________", font=("Castellar", 45))
underline.grid()
underline.place(x = 750, y = 70, anchor="center")
titleLabel = Label(root, text = "Let's reduce your carbon footprint!", font=("Castellar", 45))
titleLabel.grid()
titleLabel.place(x = 750, y = 50, anchor="center")


#Carly: Empty GUI label for the print statement of the state energy usage.
#I made this so that if the user wants to try to input different states,
#the print statement saying the energy usage will actually change rather
#than printing another label on top
avgStateUsage = Label(root, text=f"", font=("sylfaen", 35))
avgStateUsage.grid()
avgStateUsage.place(x=750, y=390, anchor="center")

#Carly: declaring string variable for storing stateName
name = tkinter.StringVar(root)
avgStateEnergy = None
stateName = None
framePersonalUsage = None
value = 0
c1Text = "No"
c2Text = "No"
c3Text = "No"
c4Text = "No"
footFill = 0


#Carly: GUI entry box that asks for user input:
    #the question:
stateInputLabel = Label(root, text = "What state do you live in?", font=("sylfaen", 35))
stateInputLabel.grid()
stateInputLabel.place(x = 750, y = 200, anchor="center")
    #the box itself:
stateNameInput = Entry(root, textvariable = name, bd = 5, width=50, relief="sunken", font=("sylfaen"))
stateNameInput.grid(column =1, row =1)
stateNameInput.place(x = 750, y = 270, anchor = "center", height= 50)


#Carly: function for the ENTER button to submit state name!
def enterButton():
    btn = tkinter.Button(text = 'ENTER', bd = 5, command=(lambda: btn_clicked()))
    btn.place(x = 750, y = 330, anchor = 'center')



#Carly:the function for the NEXT button that will
#pull up a request for the user's own electricity usage
def next1Button():
    btn2 = tkinter.Button(text = 'NEXT', bd = 5, command=(lambda: next_clicked()))
    btn2.place(x = 750, y = 535, anchor = 'center')


#Carly: the function for the NEXT button that will
#pull up the checkboxes for user's habits
def next2Button():
    btn3 = tkinter.Button(text = 'NEXT', bd = 5, command=(lambda: next2_clicked()))
    btn3.place(x = 750, y = 620, anchor = 'center')


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

