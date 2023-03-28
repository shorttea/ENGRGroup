def main(stateIn, powerIn, nameIn, yn, requestIn):
    state = stateIn
    user_name = nameIn
    average = 0
    f = open("WrittenPowerBill.txt", "w")
    f.write(f'Customer Name\n{user_name}.')
    f.write("\n//////////////////////////////////////////////////////////////")
    rf = open("StatesandPower.txt", "r")
    lines = rf.read()
    sparse_lines = lines.split()
    print(sparse_lines)
    while state not in sparse_lines:
        if state not in sparse_lines:
            print("Please enter valid state")
        else:
            power = powerIn

    if state in sparse_lines:
        average = sparse_lines[sparse_lines.index(state) + 1]
    f.write(f'Average power usage per month in {state} is {average}kWt.')
    f.write("\n")
    if power < average:
        f.write(f'Good job, your average monthly power of {power}kWt is lower than the state average.')
        f.write(f'You are helping the environment and helping limit global warming.')
    elif power > average:
        f.write(f'Caution! Your monthly average power use of {power}kWt is higher than the state average. Remember to '
                f'turn off any unused devices to help save power.')
    else:
        f.write(f'Your monthly power use is the same as the monthly average. Although this is good, we still '
                f'encourage you to save power by turning off appliances that remain on.')
    if yn == "yes":
        request = requestIn
        f.write(f'REMINDER\nYou have requested a reminder to turn off {request}. Doing so will reduce your power '
                f'usage and limit your CO2 output')

