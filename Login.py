import PySimpleGUI as sg
import gspread 
import face_recognition
import numpy as np
import random
import constants as c
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import Tk
from tkinter.filedialog import askopenfilename

import game_text_sources as gts
import ast

import re

gc = gspread.service_account("./assets/api_key/creeee.json")

sh = gc.open_by_url("https://docs.google.com/spreadsheets/d/1d7Yf2fj7tr4udMj7Jg2wL6m_KjFTwwPJTE-kBauhzB4/edit#gid=0")

worksheet = sh.sheet1

#Khai báo hằng số
EMAIL_COLUMN = 1
USERNAME_COLUMN = 2
PASSWORD_COLUMN = 3
FACE_ID_COLUMN = 4
MONEY_COLUMN = 5
LANGUAGE_COLUMN = 6
BUFF_COLUMN = 7
WINRATE_COLUMN = 8
TOTAL_GAME_COLUMN = 9
HISTORY_COLUMN = 10

#Hàm lưu dữ liệu
def Save (row, column, Svalue):
    worksheet.update_cell(row, column, Svalue)

#Hàm lấy dữ liệu FaceID từ database
def LoadFaceID(Fpassword):
    # Fpassword = str(Fpassword).replace("[", "")
    # Fpassword = Fpassword.replace("]", "")
    # temp =  Fpassword.split()
    # for i in range(128):
    #     temp[i] = np.float64(temp[i])
    # return np.array(temp, dtype=float)
    return np.fromstring(Fpassword[1:-1], dtype=float, sep=' ')

#Hàm bảo mật
def Secure(password):
  string = password
  string2 = ""
  for char in string:
        string2 = string2 + str(ord(char))
  string2 = hash(1/float(string2)) 
  return str(string2)

def is_valid_email(email):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

#Hàm đăng nhập
def Logingin():
    '''
    returns true if the user logins successfully
    returns false if the user exits the login screen
    '''
    layout = [
        [
            sg.Text ("Username"),
            sg.Input (key= "username"),
        ],
        [
            sg.Text ("Password"),
            sg.Input (key= "password", password_char= "*"),
        ],
        [
            sg.Button("Login"),
            sg.Button("Exit"),
            sg.Button("Register"),
            sg.Button("Face ID"),
        ],
        [
            sg.Text("", key = "confirm")
        ]
    ]
    window = sg.Window("Login", layout = layout)

    running = True

    while running:
        event, values = window.read()
        if event == "Login":
            if values["username"] == "" or values["password"] == "":
                window["confirm"].update("Please enter your username and password")
                continue
            soldier = 0
            row = 1
            usname = worksheet.cell(row, USERNAME_COLUMN).value
            psword = worksheet.cell(row, PASSWORD_COLUMN).value
            while usname != None:
                if usname == Secure(values["username"]): 
                    if psword != None:
                        if CheckPassword(psword, values["password"]):
                            soldier = 1   
                            break
                    else:
                        sg.popup("You haven't created a password for this account, please try another way or register with password")
                        break
                else:
                    row = row + 1
                usname = worksheet.cell(row, USERNAME_COLUMN).value
                psword = worksheet.cell(row, PASSWORD_COLUMN).value
            if soldier == 0:
                window["confirm"].update("Fail")
            else:
                window["confirm"].update("Success")
                # Get data from database
                c.money, c.language, c.selected_buff, c.winrate, c.total_games, gts.history_list, c.username = LoadData(values["username"])
                c.won_games = int(c.winrate * c.total_games)
                running = False
                window.close()
                return True
        if event == sg.WIN_CLOSED or event == "Exit":
            running = False
            window.close()
            return False
        if event == "Register":
            Registerin()
        if event == "Face ID":
            if FaceIDLogin():
                running = False
                window.close()
                return True
        
