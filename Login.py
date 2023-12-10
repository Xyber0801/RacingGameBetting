import PySimpleGUI as sg
import gspread 
import face_recognition
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename


gc = gspread.service_account("./assets/api_key/creeee.json")

sh = gc.open_by_url("https://docs.google.com/spreadsheets/d/1d7Yf2fj7tr4udMj7Jg2wL6m_KjFTwwPJTE-kBauhzB4/edit#gid=0")

worksheet = sh.sheet1

#Hàm lấy dữ liệu FaceID từ database
def LoadFaceID(Fpassword):
    Fpassword = str(Fpassword).replace("[", "")
    Fpassword = Fpassword.replace("]", "")
    temp =  Fpassword.split()
    for i in range(128):
        temp[i] = float(temp[i])
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
            i = 1
            usname = worksheet.cell(i, 1).value
            psword = worksheet.cell(i, 2).value
            while usname != None:
                if usname == Secure(str(values["username"])) and psword == Secure(str(values["password"])):
                    soldier = 1   
                    break
                else:
                    i = i + 1
                usname = worksheet.cell(i, 1).value
                psword = worksheet.cell(i, 2).value
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
            window = 0
            break
        if event == "Login":
            Logingin()
            break
        if event == "Create an account":
            if values["password"] == values["confirm"]:
                values["username"] = Secure(str(values["username"]))
                values["password"] = Secure(str(values["password"]))
                values["confirm"] = Secure(str(values["confirm"]))
                values_list = list(values.values())
                worksheet.append_row(values_list)
                sg.popup("Saved")
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
            i = 1
            usname = worksheet.cell(i, 1).value
            while usname != None:
                if usname == Secure(str(values["username"])):
                    psword = LoadFaceID(worksheet.cell(i, 4).value)
                    if face_recognition.compare_faces([inputedPic_encoding], psword)[0]:
                        soldier = 1   
                        break
                    else:
                        i = i + 1
                        usname = worksheet.cell(i,1).value
                else:
                    i = i + 1
                    usname = worksheet.cell(i, 1).value
            if soldier == 0:
                window["confirm"].update("Fail")
                return False
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
            break
        if event == "Load picture":
            Tk().withdraw()
            inputedPic = face_recognition.load_image_file(askopenfilename())
            inputedPic_encoding = str(face_recognition.face_encodings (inputedPic)[0])
        if event == "Register":
            soldier = 0
            i = 1
            usname = worksheet.cell(i, 1).value
            while usname != None:
                if usname == Secure(str(values["username"])):
                    worksheet.update_cell(i, 4, inputedPic_encoding)
                    soldier = 1
                    sg.popup("Saved")
                    running = False
                    window.close()
                    break
                else:
                    i = i + 1
                    usname = worksheet.cell(i, 1).value
            if soldier == 0:
                worksheet.update_cell(i, 1, Secure(str(values["username"])))
                worksheet.update_cell(i, 4, inputedPic_encoding)
                sg.popup("Saved")
            