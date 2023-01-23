
# function that computes the overall score

def compute_mark():    
    
    tilawa_count=0 # variable to hold tilawa mistake
    tadbiq_count=0 # variable to hold tadbiq mistake
    total_score=0  # variable to hold the total score
    

    category=input("Enter participant category: ") # getting participant category
    category_list=["60", "40", "20", "10", "5"]

    while True : # checking for valid response
        if category in category_list:
            break
        else :
            print ("Your response is not a valid category ")
            category=input("Enter participant category: ")

       
    
    p_name=input("Enter participant name: ")  #participant_name
    while True:
        if (len(p_name) !=0) and p_name.isdecimal() is False:
            break
        else:
            print("enter a valid anme please")
            p_name=input("Enter participant name: ")

              
    user_input=input("Enter .. for tilawa . for tadbiq or y if done ")

    
# while loop that keeps prompting the judge to record the mistakes
    while True:
        if user_input=="y":
            break
        elif user_input=="..":
            tilawa_count+=1
            user_input=input("Enter .. for tilawa . for tadbiq or y if done ")
            
        elif user_input==".":
            tadbiq_count+=0.5
            user_input=input("Enter .. for tilawa . for tadbiq or y if done ")
        else:
            print("enter valid response please !")
            user_input=input("Enter .. for tilawa . for tadbiq or y if done ")

            
    print ("First section done \n")
    # print()
    
   

    p_saut=str(input("Enter saut mark: "))  # variable to hold mark for sound
    p_saut_values=["5","6","7","8","9","10"] # range mark for saut
    
    while True:
        if (len(p_saut) !=0) and p_saut.isdecimal() is True and (p_saut in p_saut_values):
            break
        else:
            print("enter a valid saut mark please")
            p_saut=str(input("Enter saut mark: "))

    
    
    p_dress=str(input("Enter dress mark: ")) # variable to hold mark for dress
    p_dress_values=["5", "6", "7", "8", "9", "10"] # range mark for saut

    while True:

        if  (len(p_dress)!=0) and p_dress.isdecimal() is True and p_dress in p_dress_values :
            break
        else:
            print("enter a valid dress mark  please")
            p_dress=input("Enter dress mark please : ")




    # computing total score for participant
    total_score=80-(tilawa_count+tadbiq_count) + int(p_dress) + int(p_saut)


    #write to file after computing and save
    if category=="60":
        
        with open ("sixty_hizb.txt", "a") as f:
            f.write("Total Score  for participant {} in category {} is {} ".format(p_name,category, total_score) + "\n")

    elif category=="40":
        
        with open ("forty_hizb.txt", "a") as f:
            f.write("Total Score  for participant {} in category {} hizb is {}".format(p_name,category, total_score) + "\n")

    elif category=="20":
        
        with open ("20_hizb.txt", "a") as f:
            f.write("Total Score  for participant {} in category {} hizb is {}".format(p_name,category, total_score) + "\n")

    elif category=="10":
        
        with open ("ten_hizb.txt", "a") as f:
            f.write("Total Score  for participant {} in category {} hizb is {}".format(p_name,category, total_score) + "\n")


    elif category=="5":
        
        with open ("five_hizb.txt", "a") as f:
            f.write("Total Score  for participant {} in category {} hizb is {}".format(p_name,category, total_score) + "\n")


    #display result result

    print("Total tilawa count is {}".format(tilawa_count))
    print("Total tadbiq count is {}".format(tadbiq_count))
    print("Dress mark is {}".format(p_dress))
    print("Saut Mark {}".format(p_saut))
    print("Total Score  for participant {} in category {} hizb is {}".format(p_name,category, total_score))


# loop to restart the program after computing

response="y"

while response=="y":
    
    compute_mark()
    response=input("do you want to compute again? (y or n)")
        


