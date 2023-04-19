import csv
import matplotlib.pyplot as plt
import tkinter
from tkinter import *
from PIL import ImageTk, Image
import sv_ttk


'''This is the function for when the "ENTER" button
is clicked on the GUI.
-When the button is clicked, the state name that
the user has entered is compared against a file that
contains state names.
-A graph of all of the states' average monthly electricity
usage (also, within its own respective file)
is then pulled up with the user's state highlighted
on the graph.'''
def btn_clicked(): #all of btn_clicked() by Carly
    global stateName
    stateName = name.get() #retrieves the user's input of their state
    #read states file:
    legalNameStates = open('states.csv')
    avg_list_maker3 = csv.reader(legalNameStates) #converts States File into list of states
    for row in avg_list_maker3: #checking if the state input is in our States File
        if stateName not in row:
            stateInputLabel['text'] = 'Please input a valid state with the format: "State"'
            enterButton() #resets the ENTER button for a new state input if need be
        position = row.index(stateName)
        '''saves the index position of the entered state so that the
        correct state electricity usage can be pulled from the
        Usage File'''


    #formats State Electricity Usage File into list:
    usageList = open('newUsage.csv')
    avg_list_maker = csv.reader(usageList)
    usageList = []

    for row in avg_list_maker:  #ensures the data correctly gets put in list
        usage = row
        for num in row:
            finalNum = int(num)
            usageList.append(finalNum)


    '''Imports a file of state abbreviations and converts it
    to a list in order to later use the abbreviations as
    the labels for the x-axis on the graph of States' Monthly
    Avg Electricity Usage:'''
    statesList = open("stateAbbreviations.csv")
    avg_list_maker2 = csv.reader(statesList)

    for row in avg_list_maker2:  #ensures the data correctly gets put in list
        states = row


    '''Graphing the States' Monthly Avg Electricity Usage using
    state abbreviations list (states) as the x-axis values
    and the states' electricity usage (usageList) as the
    y-values'''
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
    label("ask4yours", root, f"Let's see how your electricity usage compares!", 35, 750, 460)

    '''Calls the NEXT button function so that the button
    appears and operates on the GUI; button opens new frame
    asking for user's personal energy usage'''
    next1Button()


#window 2: comparing user's electricity usage to state average
#base code by Nathan, GUI implementation by Carly
def next_clicked():
    global framePersonalUsage
    framePersonalUsage = Frame(root, width=1500, height=800)
    framePersonalUsage.grid()
    personalEnergy = tkinter.StringVar(framePersonalUsage)

    # main title
    mainTitle(framePersonalUsage)

    # Carly: GUI entry box that asks for user input:
    # the question:
    label("userEnergyLabel", framePersonalUsage, "What was your energy usage for this month?", 35, 750, 150)
    # the box itself:
    userEnergyInput = Entry(framePersonalUsage, textvariable=personalEnergy, bd=5, width=50, relief="sunken", font=("sylfaen"))
    userEnergyInput.grid(column=1, row=1)
    userEnergyInput.place(x=750, y=220, anchor="center", height=50)
    #energy units:
    label("units", framePersonalUsage, "kWh", 20, 1050, 220)


    #ENTER button that pulls up the comparison of the user's personal energy
    # usage to that of their state's:
    def enterButtonUserEnergy():
        btn3 = tkinter.Button(text='ENTER', bd=5, command=(lambda: PowerBill(stateName)))
        btn3.place(x=750, y=280, anchor='center')

    ''' written by Nathan = compares the user's personal energy usage
     to that of their state's so that they can get feedback on
     if they need to reduce their carbon footprint more'''
    def PowerBill(stateIn):
        #defining variables in function by different titles, so we could work
        #on code separately
        power1 = personalEnergy.get()
        power = int(power1)
        state = stateIn
        average = avgStateEnergy

        #reprinting label for state's energy use
        label("stateAvgUsageLabel", framePersonalUsage, (f"{state}'s Average Energy Usage: {average}kWh"), 35, 750, 350)

        #label for user's energy usage
        label("userUsageLabel", framePersonalUsage, (f"Your Average Energy Usage: {power}kWh"), 35, 750, 420)

        #comparing the user's personal energy usage to the state
        if power < average:
            label("comparisonLabel", framePersonalUsage, (f"Monthly Energy Usage of {power}kWh is lower than state average."), 30, 750, 490)
            label("congratsLabel", framePersonalUsage, (f"Good job! You are limiting CO2 output!"), 30, 750, 560)

        elif power > average:
            label("comparisonLabel", framePersonalUsage, (f"Caution! Monthly Power Usage of {power}kWh is higher than state average."), 30, 750, 490)
            label("fixLabel", framePersonalUsage, (f"Let's see what we can do to lower that usage!"), 30, 750, 560)

        else:
            label("comparisonLabel", framePersonalUsage, (f"Monthly Power Usage of {power}kWh is equal to state average."), 30, 750, 490)

        next2Button()
        framePersonalUsage.pack()

    enterButtonUserEnergy()


