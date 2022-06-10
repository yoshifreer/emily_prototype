import PySimpleGUI as sg
category = ["Fast fashion", "Mid-tier", "Sustainable brand", "High end", "Handmade", "Upcycled", "Vintage"]
colours = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Black", "White", "Pink", "Silver", "Gold", "Brown"]
clothing_types = ["Pants", "Shirt", "Skirt", "Dress", "Outerwear", "Shorts"]
brands = ["Gucci", "Louis Vuitton", "H&M", "Other"]
sassy_message = "Input information about your clothing item and press 'Save and Calculate' to find out how sustainable you're being.."
sustainability_score = 0

def score(item_data):
    global sustainability_score
    global sassy_message
    # Calculate category score
    if item_data[0] == "Fast fashion":
        sustainability_score -= 1
    elif item_data[0] == "Mid-tier":
        sustainability_score += 1
    elif item_data[0] == "Sustainable brand":
        sustainability_score += 2
    elif item_data[0] == "Handmade":
        sustainability_score += 3
    elif item_data[0] == "Upcycled":
        sustainability_score += 3
    elif item_data[0] == "Vintage":
        sustainability_score += 3
    else:
        #print("invalid category")
        pass

    # Calculate time score
    time_modifier = float(item_data[1]) * 0.1
    sustainability_score = sustainability_score + time_modifier

    # Calculate materials
    if item_data[5] == True:
        sustainability_score -= 1
    if item_data[6] == True:
        sustainability_score -= 1
    if item_data[7] == True:
        sustainability_score -= 1
    if item_data[8] == True:
        sustainability_score -= 1
    if item_data[9] == True:
        sustainability_score += 2

    print(f"This item's sustainability score is: {sustainability_score}")
    if sustainability_score < -1:
        sassy_message = "A penguin just died because of you."
        print("A penguin just died because of you.")
    elif sustainability_score <= 0:
        sassy_message = "You're less evil than some people, I guess."
        print("You're less evil than some people, I guess.")
    elif sustainability_score <= 3:
        sassy_message = "Well done, you're being sort of responsible."
        print("Well done, you're being sort of responsible.")
    else:
        sassy_message = "You are....... SASSY!"
        print("You are....... SASSY!")


layout = [
    [sg.Text("Enter clothing data\n\n\n\n")],
    [sg.Text("Category: "), sg.Combo(category, "Category", key="-CATEGORY-")],
    [sg.Text("Time owned (in years, 0 for Brand New items): "),sg.InputText(size=(5,1), key="-TIMEOWNED-")],
    [sg.Text("Colour: "), sg.Combo(colours,"Colour", key="-COLOUR-"),],
    [sg.Text("Type: "), sg.Combo(clothing_types, "Type", key="-TYPE-")],
    [sg.Text("Brand: "), sg.Combo(brands, "Brand", key="-BRAND-")],
    [sg.Text("Materials: ")],
    [sg.Checkbox('Sequins/embellishments', default=False, key="-EMBELLISHMENTS-"),sg.Checkbox('Animal fur (real or faux)', default=False, key="-FUR-")],
    [sg.Checkbox('More than 2 fabric types', default=False, key="-MULTIPLEFABRICS-"),sg.Checkbox('Dyed/unorganic colour', default=False, key="-DYEDCOLOUR-")],
    [sg.Checkbox('Made from 1 material', default=False, key="-SINGLEMATERIAL-")],
    [sg.Button("Save and Calculate"), sg.Button("Quit")],
    [sg.Text("\nSassy Analysis:\n")],
    [sg.Text(sassy_message, key="-SASSYMESSAGE-", size=(50,10), background_color="black")]
]




window = sg.Window("SASSY! v1.0", layout, size=(500,700))

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == "Quit":
        break
    if event == "Save and Calculate":
        item_data = [values['-CATEGORY-'],values['-TIMEOWNED-'],values['-COLOUR-'],values['-TYPE-'],values['-BRAND-'],values['-EMBELLISHMENTS-'],values['-FUR-'],values['-MULTIPLEFABRICS-'],values['-DYEDCOLOUR-'],values['-SINGLEMATERIAL-']]
        clothing_database = open("clothing_database.txt","a")
        clothing_database.write(str(item_data)+"\n")
        clothing_database.close()
        print(item_data)
        score(item_data)
        sassy_message = sassy_message + "\n" + "Sustainability Score: " + str(sustainability_score)
        window['-SASSYMESSAGE-'].update(value=sassy_message)



window.close()

