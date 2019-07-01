import json
allusers_data = []
keys = ["name", "birthday", "age", "city"]
questions = ["What is your name? ", "What is your date of birth? (MM/DD/YY) ", "What is your age? ", "What city are you from? " ]
answering = input("would you like to answer  a survey? yes or no: ")

#Extend your program from Part 1 
while answering == "yes" or new_user == "yes":      
    user_data = {}
    for i in range(len(keys)):

        user_answer = input(questions[i])
        user_data[keys[i]] = user_answer
        answering = input("would you like to keep answering? yes or no: ")
        if answering == "no":
            break
    new_user = input("are you still collecting responses? ")  
    allusers_data.append(user_data)
        
# collects responses to the survey questions from more than one user
# saves all responses as a list of dictionaries


#prompt the user to say whether they’d like to continue collecting responses.

f = open("data.json", "r")
olddata = json.load(f)
allusers_data.extend(olddata)
f.close()

with open("data.json", 'w+') as outfile:
    json.dump(allusers_data, outfile,)

#for i in range(len(allusers_data)):
#    jsonfile = allusers_data[i]
#    dictionaryToJson = json.dumps(jsonfile)
#print(allusers_data)