#Window 3: checkboxes of user's habits that provide carbon reducing feedback
#base code by Julia, GUI implementation by Carly
def next2_clicked():
    framePersonalUsage.destroy()
    frameHabits = Frame(root, width=1500, height=800)
    frameHabits.grid()
    frameHabits.tkraise()

    # main title
    mainTitle(frameHabits)

    # instructions for the checkboxes
    label("instructionsLabel", frameHabits, "Check the boxes of habits that you do!", 35, 750, 150)
    label("basedLabel", frameHabits, "We'll give you some feedback on how to reduce your energy usage based on your answers.", 25, 750, 220)
    frameHabits.pack()

    #empty foot as base image
    foot(r'IMG_1041.PNG', frameHabits)

    #checkbox feedback
    def c1_On(xValue, yValue, button, feedbackPhrase):
        global footFill
        global c1Text
        habit1feedback = Label(frameHabits,
                               text="",
                               font=("sylfaen", 14))
        habit1feedback.grid()
        habit1feedback.place(x=xValue+400, y=yValue)

        '''based on how many checkboxes are checked, 
        the foot is filled accordingly (trying to reduce carbon footprint)'''
        def footfill():
            if footFill == 0:
                foot(r'IMG_1041.PNG', frameHabits)
            elif footFill == 1:
                foot(r'IMG_1042.PNG', frameHabits)
            elif footFill == 2:
                foot(r'IMG_1043.PNG', frameHabits)
            elif footFill == 3:
                foot(r'IMG_1044.PNG', frameHabits)
            else:
                foot(r'IMG_1045.PNG', frameHabits)

        '''tkinter doesn't allow size changes of traditional checkboxes,
        so I had to make them out of regular buttons with labels'''
        if button['text']=='x':
            footFill -= 1
            button['text']=''
            habit1feedback['text'] = "  " * len(feedbackPhrase)
            footfill()

        else:
            footFill += 1
            button['text']='x'
            habit1feedback['text'] = feedbackPhrase
            footfill()

    #1st checkbox
    global c1Text
    c1 = tkinter.Button(text=c1Text, font = tkinter.font.Font(size=15), bd=5, command=(lambda: c1_On(10,325,c1,'- Remember to shut your lights off when you '
                                                                             'leave that room or your house.')), height = 1, width = 3)
    c1.place(x=300, y=300, anchor='center')
    label("c1QuestionLabel", frameHabits, 'Do you always leave your lights on?', 25, 595, 295)


    #2nd checkbox
    global c2Text
    c2 = tkinter.Button(text=c2Text, font = tkinter.font.Font(size=15), bd=5, command=(lambda: c1_On(10, 425, c2,'- Try shutting them off when you leave the'
                                                                              ' room; open a window instead for a breeze;'
                                                                              ' close your curtains to block heat from sun.')), height=1, width=3)
    c2.place(x=300, y=400, anchor='center')
    label("c2QuestionLabel", frameHabits, 'Do you keep fans running?', 25, 535, 395)


    # 3nd checkbox
    global c3Text
    c3 = tkinter.Button(text=c3Text, font = tkinter.font.Font(size=15), bd=5, command=(lambda: c1_On(10, 525, c3, '- Make sure your faucets are turned all '
                                                                               'the way off after you use them; turn your water off when you '
                                                                                 'brush your teeth.')), height=1, width=3)
    c3.place(x=300, y=500, anchor='center')
    label("c3QuestionLabel", frameHabits, 'Do you leave your water running?', 25, 585, 495)


    # 4th checkbox
    global c4Text
    c4 = tkinter.Button(text=c4Text, font = tkinter.font.Font(size=15), bd=5, command=(lambda: c1_On(10, 625, c4, '- When not using appliances, shut them off'
                                                                               ' instead of letting them run all day for convenience.')), height=1, width=3)
    c4.place(x=300, y=600, anchor='center')
    label("c4QuestionLabel", frameHabits, 'Do you leave nonessential appliances on (coffee maker, lamps, etc.)?', 25, 815, 595)
    frameHabits.pack()

    '''Carly: the function for the NEXT button that will
    pull up the final summary window'''
    def finishedButton():
        btn4 = tkinter.Button(text='DONE', bd=5, command=(lambda: finished_clicked()))
        btn4.place(x=750, y=700, anchor='center')

    #Carly: window 4: summary of carbon reduction message
    def finished_clicked():
        frameHabits.destroy()
        finishFrame = Frame(root, width=1500, height=800)
        finishFrame.grid()
        finishFrame.tkraise()

        # main title
        mainTitle(finishFrame)

        # summary:
        label("thankYouLabel", finishFrame, "Thank you for seeing what you can "
                                                "\ndo to reduce your carbon footprint!", 40, 750, 200)
        finishFrame.pack()

        label("awarenessLabel", finishFrame, "Awareness through small adjustments "
                                                 "\nis the first step to greater change!", 30, 750, 365)
        finishFrame.pack()


        #feet pics
        foot(r'IMG_1045.PNG', finishFrame, 500, 600)
        foot(r'IMG_1041.PNG', finishFrame, 1000, 600)

        arrow = Label(finishFrame, text="--->", font=("sylfaen", 35), fg="grey")
        arrow.grid()
        arrow.place(x=750, y=600, anchor="center")

        rect = Canvas(finishFrame, width=250, height=200)
        rect.create_rectangle(500, 500, 800, 800, fill='grey', outline='grey')

    finishedButton()

