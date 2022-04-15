# A small program to store data of user by hashing .

# Ha3H ST0R#R

# Modules
import tkinter as tk
import hashlib as hash

if __name__ == "__main__": # Condition to check if the file running the program is main or not
    # The start of the program after the conditon is True    
    
    # Screen/Window configuration
    Screen = tk.Tk()
    Screen.geometry("600x400+50+50")
    Screen.title("Ha3H  ST0R#R")
    Screen.config(bg="#0f0f0f")

    # Setting up the icon and image for the program
    Icon = tk.PhotoImage(file="pic-01.png")
    Background = tk.PhotoImage(file="pic-02.png")
    Screen.iconphoto(False,Icon)
    Index1 = 0

    def Clicked(LoginClick):
        # Function that handles the storing of the data into a txt file (Data.txt)

        # The userdata form the form
        Text1 = InputBox1.get(1.0, "end-1c")
        Text2 = InputBox2.get(1.0, "end-1c")
        Text3 = InputBox3.get(1.0, "end-1c")
        
        # The hasher to convert data to hash
        EncodedPass = hash.md5(Text3.encode())
        HashedText = EncodedPass.hexdigest()

        # Text for response
        FormText1 = tk.Label(Screen,text="Form is empty fill them all     ",fg="#6eda53",font=("Aerial", 7),bg="#0f0f0f")
        FormText2 = tk.Label(Screen,text="Already filled with this data   ",fg="#6eda53",font=("Aerial", 7),bg="#0f0f0f")
        FormText3 = tk.Label(Screen,text="Thanks you for filling the form ",fg="#6eda53",font=("Aerial", 7),bg="#0f0f0f")
        FormText4 = tk.Label(Screen,text="Entered invalid email address   ",fg="#6eda53",font=("Aerial", 7),bg="#0f0f0f")
        
        # Random variables 
        File2 = open("Data.txt" ,"r")
        Data2 = File2.readlines()
        Found = False
        global Index1
        LenText2 = len(Text2)
        Access = False

        # For loop to check the data in the data.txt file and apply condition
        for Lines in Data2:
            if Lines.strip() == Text1 or Lines.strip() == Text2:
                Found = True


        if not Text1 or not Text2 or not Text3:
            # Condition to check if the form is filled or not 
            FormText1.place(x=260,y=290)

        elif Text2[LenText2 - 10 : LenText2] != "@gmail.com":
            # Condition to check if the email is valid or not
            FormText4.place(x=260,y=290)
        
        elif Found == False and not Data2 == None or not Data2:
            # Fills the data into the data.txt file and shows some text after filling

            FormText3.place(x=260,y=290)
            File = open("Data.txt" ,"a+")
            File.write(f"\n{Text1}")
            File.write(f"\n{Text2}")
            File.write(f"\n{HashedText}")
            File.close()

        else:
            # Condition to check if the data is already in the data.txt file 
            FormText2.place(x=260,y=290)
        File2.close()

    
    # The background image handler
    Backgroundimg = tk.Label(Screen,image=Background , border =0)
    Backgroundimg.place(x=0,y=0)

    # The title of the program
    Title = tk.Label(Screen,text="Ha3H  ST0R#R",fg="#6eda53",font=("Aerial", 14),bg="#0f0f0f")
    Title.place(x=250,y=70)

    # Needed : Add label to all the boxes
    # The name text box
    NameText = tk.Label(Screen,text="Name:" , fg="#6eda53" , font=("Aerial" , 8),bg="#0f0f0f")
    NameText.place(x=195,y = 100)
    InputBox1 = tk.Text(Screen,height = 1 ,width= 30 , border=0.1 ,bg="#b3ebb7")
    InputBox1.place(x=195 , y = 120)

    # The email text box
    EmailText = tk.Label(Screen,text="Email:" , fg="#6eda53" , font=("Aerial" , 8),bg="#0f0f0f")
    EmailText.place(x=195,y = 140)
    InputBox2 = tk.Text(Screen,height = 1 ,width= 30 , border=0.1,bg="#b3ebb7")
    InputBox2.place(x=195 , y = 160)

    # The password text box
    PasswordText = tk.Label(Screen,text="Password:" , fg="#6eda53" , font=("Aerial" , 8),bg="#0f0f0f")
    PasswordText.place(x=195,y = 180)
    InputBox3 = tk.Text(Screen,height = 1 ,width= 30 , border=0.1,bg="#b3ebb7")
    InputBox3.place(x=195 , y = 200)

    # The main Login button for the whole program
    Signinbutton = tk.Button(Screen,text="SignIn" , border=0 ,background="#ffffff" ,width=13,fg="#6eda53",bg="#0f0f0f")
    Signinbutton.bind("<Button>" ,Clicked)
    Signinbutton.place(x=270 , y=230)
    
    Screen.mainloop()
    # Program ends after this 
    # ------------------------------------------------------------------------------------------


