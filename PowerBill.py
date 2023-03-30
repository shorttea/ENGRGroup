def PowerBill(stateIn, powerIn, nameIn, yn, requestIn):
    state = stateIn
    user_name = nameIn
    average = 0
    f = open("WrittenPowerBill.txt", "w")
    f.write(f'Customer Name:\n{user_name}')
    f.write("\n-------------------------------------------------------"
            "-----------------------------------------------------------------------------------------------------\n")
    rf = open("StatesandPower.txt", "r")
    lines = rf.read()
    sparse_lines = lines.split()
    print(sparse_lines)
    power = powerIn
    request = requestIn

    if state in sparse_lines:
        average = sparse_lines[sparse_lines.index(state) + 1]
    f.write(f'{state}\nAvg. Power Usage {average}kWt.')
    f.write("\n")
    if power < average:
        f.write(f'Monthly Power Usage of {power} is lower than state average')
        f.write(f'Good job, you are limiting CO2 output')
    elif power > average:
        f.write(f'Caution! Monthly Power Usage of {power} is higher than state average')
    else:
        f.write(f'Monthly Power Usage of {power} is equal to state average')
    if yn == "yes":
        f.write(f'\n\nREMINDER\n
       ------------------------------------------------------------------------------------------------------------------------------------------------------------\n
        Reminder to turn off {request}. Doing so will reduce your power usage and limit your CO2 output')

