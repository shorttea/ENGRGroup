# Creating a dictionary of states and their respective average electricity rates
electricity_rates = {'Alabama': 11.24,
                     'Alaska': 22.04,
                     'Arizona': 12.03,
                     'Arkansas': 9.83,
                     'California': 20.57,
                     'Colorado': 12.45,
                     'Connecticut': 21.46,
                     'Delaware': 12.49,
                     'Florida': 11.50,
                     'Georgia': 11.63,
                     'Hawaii': 33.53,
                     'Idaho': 10.22,
                     'Illinois': 13.63,
                     'Indiana': 11.62,
                     'Iowa': 12.03,
                     'Kansas': 12.73,
                     'Kentucky': 11.27,
                     'Louisiana': 9.55,
                     'Maine': 17.16,
                     'Maryland': 15.29,
                     'Massachusetts': 21.14,
                     'Michigan': 15.50,
                     'Minnesota': 13.55,
                     'Mississippi': 11.12,
                     'Missouri': 10.94,
                     'Montana': 10.28,
                     'Nebraska': 11.81,
                     'Nevada': 12.10,
                     'New Hampshire': 19.67,
                     'New Jersey': 16.65,
                     'New Mexico': 12.03,
                     'New York': 19.23,
                     'North Carolina': 11.49,
                     'North Dakota': 11.19,
                     'Ohio': 12.29,
                     'Oklahoma': 10.50,
                     'Oregon': 11.33,
                     'Pennsylvania': 14.19,
                     'Rhode Island': 19.09,
                     'South Carolina': 12.53,
                     'South Dakota': 11.82,
                     'Tennessee': 10.93,
                     'Texas': 11.65,
                     'Utah': 9.81,
                     'Vermont': 18.11,
                     'Virginia': 11.08,
                     'Washington': 9.52,
                     'West Virginia': 11.82,
                     'Wisconsin': 13.17,
                     'Wyoming': 11.42
                     }

# Getting user input
state = input("What state do you live in? ")
electric_device = input("Do you tend to leave any electrical devices running in your home? (Yes/No) ")

# Checking if the state entered by the user is valid
if state not in electricity_rates.keys():
    print("Invalid state entered. Please enter a valid U.S. state.")
else:
    # Retrieving the average electricity rate for the user's state
    avg_electricity_rate = electricity_rates[state]

    # Suggesting solutions based on the user's input
    if electric_device.lower() == "yes":
        print("Here are some solutions for reducing your electricity bill and carbon footprint:")
        print("- Turn off all electrical devices when not in use.")
        print("- Unplug chargers when not in use.")
        print("- Use power strips to turn off multiple devices at once.")
        print("- Switch to energy-efficient light bulbs and appliances.")
        print(f"- Adjust")
