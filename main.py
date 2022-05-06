#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Read invited_names.txt and store it as list

with open("Input/Names/invited_names.txt", "r") as invited_name_v:
    list_of_names = invited_name_v.readlines()
with open("Input/Letters/starting_letter.txt", "r") as start_letter:
    contents_of_letter = start_letter.read()

invited_name = []

for list_name in range(0, len(list_of_names)):
    name = list_of_names[list_name].strip("\n")
    invited_name.append(name)
    output = contents_of_letter.replace("[name]", invited_name[list_name])
    with open(f"Output/ReadyToSend/{invited_name[list_name]}.txt", "w") as ready_output:
       ready_output.write(output)


