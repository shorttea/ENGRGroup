
# lists of northern and southern states
northernStates = ['Alaska', 'Washington', 'Oregon',
                  'Idaho', 'Minnesota', 'North Dakota',
                  'South Dakota', 'Wyoming', 'Montana', 'Wisconsin',
                  'Michigan', 'Nevada', 'Utah', 'Colorado',
                  'Nebraska', 'Iowa', 'Illinois', 'Indiana',
                  'Missouri', 'Kansas', 'Ohio', 'West Virginia',
                  'Pennsylvania', 'Maryland', 'New Jersey', 'Connecticut',
                  'New York', 'Rhode Island', 'Massachusetts',
                  'New Hampshire', 'Vermont', 'Maine']
southernStates = ['California', 'Arizona', 'New Mexico', 'Texas',
                  'Oklahoma', 'Arkansas', 'Louisiana', 'Mississippi',
                  'Kentucky', 'Tennessee', 'Alabama', 'Virginia',
                  'North Carolina', 'South Carolina', 'Georgia',
                  'Florida']

# Repeat until the user enters a valid state
while true:
    # Get the user's state
    state = input("What state do you live in? ")
    # Variable will be used to curate power reduction tips to the user
    user_region = ""

    if state in northernStates:
        user_region = "N"
        break

    elif state in southernStates:
        user_region = "S"
        break

    else:
        print("Please input a valid state")

print("Done.")