#thư viện
import pygame #game
#import sys
from button import ButtonA
import game_text_sources as g 
pygame.init()

from tkinter import *  #file
from tkinter import filedialog

import cv2      #xuat file txt
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

import os.path #image

import constants as c


SCREEN = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

BG = pygame.transform.scale(pygame.image.load('./assets/BXH/bg2.png'), (c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
Ldb = pygame.image.load('./assets/BXH/leaderboard00.png')
Ldb = pygame.transform.scale(Ldb,(361,494))

brown_color  = pygame.Color(153, 82, 26)

def filetxt(): #chuyển file screen
    pygame.display.set_caption("File text")

    #chú ý
    CHOOSE_TEXT = pygame.font.SysFont('cambria', 30).render(g.lg_list[104], True, "white")
    CHOOSE_RECT = CHOOSE_TEXT.get_rect(center=(670, 600))
    SCREEN.blit(CHOOSE_TEXT, CHOOSE_RECT)
    pygame.display.update()
    cv2.waitKey(1000)

    img_path = filedialog.askopenfilename(title=g.lg_list[106])
    if not (os.path.isfile(img_path) and img_path.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.JPG'))):
        return

    running = True

    while running:
        FILE_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        
        picture = pygame.image.load(img_path)
        picture = pygame.transform.scale(picture, (300, 300))
        SCREEN.blit(picture , (350,100))


        FILE_BACK = ButtonA(image=None, pos = (640,460), text_input=g.lg_list[124], font=pygame.font.SysFont('cambria', 30), base_color="White", hovering_color="green")

        FILE_BACK.changeColor(FILE_MOUSE_POS)
        FILE_BACK.update(SCREEN)

        PC_TEXT = pygame.font.SysFont('cambria', 30).render(g.lg_list[108], True, "Yellow")
        PC_RECT = PC_TEXT.get_rect(center=(500, 50))
        SCREEN.blit(PC_TEXT, PC_RECT)

        FILE_SAVE = ButtonA(image=None, pos = (300,460), text_input=g.lg_list[126], font=pygame.font.SysFont('cambria', 30), base_color="White", hovering_color="green")

        FILE_SAVE.changeColor(FILE_MOUSE_POS)
        FILE_SAVE.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if FILE_BACK.checkForInput(FILE_MOUSE_POS):
                    return
                if FILE_SAVE.checkForInput(FILE_MOUSE_POS):
                    #xuất file txt
                    img = cv2.imread(img_path)
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    text = pytesseract.image_to_string(img, lang="eng")
                    with open("./assets/BXH/filetxt.txt", "w", encoding="utf-8") as f:
                        f.writelines(text)

                    #giao diện xuất file txt
                    root = Tk()
                    root.title("file txt")
                    root.geometry("600x600")
                    def img_to_txt():       #hiển thị txt
                        text_file = open("./assets/BXH/filetxt.txt")
                        print(text_file)
                        data = text_file.read()
                        my_text.insert(END,data)
                        text_file.close()
                    def open_file():        #thêm txt
                        text_file = open(filedialog.askopenfilename())
                        print(text_file)
                        data = text_file.read()
                        my_text.insert(END,data)
                        text_file.close()
                    def save_file():        #lưu txt
                        text_file = open(filedialog.asksaveasfilename(defaultextension='.txt',
                                                                      filetypes=[
                                                                          ("Text file", ".txt"),
                                                                          ("HTML file", ".html"),
                                                                          ("All files", ".*"),
                                                                      ]), "w")
                        data = text_file.write(my_text.get(1.0,END))
                        text_file.close()
                        

                    def tk_quit():
                        root.quit()
                        root.destroy()
                    my_text = Text(root, width=40, height=10, font=("Helvetica", 16))   #hiển thị & sửa txt
                    my_text.pack(pady=20)
                    txt_button = Button(root,text= g.lg_list[110], command = img_to_txt)
                    txt_button.pack(pady=20)
                    open_button = Button(root,text= g.lg_list[112], command = open_file)
                    open_button.pack(pady=20)
                    save_button = Button(root,text= g.lg_list[114], command = save_file)
                    save_button.pack(pady=20)  
                    quit_button = Button(root, text=g.lg_list[8], command=tk_quit).pack(pady=20)     
                    root.protocol("WM_DELETE_WINDOW", tk_quit)
                    root.mainloop()
                     
                    #thông báo thành công
                    CPL_TEXT = pygame.font.SysFont('cambria', 30).render(g.lg_list[116], True, "white")
                    CPL_RECT = CPL_TEXT.get_rect(center=(300, 500))
                    SCREEN.blit(CPL_TEXT, CPL_RECT)

                    pygame.display.update()
                    cv2.waitKey(1000)
        pygame.display.update()
    
   

# def Start(): #game chính screen
#     pygame.display.set_caption("Play")

#     while True:
#         PLAY_MOUSE_POS = pygame.mouse.get_pos()

#         SCREEN.fill("black")

#         PLAY_TEXT = pygame.font.SysFont('cambria', 30).render("This is the Play screen.", True, "White")
#         PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
#         SCREEN.blit(PLAY_TEXT, PLAY_RECT)

#         PLAY_BACK = ButtonA(image=None, pos = (640,460), text_input="BACK", font=pygame.font.SysFont('cambria', 30), base_color="White", hovering_color="green")

#         PLAY_BACK.changeColor(PLAY_MOUSE_POS)
#         PLAY_BACK.update(SCREEN)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONUP:
#                 if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
#                     main_BXH()
#         pygame.display.update()


def main_BXH(finished_racers): #main BXH screen
    pygame.display.set_caption("BXH")

    pygame.mixer.stop()
    pygame.mixer.music.load("./assets/music/leaderboard_music.mp3")
    pygame.mixer.music.play(-1)

    running = True

    while running:
        SCREEN.blit(BG, (0,0))
        SCREEN.blit(Ldb, (460,113))
        BXH_MOUSE_POS = pygame.mouse.get_pos()  #kiểm tra chuột
        
        #button
        ST = pygame.image.load("./assets/BXH/button00.png")
        ST = pygame.transform.scale(ST, (150, 170))
        Start_button = ButtonA(image=ST, pos = (665, 600), 
                       text_input="Menu", font=pygame.font.SysFont('cambria', 30), base_color="red", hovering_color="yellow")
        
        Scr = pygame.image.load("./assets/BXH/button00.png")
        Scr = pygame.transform.scale(Scr, (150, 170))
        Screenshot_button = ButtonA(image=Scr, pos = (500,620), 
                       text_input=g.lg_list[118], font=pygame.font.SysFont('cambria', 30), base_color="red", hovering_color="yellow")
        
        file = pygame.image.load("./assets/BXH/button00.png")
        file = pygame.transform.scale(file, (150, 170))
        filetxt_button = ButtonA(image=file, pos = (800,620), 
                       text_input=g.lg_list[120], font=pygame.font.SysFont('cambria', 30), base_color="red", hovering_color="yellow")

        #leaderboard text
        for i in range(5):
            racer = finished_racers.sprites()[i]
            racer_text = pygame.font.SysFont('cambria', 40).render(f"{racer.name}", True, brown_color)
            SCREEN.blit(racer_text, (580, 200 + i * 75))

        #đổi màu button khi trỏ chuột
        for button in [Start_button, Screenshot_button, filetxt_button]:
            button.changeColor(BXH_MOUSE_POS)
            button.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if Start_button.checkForInput(BXH_MOUSE_POS):   
                    running = False

                if Screenshot_button.checkForInput(BXH_MOUSE_POS):
                    #lấy tọa độ và chụp màn hình
                    #picture = pyautogui.screenshot(region=(rect.left + 10,rect.top + 35,1000,672))
                    #picture.save('./assets/BXH/screenshot.png')
                    pygame.image.save(SCREEN, './assets/BXH/screenshot.png')
                    
                        #HIỂN THỊ ẢNH VỪA CHỤP
                    #pc = cv2.imread('C:\\Users\\ASUS\\OneDrive\\Desktop\\DL BXH\\BXH\\screenshot.png')
                    #cv2.imshow("SAVED SCREEN IMAGES", pc)
                    #cv2.waitKey()
                    

                    #LƯU ẢNH VỪA CHỤP (BẮT BUỘC)
                    # Load image
                    pct = pygame.image.load("./assets/BXH/screenshot.png")
                    # Show save dialog
                    root =Tk()
                    root.withdraw()
                    path = filedialog.asksaveasfilename(defaultextension='.png',
                                                                      filetypes=[
                                                                          ("PNG file", ".png"),
                                                                      ],title=g.lg_list[122])
                    # Save image
                    while not path or os.path.splitext(path)[1] != ".png":
                        path = filedialog.asksaveasfilename(defaultextension='.png',
                                                                      filetypes=[
                                                                          ("PNG file", ".png"),
                                                                      ],title=g.lg_list[122])
                    pygame.image.save(pct, path)
                    
                    
                    #thông báo hoàn thành
                    CPL_TEXT = pygame.font.SysFont('cambria', 30).render(g.lg_list[116], True, "white")
                    CPL_RECT = CPL_TEXT.get_rect(center=(330, 600))
                    SCREEN.blit(CPL_TEXT, CPL_RECT)
                    pygame.display.update()
                    cv2.waitKey(1000)

                    
                if filetxt_button.checkForInput(BXH_MOUSE_POS):
                    filetxt()

        pygame.display.update()