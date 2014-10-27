
def NewRecipe ():
#This function asks the user to enter the details of a recipe

   recipename = input ("Please tell me the name of your recipe")
   recipeserves = input("How many does this serve?")

   #use the recipe name as the filename
   f = open(recipename,'w')

   #first line has the number served
   f.write (recipeserves + '\n')

   #Ask for new ingredients repeatedly until the users doesn't
   #say y to the question (case sensitive)
   more = "y"
   while (more == "y"):
       item = input("Item name")
       count = input("how much")
       units = input("What are the units?")

       #Add a comma delimited line for the ingredient
       f.write(item + ',' + count + ',' + units + '\n')
             
       more = input("more ingredients?")

   #Always close the file when you are done with it.
   f.close()

def ShowRecipe():
#This function displays the list of ingredients for a recipe
#with the quantities adjusted to serve the number specified.

   recipename = input ("What recipe would you like?")
   
   #assume the file has the recipe name and open for reading
   f = open(recipename,'r')
   recipeserves = int(f.readline())

   serve = int(input("How many people are coming?"))


   print ("you need:")

   #loop reading each ingredient in turn
   line = f.readline()
   while (line != ""):
       ingredient = line.split(",")
       item = ingredient[0]
       count = int(ingredient[1])
       units = ingredient[2]

       print ( (count/recipeserves) * serve, units, " of ", item)
       line = f.readline()

   #Always close the file when you are done with it.
   f.close()

#Main

choice = ""
while (choice != "q" and choice != "Q"):
    #Show the menu
    print ("   1 Enter the details of a new recipe")
    print ("   2 Show the ingredients of an existing recipe")
    print ("   q Quit this program\n\n")
    choice = input ("Please enter 1, 2 or q")

    if not (choice in ('1', '2', 'q', 'Q')):
           print ("Invalid input.")
    elif (choice == '1'):
           NewRecipe ()
    elif (choice == '2'):
            ShowRecipe()
           

