
############################################################
# - Murder on Mason Street
# - by Ben Fox, Babak Rezai, James O'Dea, Caroline Lancaster
# - text based adventure game
# - CST205 2014: Lab 11
############################################################

def gamePlay():
  currentLocation = 7 
  choice=requestString("""Welcome to Murder on Maston Street,
    In each room you will be told which directions you can go, '
    You'll be able to go forward, backward, right, or left by typing that direction "
    Type help to redisplay this introduction 
    Type exit to quit at any time.
     
    Good evening detective, quite the night for a murder mystery, eh?
    We have a body,face down in the bedroom. The storm knocked the power 
    out so watch your step. If you need anything let me know.
    Do you wish to go forward, backward right or left?""")
  movement(currentLocation,choice)
    
def movement(currentLocation,choice):
  while choice in ('forward','backward','right','left','eat','move','use','help','listen','solve','look','exit'):
    if currentLocation == 1 and choice == 'backward':
        print ('okay, you move ' + choice)
        bedRoom()
    if currentLocation == 2 and choice == 'backward':
        livingRoom() 
        print ('okay, you move ' + choice)
    if currentLocation == 3 and choice  == 'forward':
        print ('okay, you move ' + choice)
        bathRoom()
    if currentLocation == 3 and choice  == 'right':
        print ('okay, you move ' + choice)
        livingRoom()
    if currentLocation == 4 and choice  == 'forward':
        print ('okay, you move ' + choice)
        garage()
    if currentLocation == 4 and choice  == 'right':
        print ('okay, you move ' + choice)
        kitchen()
    if currentLocation == 4 and choice  == 'left':
        print ('okay, you move ' + choice)
        bedRoom() 
    if currentLocation == 4 and choice  == 'backward':
        print ('okay, you move ' + choice)
        porch()     
    if currentLocation == 5 and choice  == 'left':
        print ('okay, you move ' + choice)
        livingRoom()        
    if currentLocation == 6 and choice  == 'right':
        print ('okay, you move ' + choice) 
        porch()  
    if currentLocation == 7 and choice  == 'left':
        print ('okay, you move ' + choice)
        lawn()   
    if currentLocation == 7 and choice  == 'forward':
        print ('okay, you move ' + choice)   
        livingRoom() 
    if currentLocation == 7 and choice  == 'right':
        print ('okay, you move ' + choice)   
        window()  
    if currentLocation == 7 and choice  == 'backward':
        print ('okay, you move ' + choice)
        street()    
    if currentLocation == 8 and choice  == 'left':
        print ('okay, you move ' + choice)  
        porch()
    if currentLocation == 9 and choice  == 'forward':
        print ('okay, you move ' + choice) 
        porch()   
    if currentLocation == 5 and choice == 'eat':
        print ('okay, detective, you need ' + choice) 
        sandwich(currentLocation)
    if currentLocation == 3 and choice == 'move':
        print ('okay, detective, you need ' + choice) 
        moveBody(currentLocation)
    if currentLocation == 1 and choice.lower().startswith("u"):
        print ('okay, detective, you need ' + choice) 
        toilet(currentLocation)
    if choice.lower().startswith("sol"):
        print ('okay, detective, you think you ' + choice + 'it') 
        solved(currentLocation)
    if choice.lower().startswith("hel"):
        help(currentLocation)
    if choice.lower().startswith("loo"):
        look(currentLocation)
    elif choice == "exit":
       print ("Okay detective, you need a break.") 
    break;
    tryAgain(currentLocation)

    
def bathRoom():
  currentLocation = 1 
  choice=requestString("""The bathroom is clean and tidy just as the rest of the home. 
  On the floor lies an open bottle of tums with the contents strewn across the floor. 
  They are the mint kind, yuck! You can move backward.""")
  movement(currentLocation,choice)

def garage():
  flashlight = 0
  currentLocation = 2 
  choice=requestString("""You\'ve entered the garage. It is quiet except for the feint sound of 
  rain on the roof above. It smells of gasoline, exhaust and yard clippings in 
  here. On the wall is a collection of tools all hung in spots with outlines to 
  insure proper placement. One tool appears to be missing and the outline is that 
  of a large adjustable wrench. A fliashlight lies on the workbench You can move backward""")
  if choice == "take":
    flashlight = 1
    print("you take the flashlight.")
  else 
  movement(currentLocation,choice)

