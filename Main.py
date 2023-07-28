# A small program to store data of user by hashing .

# Ha3H ST0R#R

# Modules
import tkinter as tk
import hashlib as hash
import sys 
import mysql.connector


if __name__ == "__main__": # Condition to check if the file running the program is main or not
    # The start of the program after the conditon is True    

    #Window_class//

    class window:

        def __init__ (self):
            self.height = 400
            self.width = 600
            self.window = tk.Tk()
            self.window_geometry = f"{self.width}x{self.height}"
            self.title = "Ha3h-StoRE#r"
            self.background_color = "#0f0f0f"
            self.icon_img = tk.PhotoImage(file="images/pic-01.png")
            self.background_img = tk.PhotoImage(file="images/pic-02.png")
            self.font_name = "Aerial"
            self.font_size = 10

        def initlized(self):
            self.window.geometry(self.window_geometry)
            self.window.title(self.title)
            self.window.config(bg=self.background_color)
            self.window.resizable(False,False)
           


    # mywindow.window/Window configuration
    mywindow = window()    
    mywindow.window
    mywindow.initlized()
    # Setting up the icon and image for the program


    def database(user_name,user_email,user_password):

        user_args = sys.argv
        servername = user_args[1]
        username = user_args[2]
        password = user_args[3]
        database = user_args[4]
        table = user_args[5]

        connect = mysql.connector.connect(
            host=servername,
            user=username,
            password=password,
            database=database
        )

        mysql_query_executor = connect.cursor()
        mysql_query = f"insert into {table} (Name,Email,Password) values ('{user_name}','{user_email}','{user_password}')"
        mysql_query_executor.execute(mysql_query)

        connect.commit()

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
        FormText1 = tk.Label(mywindow.window,text="Form is empty fill them all     ",fg="#6eda53",font=("Aerial", 7),bg="#0f0f0f")
        FormText3 = tk.Label(mywindow.window,text="You have been signed in         ",fg="#6eda53",font=("Aerial", 7),bg="#0f0f0f")
        FormText4 = tk.Label(mywindow.window,text="Entered invalid email address   ",fg="#6eda53",font=("Aerial", 7),bg="#0f0f0f")
        
        # Random variables 
        Found = False

        LenText2 = len(Text2)

        # For loop to check the data in the data.txt file and apply condition

        if not Text1 or not Text2 or not Text3:
            # Condition to check if the form is filled or not 
            FormText1.place(x=232,y=290)

        elif Text2[LenText2 - 10 : LenText2] != "@gmail.com":
            # Condition to check if the email is valid or not
            FormText4.place(x=232,y=290)
        
        elif Found == False:
            # Fills the data into the data.txt file and shows some text after filling

            FormText3.place(x=232,y=290)
            database(Text1,Text2,HashedText)
            

    
    # The background image handler
    
    # The title of the program
    Title = tk.Label(mywindow.window,text="Ha3H  ST0R#R",fg="#6eda53",font=("Aerial",int(mywindow.font_size*2)),bg="#0f0f0f")
    Title.place(x=int(mywindow.width/2 - 100),y=int(mywindow.height/10))

    
    # Needed : Add label to all the boxes
    # The name text box
    NameText = tk.Label(mywindow.window,text="Name:" , fg="#6eda53" , font=("Aerial" , 8),bg="#0f0f0f")
    NameText.place(x=int(mywindow.width/2 - 130),y = 100)


    InputBox1 = tk.Text(mywindow.window,height = 1 ,width= 30 , border=0.1 ,bg="#1f1f1f" ,foreground="#ffffff")
    InputBox1.place(x=int(mywindow.width/2 - 130) , y = 120)

    
    # The email text box
    EmailText = tk.Label(mywindow.window,text="Email:" , fg="#6eda53" , font=("Aerial" , 8),bg="#0f0f0f")
    EmailText.place(x=int(mywindow.width/2 - 130),y = 149)
    
    
    InputBox2 = tk.Text(mywindow.window,height = 1 ,width= 30 , border=0.1,bg="#1f1f1f" ,foreground="#ffffff")
    InputBox2.place(x=int(mywindow.width/2 - 130) , y = 170)

    # The password text box
    PasswordText = tk.Label(mywindow.window,text="Password:" , fg="#6eda53" , font=("Aerial" , 8),bg="#0f0f0f")
    PasswordText.place(x=int(mywindow.width/2 - 130),y = 195)


    InputBox3 = tk.Text(mywindow.window,height = 1 ,width= 30 , border=0,bg="#1f1f1f" ,foreground="#ffffff")
    InputBox3.place(x=int(mywindow.width/2 - 130) , y = 215)


    # The main Login button for the whole program
    Signinbutton = tk.Button(mywindow.window,text="SignIn" , border=0 ,background="#ffffff" ,width=13,fg="#6eda53",bg="#0f0f0f")
    Signinbutton.bind("<Button>" ,Clicked)
    Signinbutton.place(x=int(mywindow.width/2-70) , y=250)
    
    mywindow.window.mainloop()
    # Program ends after this 
    # ------------------------------------------------------------------------------------------


