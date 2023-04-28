
#### Add Import Statement(s) as needed ####
from modules import pattern 
#### End Add Import Statement(s) ####

def main():
    # Setup pattern
    pattern.setup()

    # Play again loop
    playAgain = True

    while playAgain:
        # Present a menu to the user
        # Let them select mode
        print("Choose a mode")
        print("1) Rectangle Pattern")
        print("2) Circle Pattern")
        print("3) Super Pattern")
        mode = eval(input("Which mode do you want to play? 1, 2 or 3: "))

        # If they choose 'Rectangle Patterns'
        if mode == 1:
            #### Add Input Statement(s) as needed ####
          pos = input("center: x, y:  ")
          centerX, centerY = map(int, pos.split(", "))
          centerX, centerY = ((centerX, centerY))
          offset = int(input("offset:  "))
          height = int(input("height:  "))
          width = int(input("width:  "))
          count = int(input("count:  "))
          rotation = int(input("rotation:  "))
            #### End Add Inputs Statement(s) ####


            # Draw the rectangle pattern
          pattern.drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)

        # If they choose 'Circle Patterns'
        elif mode == 2:
            #### Add Input Statement(s) as needed ####
          pos = input("center: x, y:  ")
          x, y = map(int, pos.split(", "))
          x, y = ((x, y))
          offset = int(input("offset:  "))
          radius = int(input("radius:  "))
          count = int(input("count:  "))
          rotation = int(input("rotation:  "))
          pattern.drawCirclePattern(x, y, offset, radius, count)
            #### End Add Inputs Statement(s) ####

            # Draw the circle pattern
            #pattern.drawCirclePattern(centerX, centerY, offset, radius, count)

        # If they choose 'Super Patterns'
        elif mode == 3:
            #### Add Input Statement(s) as needed ####
          pattern.drawSuperPattern()
            #### End Add Inputs Statement(s) ####
                

        # Play again?
        print("Do you want to play again?")
        print("1) Yes, and keep drawings")
        print("2) Yes, and clear drawings")
        print("3) No, I am all done")
        response = eval(input("Choose 1, 2, or 3: "))

        #### Add Statement(s) to clear drawings and play again ####
        if response == 1:
          continue
        if response == 2:
          pattern.reset()
        if response == 3:
          playAgain = False
        #### End Add Inputs Statement(s) ####

    # print a message saying thank you
    print("Thanks for playing!")
    pattern.done()


main()