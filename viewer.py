import PySimpleGUI as sg
clothes_list = []

def score(item_data):
    sustainability_score = 0.0
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
        print("invalid category")

    # Calculate time score
    time_modifier = float(item_data[1]) * 0.1
    # print(f"time modifier: {time_modifier}")
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
        print("A penguin just died because of you.")
    elif sustainability_score <= 0:
        print("You're less evil than some people, I guess.")
    elif sustainability_score <= 3:
        print("Well done, you're being sort of responsible.")
    else:
        print("You are....... SASSY!")

def load_database():
    # clothing_database = open('clothing_database.txt', 'r')
    # for lines in clothing_database:
    #     clothes_list.append(lines)#.rstrip('\n'))#.split(','))
    with open('clothing_database.txt') as file:
        lines = file.readlines()
    new_lines = []
    for x in range(len(lines)):
        stripped = lines[x].replace('[','').replace(']','').replace("'",'')
        new_lines.append(stripped)
        split = new_lines[x].split(", ")
        for x in range(len(split)):
            print(split[x])
    # stripped = lines[1].replace('[', '')
    # new_lines.append(stripped)
    #print(new_lines)
    #print(clothes_list)


layout = [
    [sg.Text("Enter clothing data")],
    [sg.Text("")]
    # [sg.Text("Category: "), sg.Combo(category, "Category", key="-CATEGORY-")],
    # [sg.Text("Time owned (in years, 0 for Brand New items): "),sg.InputText(size=(5,1), key="-TIMEOWNED-")],
    #
    [sg.Button("Load"), sg.Button("Quit")]
]



window = sg.Window("SASSY! Viewer v1.0", layout, size=(600, 400))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Quit":
        break
    if event == "Load":
        load_database()
#        item_data = [values['-CATEGORY-'],values['-TIMEOWNED-'],values['-COLOUR-'],values['-TYPE-'],values['-BRAND-'],values['-EMBELLISHMENTS-'],values['-FUR-'],values['-MULTIPLEFABRICS-'],values['-DYEDCOLOUR-'],values['-SINGLEMATERIAL-']]
#         clothing_database = open("clothing_database.txt","a")
#         clothing_database.write(str(item_data)+"\n")
#         clothing_database.close()
#         print(item_data)
#         score(item_data)



window.close()

