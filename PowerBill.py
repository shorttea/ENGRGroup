def PowerBill(stateIn, powerIn, nameIn, yn, requestIn):
    #sets user state and name and creates average variable for later assignment
    state = stateIn
    user_name = nameIn
    average = 0
    #opens WrittenPowerBill file so prepare for creating user's power bill
    f = open("WrittenPowerBill.txt", "w")
    #Writes set up for user power bill by printing the user name and separating the header from the rest of the bill
    f.write(f'Customer Name:\n{user_name}')
    f.write("\n-------------------------------------------------------"
            "-----------------------------------------------------------------------------------------------------\n")
    #opens file with state names and average power use to read
    rf = open("StatesandPower.txt", "r")
    lines = rf.read()
    sparse_lines = lines.split()
    
    #sets power to powerIn and user request to request in
    power = powerIn
    request = requestIn
    
    # if the input state is in the list of states, then it sets average to that state's average
    if state in sparse_lines:
        average = sparse_lines[sparse_lines.index(state) + 1]
        
    #writes the states average power use for visual comparison
    f.write(f'{state}\nAvg. Power Usage {average}kWt.')
    f.write("\n")
    
    #checks if user power usage is above, below, or equal to state's average and writes message accordingly
    if power < average:
        f.write(f'Monthly Power Usage of {power} is lower than state average')
        f.write(f'Good job, you are limiting CO2 output')
    elif power > average:
        f.write(f'Caution! Monthly Power Usage of {power} is higher than state average')
    else:
        f.write(f'Monthly Power Usage of {power} is equal to state average')
        
    #If the user set a reminder, write what the user wanted to be reminded of
    if yn == "yes":
        f.write(f'\n\nREMINDER\n
       ------------------------------------------------------------------------------------------------------------------------------------------------------------\n
        Reminder to turn off {request}. Doing so will reduce your power usage and limit your CO2 output')