def bedRoom():
  currentLocation = 3 
  choice=requestString("""You stand in a dark bedroom. The bed is still made and a body lies 
  face-down on the floor. There does not appear to have been a struggle and 
  no marks are visible on the body. You can move forward or right.""")
  movement(currentLocation,choice)
  
def livingRoom():
  currentLocation = 4 
  choice=requestString("""You stand in silence, listening to the rain as blue and red flashes of light from the squad 
  cars outside play blinding games on the walls of the living room. You notice a clock stopped at 10:57 
  on the wall and the smell of standing water assaults your nose. There is a door to the forward, an 
  entry to the kitchen to your right and a door to the left. You can move forward, backward, right or left.""")
  if choice == "move":
    secretRoom()
  else:
  movement(currentLocation,choice)

def kitchen():
  currentLocation = 5 
  choice=requestString("""The kitchen is immaculate with the exception of a half-eaten 
  sandwich on the counter. A cat clock on the wall swings its tail and 
  eyes to the passing of time. On the refrigerator are pictures held to 
  the surface by various magnets. A window looking out onto the street 
  is broken but the floor under the window is spotless. You can move left.""")
  
  movement(currentLocation,choice)
  
def lawn():
  currentLocation = 6
  choice=requestString("""You are on the front lawn of the home. It is nicely manicured 
  and a small garden gnome stares happily into the dark, rainy night. You can move right.""")
  movement(currentLocation,choice)
  
def porch():
  currentLocation = 7
  choice=requestString("""...You stand back on the porch of a small home in a suburb of Los Angeles. 
    It is cold and rainy and to the forward is a dark living room. 
    An officer stands next to you writing on a notepad. You can move forward, backward, right or left.""")
  movement(currentLocation,choice)

def window():
  currentLocation = 8
  choice=requestString("""You stand to the right (right) of the porch in a muddy planter. 
  The window above the planter is broken and markers placed by the officers 
  here before you indicate foot prints made in the mud under the window were 
  made by boot-covered feet. There is glass pieces scattered in the mud. 
  You can move left.""")
  movement(currentLocation,choice)
  
def street():
  currentLocation = 9
  choice=requestString("""There is nothing here but cold rain and parked squad cars with lights flashing. 
  It?s too early in the morning for anyone to be out but you do notice a few people peeking out 
  from behind drawn curtains of neighborhood homes. The officers you met here said they 
  interviewed everyone and no one saw or heard anything. You can move forward.""")
  movement(currentLocation,choice)
  
def secretRoom():
 currentLocation = 10
 if flashlight == 1:
   choice=printNow("""You enter a dark secret room.You flick on the flashlight you took 
from the garage and are horrified to see body parts hanging throughout the room.
The smell of standing water and rotting flesh turns your stomach. You race back upstairs to vomit.""")
 else:
   choice=printNow("You enter a dark secret room. It is pitch black in here and you can't see a thing.")
 movement(currentLocation,choice)

def sandwich(currentLocation):
  choice=requestString('Don\'t eat that, it\'s poisoned!!!')
  movement(currentLocation,choice)

def moveBody(currentLocation):
  choice=requestString("""When you move the body, it lets out a long breathy sigh. 
  You jump back initially but realize it is just air escaping the body. 
  There are no other signs of foul play on this body and the eyes of a 
  middle-aged man stare blankly up at you. """)
  movement(currentLocation,choice)
  
def toilet(currentLocation):
  choice=requestString("Ahh, much better! Now What?")
  movement(currentLocation,choice)

def poison():
  printNow("You did it! Congratulations! Now, who the hell did perpetrated this horrible crime\?")
  
def solved(currentLocation):
  choice=requestString("You figured out what happened, eh? Well, how was this person murdered\?")
  while choice in ("poison"):
    if currentLocation == 1 and choice == "poison":
        poison()
    tryAgain(currentLocation)

def moveBody(currentLocation):
  choice=requestString("""When you move the body, it lets out a long breathy sigh. 
  You jump back initially but realize it is just air escaping the body. 
  There are no other signs of foul play on this bod""")

def tryAgain(currentLocation):
  choice=requestString('Invalid choice Detective, you must start over. Enter Yes to Play again or No to Quit')
  if choice.lower().startswith("y"):
    gamePlay()
  if choice.lower().startswith("n"):
    print('Goodbye Detective')
 
  
        
def help(currentLocation):
  choice=requestString("""You can try: 
    forward
    backward
    right
    left
    eat
    look
    
    pick
    use
    move
    help
    exit
    solve, so now what?""")
  movement(currentLocation,choice)    
