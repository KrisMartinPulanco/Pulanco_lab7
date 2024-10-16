name=input("What is you name:")
section=input("What is your section:")
prelim=float(input("Prelim grade:"))
if 40<=prelim<=100:
    midterm=float(input("Midterm grade:"))
if 40<=midterm<=100:
    finals=float(input("Final grade:"))
    if 40<=finals<=100:
        totalgrade=prelim+midterm+finals
        finalgrade=round(totalgrade/3)
        displayfinalgrade=str(finalgrade)
        if finalgrade<75:
            print("Final grade:", displayfinalgrade)
            print("Grade points: 5.0")
            print("Percentage equivalent : 75%")
            print("General description: failed")
        elif 77>=finalgrade>=75:
            print("Final grade",  displayfinalgrade)
            print("Grade point: 3.00")
            print("Percentage equivalent: 75-77%")
            print("General description: passed")
        elif 80>=finalgrade>=78:
            print("Final grade:",  displayfinalgrade)
            print("Grade point: 2.75")
            print("Percentage equivalent: 80-89%")
            print("General description: fair")
        elif 83>=finalgrade>=81:
            print("Final grade:",  displayfinalgrade)   
            print("Grade point: 2.50")
            print("Percentage equivalent: 81-83%")
            print("General description: fairly satisfactory")
        elif  86>=finalgrade>=84:
            print("Final grade:",  displayfinalgrade)
            print("Grade point: 2.25")
            print("Percentage equivalent: 84-86%")
            print("General description: excellent!")
        elif 89>=finalgrade>=87:
            print("Final grade:",  displayfinalgrade)
            print("Grade point: 2.00")
            print("Percentage equivalent: 87-89%")
            print("General description: good!")
        elif 92>=finalgrade>=90:
            print("Final grade:",  displayfinalgrade)
            print("Grade point: 1.75")
            print("percantage  equivalent: 90-92%")
            print("General description: very good!")
       
        elif 95>=finalgrade>=93:
            print("Final grade:",  displayfinalgrade)
            print("Grade point: 1.50")
            print("Percantage  equivalent: 93-95%")
            print("General description: superior!")
        elif 98>=finalgrade>=96:
            print("Final grade:",  displayfinalgrade)
            print("Grade point: 1.25")
            print("Percentage equivalent: 96-98%")
            print("General description: outstanding!")
        elif 100>=finalgrade>=99:
            print("Final grade:", displayfinalgrade)
            print("Grade point: 1.0")
            print("Percantage equivalent: 99-100%")
            print("General description: Excellent")
        else:
            print("Invalid grade")
    else:
        print("Invalid input, please enter a valid grade")
else:
    print("Invalid input, please enter a valid grade")