#Hàm đăng kí
def Registerin():
    layout = [
        [
            sg.Text("Email"),
            sg.Input(key= "email")
        ],
        [
            sg.Text ("Username"),
            sg.Input (key= "username"),
        ],
        [
            sg.Text ("Password"),
            sg.Input (key= "password", password_char= "*"),
        ],
        [
            sg.Text ("Confirm"),
            sg.Input (key= "confirm", password_char= "*"),
        ],
        [
            sg.Button ("Create an account"),
            sg.Button ("Login"),
            sg.Button ("Exit"),
        ],
    ]
    window = sg.Window("Register", layout = layout)
    
    running = True

    while running:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            running = False
            window.close()
        if event == "Login":
            running = False
            window.close()
            break
        if event == "Create an account":
            if values["email"] == "" or values["username"] == "" or values["password"] == "" or values["confirm"] == "":
                sg.popup("Please enter all the fields")
                continue
            if not(is_valid_email(values["email"])):
                sg.popup("Please enter a valid email address")
                continue
            if values["password"] == values["confirm"]:
                soldier = 0
                row = 1
                usname = worksheet.cell(row, USERNAME_COLUMN).value
                while usname != None:
                    if usname == Secure(values["username"]):
                        sg.popup("The account has already exist, please try another one or login in to continue")
                        if FaceIDLogin():
                            soldier = 1
                            break
                        else:
                           soldier = 0
                           row = row + 1
                           break
                    else:
                        row = row + 1
                        usname = worksheet.cell(row, USERNAME_COLUMN).value
                        soldier = 1 
                if soldier == 1 or row == 1:
                    rannumber = random.randint(100000, 999999)
                    SendEmail(rannumber, values["email"])
                    if Verify(rannumber):
                        unhashed_username = values["username"]
                        values["email"] = Secure(values["email"])
                        values["username"] = Secure(values["username"])
                        values["password"] = Secure(values["password"])
                        values["confirm"] = Secure(values["confirm"])
                        worksheet.update_cell(row, EMAIL_COLUMN, str(values["email"]))
                        worksheet.update_cell(row, USERNAME_COLUMN, str(values["username"]))
                        worksheet.update_cell(row, PASSWORD_COLUMN, str(values["password"]))
                        SaveGame(300, 'English', 0, 0, 0, [], unhashed_username)

                        sg.popup("Saved")
                        running = False
                        window.close()
                        break
            else:
                sg.popup("Please enter the same password in both password fields.")

#Hàm đăng nhập bằng Face ID
def FaceIDLogin():
    layout = [
        [
            sg.Text("Username"),
            sg.Input(key = "username")
        ],
        [
            sg.Button("Load picture",expand_x= True)
        ],
        [
            sg.Button("Login",expand_x=True),
            sg.Button("Exit",expand_x=True)
        ],
        [
            sg.Button("Register by Face ID", expand_x= True)
        ],
        [
            sg.Text("",key = "confirm"),
        ]
    ]
    window = sg.Window("Face ID", layout = layout)

    running = True

    while running:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            running = False
            window.close()
            return False
            
        if event == "Load picture":
            Tk().withdraw()
            inputedPic = face_recognition.load_image_file(askopenfilename())
            #Kiểm tra xem có phải là ảnh chứa khuôn mặt hay không
            if len(face_recognition.face_encodings (inputedPic)) == 0:
                window["confirm"].update("Failed to detect any faces in the inputed image.")
                continue
            window["confirm"].update("Face detected. Press login to continue.")
            inputedPic_encoding = face_recognition.face_encodings (inputedPic)[0]
        if event == "Login":
            if values["username"] == "":
                window["confirm"].update("Please enter your username")
                continue
            soldier = 0
            row = 1
            usname = worksheet.cell(row, USERNAME_COLUMN).value
            while usname != None:
                if usname == Secure(values["username"]):
                    if worksheet.cell(row, FACE_ID_COLUMN).value != None:
                        psword = LoadFaceID(worksheet.cell(row, FACE_ID_COLUMN).value)
                        if not(SamePic(psword, LoadFaceID(str(inputedPic_encoding)))):
                            if CheckFaceID(psword, inputedPic_encoding):
                                soldier = 1   
                                break
                            else:
                                break
                        else:
                            window["confirm"].update("Please choose a photo different from the one used to register") 
                            break
                    else:
                        sg.popup("You haven't created a Face ID for this account, please try another way or register with Face ID")
                        break
                else:
                    row = row + 1
                    usname = worksheet.cell(row, USERNAME_COLUMN).value
            
            if soldier == 0:
                window["confirm"].update("Fail")
            else:
                window["confirm"].update("Success")
                running = False
                window.close()
                return True
        if event == "Register by Face ID":
            FaceIDRegisterin()

#Hàm đăng kí bằng Face ID
def FaceIDRegisterin():
    layout = [
        [
            sg.Text("Username"),
            sg.Input(key = "username")
        ],
        [
            sg.Button("Load picture",expand_x= True)
        ],
        [
            sg.Button("Register", expand_x= True),
            sg.Button("Exit", expand_x= True)
        ],
    ]
    window = sg.Window("Face ID register", layout = layout)
    
    running = True

    while running:
        event, values = window.read()
        if event == "Exit" or event == sg.WINDOW_CLOSED:
            running = False
            window.close()
        if event == "Load picture":
            Tk().withdraw()
            inputedPic = face_recognition.load_image_file(askopenfilename())
            inputedPic_encoding = str(face_recognition.face_encodings (inputedPic)[0])
        if event == "Register":
            if values["username"] == "":
                sg.popup("Please enter your username")
                continue
            soldier = 0
            row = 1
            usname = worksheet.cell(row, USERNAME_COLUMN).value
            while usname != None:
                if usname == Secure(values["username"]):
                    sg.popup("The account has already exist, please try another one or login in to continue")
                    if Logingin():
                        worksheet.update_cell(row, FACE_ID_COLUMN, inputedPic_encoding)
                        soldier = 1
                        sg.popup("Saved")
                        running = False
                        window.close()
                        break
                    else:
                        soldier = 1
                        break
                else:
                    row = row + 1
                    usname = worksheet.cell(row, USERNAME_COLUMN).value
            if soldier == 0:
                worksheet.update_cell(row, USERNAME_COLUMN, Secure(values["username"]))
                worksheet.update_cell(row, FACE_ID_COLUMN, inputedPic_encoding)
                SaveGame(300, 'English', 0, 0, 0, [], values["username"])
                sg.popup("Saved")
                running = False
                window.close()
                break

