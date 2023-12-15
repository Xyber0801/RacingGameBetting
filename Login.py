import PySimpleGUI as sg
import gspread 
import face_recognition
import numpy as np
import random
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import Tk
from tkinter.filedialog import askopenfilename



gc = gspread.service_account()

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


#Hàm lưu dữ liệu
def Save (row, column, Svalue):
    worksheet.update_cell(row, column, Svalue)

#Hàm lấy dữ liệu FaceID từ database
def LoadFaceID(Fpassword):
    Fpassword = str(Fpassword).replace("[", "")
    Fpassword = Fpassword.replace("]", "")
    temp =  Fpassword.split()
    for i in range(128):
        temp[i] = np.float64(temp[i])
    return np.array(temp, dtype=float)

#Hàm bảo mật
def Secure(password):
  string = password
  string2 = ""
  for char in string:
        string2 = string2 + str(ord(char))
  string2 = hash(1/float(string2)) 
  return str(string2)

#Hàm đăng nhập
def Logingin():
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
            sg.Text("",key = "confirm")
        ]
    ]
    window = sg.Window("Login", layout = layout)

    running = True

    while running:
        event, values = window.read()
        if event == "Login":
            soldier = 0
            row = 1
            usname = worksheet.cell(row, USERNAME_COLUMN).value
            psword = worksheet.cell(row, PASSWORD_COLUMN).value
            while usname != None:
                if usname == Secure(values["username"]):
                    if CheckPassword(psword, values["password"]):
                        soldier = 1   
                        break
                else:
                    row = row + 1
                usname = worksheet.cell(row, USERNAME_COLUMN).value
                psword = worksheet.cell(row, PASSWORD_COLUMN).value
            if soldier == 0:
                window["confirm"].update("Fail")
            else:
                window["confirm"].update("Success")
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
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            window.close()
            break
        if event == "Login":
            window.close()
            Logingin()
            break
        if event == "Create an account":
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
                        values["email"] = Secure(values["email"])
                        values["username"] = Secure(values["username"])
                        values["password"] = Secure(values["password"])
                        values["confirm"] = Secure(values["confirm"])
                        worksheet.update_cell(row, EMAIL_COLUMN, values["email"])
                        worksheet.update_cell(row, USERNAME_COLUMN, values["username"])
                        worksheet.update_cell(row, PASSWORD_COLUMN, values["password"])
                        sg.popup("Saved")
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
            window.close()
            break
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
            soldier = 0
            row = 1
            usname = worksheet.cell(row, USERNAME_COLUMN).value
            while usname != None:
                if usname == Secure(values["username"]):
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
                sg.popup("Saved")

#Hàm lưu dữ liệu khi tắt game
def SaveGame (MoneyV, LanguageV, BuffV, WinrateV, Username):
    Row = 1
    usname = worksheet.cell(Row, USERNAME_COLUMN).value
    while usname != None:
        if usname == Secure(Username):
            Save(Row, MONEY_COLUMN, MoneyV)
            Save(Row, LANGUAGE_COLUMN, LanguageV)
            Save(Row, BUFF_COLUMN, BuffV)
            Save(Row, WINRATE_COLUMN, WinrateV)
        else:
            Row = Row + 1

#Hàm lấy dữ liệu khi khởi động game
def LoadData (M, L, B, W, Usname):
    Row = 1
    usname = worksheet.cell(Row, USERNAME_COLUMN).value
    while usname != None:
        if usname == Secure(Usname):
            M = worksheet.cell(Row, MONEY_COLUMN).value
            L = worksheet.cell(Row, LANGUAGE_COLUMN).value
            B = worksheet.cell(Row, BUFF_COLUMN).value
            W = worksheet.cell(Row, WINRATE_COLUMN).value
        else:
            Row = Row + 1

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
            if values["verification code"] == str(Vcode):
                window.close()
                return True
            else:
                window["announcment"].update("Please enter the correct verification code")

#Hàm check ảnh trùng
def SamePic(Pic1, Pic2):
    temp1 = list(Pic1)
    temp2 = list(Pic2)
    for i in range (128):
        if temp1[i] != temp2[i]:
            return False
    return True

Logingin()