#label function to reduce code for GUI text:
def label(labelTitle, frame, text, fontSize, x, y, font="sylfaen"):
    labelTitle = Label(frame, text=text, font=(font, fontSize))
    labelTitle.grid()
    labelTitle.place(x=x, y=y, anchor="center")

#label fuction for main title specifically:
def mainTitle(frame):
    label("underline", frame, "_____________________________________________", 45, 750, 70, "Castellar")
    label("titleLabel", frame, "Let's reduce your carbon footprint!", 45, 750, 50, "Castellar")

#function for opening and resizing the feet pics:
def foot(image, frame, x=150, y=450):
    img = Image.open(image)
    imageResize = img.resize((300, 300), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(imageResize)

    imageLabel = Label(frame, image=image)
    imageLabel.image = image
    imageLabel.place(x=x, y=y, anchor="center")

#function for the ENTER button to submit state name!
def enterButton():
    btn = tkinter.Button(text = 'ENTER', bd = 5, command=(lambda: btn_clicked()))
    btn.place(x = 750, y = 330, anchor = 'center')

#the function for the NEXT button that will
#pull up a request for the user's own electricity usage
def next1Button():
    btn2 = tkinter.Button(text = 'NEXT', bd = 5, command=(lambda: next_clicked()))
    btn2.place(x = 750, y = 535, anchor = 'center')

#the function for the NEXT button that will
#pull up the checkboxes for user's habits
def next2Button():
    btn3 = tkinter.Button(text = 'NEXT', bd = 5, command=(lambda: next2_clicked()))
    btn3.place(x = 750, y = 620, anchor = 'center')


#GUI base
root = tkinter.Tk()
sv_ttk.set_theme('dark')
root.title('GUI')
root.geometry('1500x800')

#GUI intro title --> tells the user what the program is going to do:
mainTitle(root)

'''Empty GUI label for the print statement of the state energy usage.
I made this so that if the user wants to try to input different states,
the print statement saying the energy usage will actually change rather
than printing another label on top.'''
avgStateUsage = Label(root, text=f"", font=("sylfaen", 35))
avgStateUsage.grid()
avgStateUsage.place(x=750, y=390, anchor="center")

#declaring string variable for storing stateName
name = tkinter.StringVar(root)
avgStateEnergy = None
stateName = None
framePersonalUsage = None
value = 0
c1Text = ""
c2Text = ""
c3Text = ""
c4Text = ""
footFill = 0

#GUI entry box that asks for user input:
    #the question:
stateInputLabel = Label(root, text = "What state do you live in?", font=("sylfaen", 35))
stateInputLabel.grid()
stateInputLabel.place(x = 750, y = 200, anchor="center")
    #the box itself:
stateNameInput = Entry(root, textvariable = name, bd = 5, width=50, relief="sunken", font=("sylfaen"))
stateNameInput.grid(column =1, row =1)
stateNameInput.place(x = 750, y = 270, anchor = "center", height= 50)


#calls the ENTER button function so that the button
# appears and operates on the GUI to submit state name
enterButton()

#makes sure the window displays in an infinite loop
# until closed out by user
root.mainloop()