#Hàm lưu dữ liệu khi tắt game
def SaveGame (MoneyV, LanguageV, BuffV, WinrateV, TotalGameV, History, Username):
    Row = 1
    usname = worksheet.cell(Row, USERNAME_COLUMN).value
    while usname != None:
        if usname == Secure(Username):
            print("saving game")
            Save(Row, MONEY_COLUMN, MoneyV)
            Save(Row, LANGUAGE_COLUMN, LanguageV)
            Save(Row, BUFF_COLUMN, BuffV)
            Save(Row, WINRATE_COLUMN, WinrateV)
            Save(Row, TOTAL_GAME_COLUMN, TotalGameV)
            Save(Row, HISTORY_COLUMN, str(History))
            break
        else:
            Row = Row + 1
            usname = worksheet.cell(Row, USERNAME_COLUMN).value

#Hàm lấy dữ liệu khi khởi động game
def LoadData (Usname):
    Row = 1
    usname = worksheet.cell(Row, USERNAME_COLUMN).value
    while usname != None:
        if usname == Secure(Usname):
            money = worksheet.cell(Row, MONEY_COLUMN).value
            language = worksheet.cell(Row, LANGUAGE_COLUMN).value
            selected_buff = worksheet.cell(Row, BUFF_COLUMN).value
            winrate = worksheet.cell(Row, WINRATE_COLUMN).value
            total_games = worksheet.cell(Row, TOTAL_GAME_COLUMN).value

            if len(worksheet.cell(Row, HISTORY_COLUMN).value) <= 2:
                history_list = []
            else:
                str_list = worksheet.cell(Row, HISTORY_COLUMN).value
                history_list = ast.literal_eval(str_list)  # This will convert the string to a list

            return (int(money), language, int(selected_buff), float(winrate.replace(',','.')), int(total_games), history_list, Usname)
        else:
            Row = Row + 1
            usname = worksheet.cell(Row, USERNAME_COLUMN).value

def CheckPassword (SavedPassword, InputedPassword):
    if SavedPassword == Secure(InputedPassword):
        return True
    else:
        return False
    
def CheckFaceID (SavedFaceID, InputedFaceID):
    return face_recognition.compare_faces([SavedFaceID], InputedFaceID)[0]

#Hàm gửi mail xác nhận
def SendEmail(Code, Useremail):
    sender_email = "racetracktycoon@gmail.com"
    receiver_email = Useremail
    password = "gzxy qgbw mulx vwux"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Confirm code"
    message["From"] = "RACETRACK TYCOON"
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hello, 
    This is the code you need to verify your email, 
    Please enter this code to the "Verify code" section to continue:
    www.realpython.com""" + str(Code)
    html = """\
    <html>
    <body>
        <p>Hello,<br>
        This is the code you need to verify your email,<br>
        Please enter this code to the "Verify code" section to continue: 
        </p>
    </body>
    </html>
    """ + str(Code) + """\
    <html>
    <body>
        <p>To assure that your account is safe, please don't send this code to other people.
        </p>
    </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

#Hàm xác nhận
def Verify(Vcode):
    layout = [
        [
            sg.Text("Verification code:"),
            sg.Input(key = "verification code"),
        ],
        [
            sg.Button("Verify", expand_x = True),
            sg.Button("Exit", expand_x= True)
        ],
        [
            sg.Text("", key = "announcement"),
        ]
    ]
    window = sg.Window("Verification", layout= layout)

    running = True
    while running:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            running = False 
            window.close()
        if event == "Verify":
            if str(values["verification code"]).replace(' ', '') == str(Vcode):
                window.close()
                return True
            else:
                window["announcement"].update("Please enter the correct verification code")

#Hàm check ảnh trùng
def SamePic(Pic1, Pic2):
    temp1 = list(Pic1)
    temp2 = list(Pic2)
    for i in range (128):
        if temp1[i] != temp2[i]:
            return False
    return True