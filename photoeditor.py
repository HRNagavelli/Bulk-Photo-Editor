
from re import L
from pathlib import Path
from PIL import Image , ImageEnhance, ImageFilter
import os

# Get the Data Paths for Input and Output
path = input("Enter the folder to pick the images: ")
pathout = input("Enter the folder to save the edited images: ")

#Get the Effects to be Applied

while True:
    try:
        effect = int(input(f"Enter the Effect to be applied, you have the choices of /n 1. Sharpen /n 2. Smooth 3. Rotate 4. Convert to GrayScale:"))
    except ValueError:
        print("Sorry, I didn't understand that.")

#better try again... Return to the start of the loop

        continue
    else:

#we're ready to exit the loop.

        break

if effect in range(0,5):

# get the files

        try:
            for filename in os.listdir(path):
                    img = Image.open(f"{path}/{filename}")

# Get the Effect Choice and apply    

                    if effect == 1:
                
                        edit = img.filter(ImageFilter.SHARPEN)

                    elif effect ==2:
                        try:
                            more = str(input("Would you like to deep smoothness? Enter 'y' for Yes 'n' for No: "))
                            if more == 'n':
                                print(f'Ok Lets apply Normal Smoothness')
                                edit = img.filter(ImageFilter.SMOOTH)
                            elif more == 'y':
                                print(f'Great, Lets apply deep Smoothness')
                                edit = img.filter(ImageFilter.SMOOTH_MORE)
                            else:
                                print (f'incorrect choice')
                        except ValueError:
                            print ("Please enter either y or n")


                    elif effect ==3:
                        try:
                            rotation = int(input("In what angle you would like to rotate? Enter 1 for -90, 2 for 90, 3 for -180 and 4 for 180 : "))
                            if rotation in range(0,5):  
                                if rotation == 1:
                                    edit = img.filter(ImageFilter).rotate(-90)
                                elif more == 2:
                                    edit = img.filter(ImageFilter).rotate(90)
                                elif more == 3:
                                    edit = img.filter(ImageFilter).rotate(-180)
                                elif more == 4:
                                    edit = img.filter(ImageFilter).rotate(180)
                                else:
                                    print (f'incorrect choice')
                            else:
                                print(f'entered choice is out of options')
                        except ValueError:
                            print ("Please enter an integer in range of 1 to 4")


                    elif effect ==4:

                            edit = img.filter(ImageFilter).convert('L')

                    
                    else:
                        print(f"Incorrect effect choosed ")

#save the file 

                    clean_name = os.path.splitext(filename)[0]
                    edit.save(f'.{pathout}/{clean_name}_edited.jpg')

        except:
            print(f"There is an error Occured")



else:
    print(f'Please choose an option in range of 1 to 4')




