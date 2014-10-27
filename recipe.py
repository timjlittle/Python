recipe = []
recipename = ""
recipeserves = 0

def NewRecipe ():
#This function asks the user to enter the details of a recipe

   recipename = input ("Please tell me the name of your recipe")
   recipeserves = input("How many does this serve?")

   f = open(recipename,'w')
   f.write (recipeserves + '\n')

   #Ask for new ingredients repeatedly until the users doesn't
   #say y to the question (case sensitive)
   more = "y"
   while (more == "y"):
       item = input("Item name")
       count = input("how much")
       units = input("What are the units?")

       #Add a dynamically created list containing the ingredient name,
       # how many and what the units are to the recipe list
       f.write(item + ',' + count + ',' + units + '\n')
       recipe.append([item, count, units] )
       
       more = input("more ingredients?")

   
   f.close()

def ShowRecipe():
#This function displays the list of ingredients for a recipe
#with the quantities adjusted to serve the number specified.
   serve = int(input("How many people are coming?"))


   print ("you need:")
   for ingredient in recipe:
       item = ingredient[0]
       count = ingredient[1]
       units = ingredient[2]

       print ( (count/recipeserves) * serve, units, " of ", item)

#Main

choice = ""
while (choice != "q" and choice != "Q"):
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
           
