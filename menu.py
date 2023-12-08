#Khai báo thư viện
import pygame, sys
from pygame.locals import *
import constants as c
from coregame import GameManager
from DinoGame import Dino_game
from minigame import Minigame
from car_game import Car_Game
from snake_game import Snake_game
from game_text_sources import *
pygame.mixer.pre_init(frequency=44100,size=-16,channels=2,buffer=512)
pygame.init()
clock=pygame.time.Clock()
#Tiêu đề, cửa sổ game, phông chữ
pygame.display.set_caption('Menu')
font=pygame.font.SysFont('Constantia',35)
screen=pygame.display.set_mode((1280,720))
#Background
bg=pygame.transform.scale(pygame.image.load(r".\Assets\Menu_Background\Menu0.png"),(1280,720))
#Các class đối tượng
    #Class menu button
class button():
    text_col=(0,0,0)   
    def __init__(self,x,y,width,height,type,text_dis,text):
        self.x=x
        self.y=y
        self.text=text
        self.width=width
        self.height=height
        self.type=type
        self.text_dis=text_dis
    def draw_button(self):
        global clicked, image_list
        action=False
        #Lấy vị trí trỏ chuột
        pos=pygame.mouse.get_pos()
        #Tạo rect cho nút
        button_surface=pygame.transform.scale(pygame.image.load(image_list[self.type]),(self.width,self.height))
        button_rect=button_surface.get_rect(center=(self.x+self.width/2, self.y+self.height/2))
        #Kiểm tra điều kiện nhấn chuột
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                clicked=True
                button_surface=pygame.transform.scale(pygame.image.load(image_list[self.type+1]),(self.width,self.height))
                screen.blit(button_surface,button_rect)
            elif pygame.mouse.get_pressed()[0]==0 and clicked==True:
                clicked=False
                action=True
            else:
                button_surface=pygame.transform.scale(pygame.image.load(image_list[self.type]),(self.width,self.height))
                screen.blit(button_surface,button_rect)
                
        else:
            button_surface=pygame.transform.scale(pygame.image.load(image_list[self.type-1]),(self.width,self.height))
            screen.blit(button_surface,button_rect)
            
        #Thêm viền cho nút
        pygame.draw.line(screen,"white",(self.x,self.y),(self.x+self.width,self.y),2)
        pygame.draw.line(screen,"white",(self.x,self.y),(self.x,self.y+self.height),2)
        pygame.draw.line(screen,"white",(self.x,self.y+self.height),(self.x+self.width,self.y+self.height),2)
        pygame.draw.line(screen,"white",(self.x+self.width,self.y),(self.x+self.width,self.y+self.height),2)
        #Thêm chữ cho nút
        text_img=font.render(self.text,True,self.text_col)
        text_len=text_img.get_width()
        screen.blit(text_img,(self.x+int(self.width/2)-int(text_len/2),self.y+self.text_dis))
        return action
class round_button():
    button_col=(25,190,220)
    hover_col=(75,225,225)
    click_col=(50,150,255)
    text_col=(255,255,255)
    r=70
    def __init__(self,x,y,radius,text_dis,text):
        self.x=x
        self.y=y
        self.radius=radius
        self.text_dis=text_dis
        self.text=text
    def draw_button(self):
        global clicked
        action=False
        #Lấy vị trí trỏ chuột
        pos=pygame.mouse.get_pos()
        #Tạo rect cho nút
        button_surface=pygame.Surface((3.0*self.r, 3.0*self.r))
        button_rect=button_surface.get_rect(center=(self.x, self.y))
        #Kiểm tra điều kiện nhấn chuột
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                clicked=True
                pygame.draw.circle(screen,self.click_col,(self.x, self.y),self.radius)
            elif pygame.mouse.get_pressed()[0]==0 and clicked==True:
                clicked=False
                action=True
            else:
                pygame.draw.circle(screen,self.hover_col,(self.x, self.y),self.radius)
        else:
            pygame.draw.circle(screen,self.button_col,(self.x, self.y),self.radius)
        #Thêm viền cho nút
        pygame.draw.circle(screen,"white",(self.x, self.y),self.radius,3)
        #Thêm chữ cho nút
        text_img=font.render(self.text,True,self.text_col)
        text_len=text_img.get_width()
        screen.blit(text_img,(self.x-int(text_len/2),self.y-4*self.text_dis))
        return action
#Các hàm

def game_name():
    global text_x, text_y, dtext
    name_text=pygame.transform.scale(pygame.image.load(r'.\Assets\Menu_Background\name_text.png'),(730,140))
    name_text_rect=name_text.get_rect(center=(text_x, text_y)) 
    text_y+=dtext
    if (text_y>=70):
        dtext=-dtext
    if (text_y<=100):
        dtext=-dtext
    screen.blit(name_text, name_text_rect)
        
    #Hàm vẽ khung chữ nhật
def draw_rect(x,y,width,height,type,text_color,text_dis,text):
    surface=pygame.transform.scale(pygame.image.load(image_list[type]),(width,height))
    surface_rect=surface.get_rect(center=(x+int(width/2),y+int(height/2)))
    screen.blit(surface,surface_rect)
    text_img=font.render(text,True,text_color)
    text_len=text_img.get_width()
    screen.blit(text_img,(x+int(width/2)-int(text_len/2),y+text_dis))
    #Hàm màn hình menu
def menu_display():
    global menu_active, play_button_active, history_button_active, setting_button_active, shop_button_active, minigame_active
    play=button(460,170,360,80,1,22.5,lg_list[2])
    history=button(460,270,360,80,1,22.5,lg_list[4])
    setting=button(460,370,360,80,1,22.5,lg_list[6])
    quit=button(460,470,360,80,1,22.5,lg_list[8])
    shop=button(1024,16,240,40,1,2.5,lg_list[10])
    mini_game=button(1024,76,240,40,1,2.5,lg_list[12])
    if play.draw_button():
        menu_active=False
        play_button_active=True
    if history.draw_button():
        menu_active=False
        history_button_active=True
    if setting.draw_button():
        menu_active=False
        setting_button_active=True
    if quit.draw_button():
        pygame.quit()
        sys.exit()
    if shop.draw_button():
        menu_active=False
        shop_button_active=True
    if mini_game.draw_button():
        menu_active=False
        minigame_active=True
    #Hàm chọn môi trường
def environment_display():
    global menu_active, play_button_active, ev_choosing, ev
    ev1=button(29,140,388,218.25,4,5,'')
    ev2=button(446,140,388,218.25,7,5,'')
    ev3=button(863,140,388,218.25,10,5,'')
    back=button(30,30,180,40,1,2.5,lg_list[14])
    draw_rect(29,388.25,388,80,112,(0,0,0),22.5,lg_list[16])
    draw_rect(446,388.25,388,80,112,(0,0,0),22.5,lg_list[18])
    draw_rect(863,388.25,388,80,112,(0,0,0),22.5,lg_list[20])
    draw_rect(415,30,450,80,111,(0,0,0),22.5,lg_list[22])   
    if back.draw_button():
        ev=''
        menu_active=True
        play_button_active=False
        ev_choosing=False
    if ev1.draw_button():
        ev_choosing=True
        ev=lg_list[16]       
    if ev2.draw_button():
        ev_choosing=True
        ev=lg_list[18]
    if ev3.draw_button():
        ev_choosing=True
        ev=lg_list[20]
    #Hàm chọn Yes/No (Môi trường)
def evm_choosing():
    global chr_set_active, ev_choosing, ev, play_button_active, actual_ev
    yes=button(340,600,180,40,1,2.5,lg_list[24])
    no=button(760,600,180,40,1,2.5,lg_list[26])
    if ev_choosing:   
        draw_rect(215,498.25,850,191.75,113,(0,0,0),30,lg_list[28].replace('\n',ev))
        if yes.draw_button():
            chr_set_active=True
            play_button_active=False
            ev_choosing=False
        if no.draw_button():
            ev_choosing=False
            ev=''
    #Hàm hiển thị set nhân vật
def character_set_display():
    global play_button_active, chr_set_active, chr_set_choosing, chr_set, chr_set_index, distance_active
    set1=button(29,140,388,170,22,5,'')
    set2=button(446,140,388,170,25,5,'')
    set3=button(863,140,388,170,28,5,'')
    set4=button(237.5,340,388,170,31,5,'')
    set5=button(654.5,340,388,170,34,5,'')
    back=button(30,30,180,40,1,2.5,lg_list[14])   
    draw_rect(415,30,450,80,111,(0,0,0),22.5,lg_list[40])   
    if back.draw_button():
        play_button_active=True
        chr_set_active=False
        chr_set_choosing=False
    if set1.draw_button():
        chr_set_choosing=True
        chr_set=lg_list[30]
        chr_set_index=1
    if set2.draw_button():
        chr_set_choosing=True
        chr_set=lg_list[32]
        chr_set_index=2
    if set3.draw_button():
        chr_set_choosing=True
        chr_set=lg_list[34]
        chr_set_index=3  
    if set4.draw_button():
        chr_set_choosing=True
        chr_set=lg_list[36]  
        chr_set_index=4 
    if set5.draw_button():
        chr_set_choosing=True
        chr_set=lg_list[38] 
        chr_set_index=5
    #Hàm chọn Yes/No/More Info (set nhân vật)
def chr_choosing():
    global chr_set_active, chr_set_choosing, chr_set, distance_active, chr_set_info, chr_set_info_button, chr_set_index
    yes=button(295,620,180,40,1,2.5,lg_list[24])
    no=button(505,620,180,40,1,2.5,lg_list[26])
    chr_set_info_button=button(715,620,270,40,1,2.5,lg_list[46])
    if chr_set_choosing:
        draw_rect(215,540,850,150,113,(0,0,0),22.5,chr_set)
        if yes.draw_button():
            distance_active=True
            chr_set_active=False
            chr_set_choosing=False
        if no.draw_button():
            chr_set_choosing=False
            chr_set_index=0
        if chr_set_info_button.draw_button():
            chr_set_active=False
            chr_set_choosing=False
            chr_set_info=True
    #Hàm thông tin set nhân vật
def chr_set_information():
    global chr_set_choosing, chr_set_active, chr_set_info, chr_info, chr_set, chr, character_name, chr_set_index, unit
    draw_rect(415,30,450,80,111,(0,0,0),22.5,lg_list[78+2*(chr_set_index-1)])
    chr1=button(30,140,220,550,34+(5*(chr_set_index-1)+1)*3,5,'')
    chr2=button(280,140,220,550,34+(5*(chr_set_index-1)+2)*3,5,'')
    chr3=button(530,140,220,550,34+(5*(chr_set_index-1)+3)*3,5,'')
    chr4=button(780,140,220,550,34+(5*(chr_set_index-1)+4)*3,5,'')
    chr5=button(1030,140,220,550,34+(5*(chr_set_index-1)+5)*3,5,'')
    back=button(30,30,180,40,1,2.5,lg_list[14])
    if back.draw_button():
        chr_set_active=True
        chr_set_info=False
        chr_info=False
    if chr1.draw_button(): 
        chr_set_info=False
        chr_info=True       
        chr=5*(chr_set_index-1)+1
    if chr2.draw_button():
        chr_set_info=False
        chr_info=True
        chr=5*(chr_set_index-1)+2
    if chr3.draw_button():
        chr_set_info=False
        chr_info=True
        chr=5*(chr_set_index-1)+3
    if chr4.draw_button():
        chr_set_info=False
        chr_info=True
        chr=5*(chr_set_index-1)+4
    if chr5.draw_button():
        chr_set_info=False
        chr_info=True
        chr=5*(chr_set_index-1)+5
    unit=4*(chr-1)
    #Hàm lấy thông tin nhân vật
def chr_information():
    global chr_set_info, chr_info, chr, info, unit
    back=button(30,30,180,40,1,2.5,lg_list[14])
    pre=button(10,320,50,40,1,2.5,'<-')
    next=button(1220,320,50,40,1,2.5,'->')
    chr_img=pygame.transform.smoothscale(pygame.image.load(info[unit]),(1280,720))
    screen.blit(chr_img,(0,0))
    if back.draw_button():
        chr_set_info=True
        chr_info=False    
    if pre.draw_button():
        unit=4*(chr-1)
    if next.draw_button():
        unit=4*(chr-1)+2
    #Hàm chọn độ dài đường đua
def distance_display():
    global distance_active, chr_set_active, distance_choosing, distance
    dis1=button(29,140,388,218.25,13,5,'')
    dis2=button(446,140,388,218.25,16,5,'')
    dis3=button(863,140,388,218.25,19,5,'')
    back=button(30,30,180,40,1,2.5,lg_list[14])
    draw_rect(29,388.25,388,80,112,(0,0,0),22.5,lg_list[48])
    draw_rect(446,388.25,388,80,112,(0,0,0),22.5,lg_list[50])
    draw_rect(863,388.25,388,80,112,(0,0,0),22.5,lg_list[52])
    draw_rect(415,30,450,80,111,(0,0,0),22.5,lg_list[54])   
    if back.draw_button():
        chr_set_active=True
        distance_active=False
        distance_choosing=False
    if dis1.draw_button():
        distance_choosing=True
        distance=lg_list[48]         
    if dis2.draw_button():
        distance_choosing=True
        distance=lg_list[50]   
    if dis3.draw_button():
        distance_choosing=True
        distance=lg_list[52]   
    #Hàm chọn Yes/No(độ dài đường đua)
def dis_choosing():
    global distance_choosing, distance_active, distance, menu_running
    yes=button(360,600,180,40,1,2.5,lg_list[24])
    no=button(740,600,180,40,1,2.5,lg_list[26])
    if distance_choosing:
        draw_rect(240,498.25,800,191.75,113,(0,0,0),30,lg_list[56].replace('\n',distance))
        if yes.draw_button():
            initial_setup()
            pygame.mixer_music.stop()
            menu_running=False
            distance_active=False
            distance_choosing=False
        if no.draw_button():
            distance_choosing=False
            distance=''
def initial_setup():
    global ev, distance, chr_set_index
    if ev==lg_list[16]:
        if distance==lg_list[48]:
            c.background_setup=c.forest_short
        if distance==lg_list[50]:
            c.background_setup=c.forest_medium
        if distance==lg_list[52]:
            c.background_setup=c.forest_long
    elif ev==lg_list[18]:
        if distance==lg_list[48]:
            c.background_setup=c.grassland_short
        if distance==lg_list[50]:
            c.background_setup=c.grassland_medium
        if distance==lg_list[52]:
            c.background_setup=c.grassland_long
    else:
        if distance==lg_list[48]:
            c.background_setup=c.sunset_short
        if distance==lg_list[50]:
            c.background_setup=c.sunset_medium
        if distance==lg_list[52]:
            c.background_setup=c.sunset_long
    if chr_set_index==1:
        c.character_setup=c.animal_set
    elif chr_set_index==2:
        c.character_setup=c.chibi_set
    elif chr_set_index==3:
        c.character_setup=c.medieval_set
    elif chr_set_index==4:
        c.character_setup=c.monster_set
    else:
        c.character_setup=c.car_set
    #Hàm hiển thị lịch sử gameplay
def history_display():
    global menu_active, history_button_active, u, v
    back=button(30,30,180,40,1,2.5,lg_list[14])
    previous=button(30,320,180,40,1,2.5,lg_list[58])
    next=button(1070,320,180,40,1,2.5,lg_list[42])
    winrate=0
    for i in range(0,len(history_list),1):
        if i%6==2:
            if history_list[i]==1:
                winrate+=1
    winrate=round(100*winrate/(len(history_list)//6),2)
    winrate_text = font.render(history_text[0].replace('\n',str(winrate)), True, (255,255,255))
    winrate_text_rect = winrate_text.get_rect(midtop=(640,50))
    game_played_text = font.render(history_text[1].replace('\n',str(len(history_list)//6)), True, (255,255,255))
    game_played_text_rect = game_played_text.get_rect(midtop=(640,125))
    history_bg=pygame.image.load(image_list[116])
    screen.blit(history_bg,(0,0))
    draw_rect(240,25,800,160,129,(0,0,0),5,'')
    draw_rect(240,225,800,460,129,(0,0,0),5,'')
    screen.blit(winrate_text, winrate_text_rect)
    screen.blit(game_played_text, game_played_text_rect)  
    if back.draw_button():
        menu_active=True
        history_button_active=False
    if previous.draw_button():
        u-=6
        v-=6
        if u<0:
            u=0
        if (v<6):
            v=6
    if next.draw_button():
        u+=6
        v+=6
        if v>=len(history_list):         
            v=len(history_list)
        if u>=len(history_list) - 6:
            u=len(history_list) - 6
    if len(history_list)!=0:
        for i in range(u,v,1):
            txt_surface = font.render(history_text[2+i%6].replace('\n',str(history_list[i])), True, (255,255,255))
            txt_surface_rect=txt_surface.get_rect(midtop=(640, 250 + (i%6)*(75)))
            screen.blit(txt_surface, txt_surface_rect)
    #Hàm cài đặt trong trò chơi
def setting_display():
    global menu_active, setting_button_active, dvl, switch_language, lg_count, lg_list, switch_resolution
    back=button(30,30,180,40,1,2.5,lg_list[14])
    volume_down=button(532,305,40,40,1,1.5,'-')
    volume_up=button(962,305,40,40,1,1.5,'+')
    more_lg=button(727,375,40,40,1,1.5,'...')
    language_choice=button(532,375,180,40,1,2.5,lg_list[0])
    more_rs=button(797,460,40,40,1,1.5,'...')
    resolution_choice=button(532,460,250,40,1,2.5,rs_list[0])
    volume_text=font.render(lg_list[60],True,(255,255,255))
    volume_text_rect=volume_text.get_rect(center=(400,322.5))   
    language_text=font.render(lg_list[62],True,(255,255,255))
    language_text_rect=language_text.get_rect(center=(415,392.5))
    resolution_text=font.render(lg_list[64],True,(255,255,255))
    resolution_text_rect=resolution_text.get_rect(center=(420,477.5))
    screen.blit(volume_text,volume_text_rect)   
    screen.blit(language_text,language_text_rect)
    screen.blit(resolution_text,resolution_text_rect)
    draw_rect(587,305,360,40,114,(0,0,0),22.5,'')
    if back.draw_button():
        menu_active=True
        setting_button_active=False
        switch_language=False
    if volume_up.draw_button():
        dvl+=0.1
        if dvl>1.0:
            dvl=1.0
        pygame.mixer.music.set_volume(dvl)
    if volume_down.draw_button():
        dvl-=0.1
        if dvl<0.0:
            dvl=0.0
        pygame.mixer.music.set_volume(dvl)
    for i in range(1,int(dvl*10)+1,1):
        draw_rect(587+(i-1)*36,305,36,40,115,(0,0,0),22.5,'')
    if language_choice.draw_button() or more_lg.draw_button(): 
        lg_count+=1     
        switch_language=True
        if lg_count>1:
            lg_count=0
            switch_language=False
    if resolution_choice.draw_button() or more_rs.draw_button(): 
        lg_count+=1
        switch_resolution=True
        if lg_count>1:
            lg_count=0
            switch_resolution=False
def switch_lg(list):
    for i in range(0,len(list),1):
        if i%2==0:
            b=list[i]
            list[i]=list[i+1]
            list[i+1]=b
    return list
def setting_language():
    global switch_language, lg_count, lg_list, switch_resolution, rs_count, info
    if switch_language:
        new_choice=button(532,415,180,40,1,2.5,lg_list[1])
        if new_choice.draw_button():
            lg_count=0
            switch_lg(lg_list)
            switch_lg(info)
            switch_language=False
    if switch_resolution:
        new_choice=button(532,500,250,40,1,5,rs_list[1])
        if new_choice.draw_button():
            lg_count=0
            for i in range(0,len(rs_list),1):
                if i%2==0:
                    a=rs_list[i]
                    rs_list[i]=rs_list[i+1]
                    rs_list[i+1]=a
            if rs_count==0:
                pygame.display.set_mode((1280,720),FULLSCREEN)
                rs_count=1
            else:
                pygame.display.set_mode((1280,720))
                rs_count=0
            switch_resolution=False
def shop_display():
    global menu_active, shop_button_active, buff_choice, buff, get_money
    buff_1=round_button(172,280,140,30,'Buff 1')
    buff_2=round_button(484,280,140,30,'Buff 2')
    buff_3=round_button(796,280,140,30,'Buff 3')
    buff_4=round_button(1108,280,140,30,'Buff 4')
    back=button(30,30,180,40,1,2.5,lg_list[14])
    draw_rect(315,30,650,80,111,(0,0,0),22.5,lg_list[66])
    money_text=font.render(f'${c.money}',True,"yellow")
    money_text_rect=money_text.get_rect(center=(1180,47.5))
    screen.blit(money_text,money_text_rect)
    if back.draw_button():
        menu_active=True
        shop_button_active=False
        buff_choice=False
        get_money=False
    if buff_1.draw_button():
        buff_choice=True
        buff=1
    if buff_2.draw_button():
        buff_choice=True
        buff=2
    if buff_3.draw_button():
        buff_choice=True
        buff=3
    if buff_4.draw_button():
        buff_choice=True
        buff=4
def buff_choosing():
    global buff_choice, buff_info, buff, shop_button_active, get_money, minigame_active, actual_buff
    buy=button(295,600,180,40,1,2.5,lg_list[68])
    cancel=button(505,600,180,40,1,2.5,lg_list[44])
    more_info=button(715,600,270,40,1,2.5,lg_list[46])
    if buff_choice:
        a=['First','Second','Third', 'Fourth']
        draw_rect(215,450,850,240,113,(0,0,0),30,lg_list[70].replace('\n',str(buff)))
        if buy.draw_button():
            if c.money<100:               
                buff=0
                get_money=True
                buff_choice=False          
            else:
                c.money-=100
                actual_buff=buff
                print(actual_buff)
                buff_choice=False
            
        if cancel.draw_button():
            buff_choice=False
            buff=0
        if more_info.draw_button():
            buff_info=True
            shop_button_active=False
            buff_choice=False
    if get_money:
        draw_rect(140,450,1000,240,113,(0,0,0),30,lg_list[72])
        minigame=button(290,600,300,40,1,2.5,lg_list[74])
        cancel=button(750,600,240,40,1,2.5,lg_list[44])
        if minigame.draw_button():
            minigame_active=True
            shop_button_active=False
            get_money=False
        if cancel.draw_button():
            get_money=False
            shop_button_active=True
def buff_information():
    global shop_button_active, buff_info, buff
    back=button(30,30,180,40,1,2.5,lg_list[14])
    screen.fill(255)
    if back.draw_button():
        shop_button_active=True
        buff_info=False
    inf=font.render((info[100+2*(buff-1)]),True, "black")
    inf_rect=inf.get_rect(center=(640,320))
    screen.blit(inf, inf_rect)
def minigame_display():
    global menu_active, minigame_active, font
    if minigame_active:
        back=button(30,30,180,40,1,2.5,lg_list[14])       
        minigame1=button(30,140,595,260,118,5,'')
        minigame2=button(655,140,595,260,121,5,'')
        minigame3=button(30,430,595,260,124,5,'')
        minigame4=button(655,430,595,260,127,5,'')
        draw_rect(415,30,450,80,111,(0,0,0),22.5,lg_list[76]) 
        if back.draw_button():
            menu_active=True
            minigame_active=False
        if minigame1.draw_button():
            c.money+=int(Dino_game.start())
        if minigame2.draw_button():
            c.money+=int(Minigame.start())
            pygame.display.set_mode((1280,720))    
        if minigame3.draw_button():
            c.money+=int(Car_Game.start())
            pygame.display.set_mode((1280,720))   
        if minigame4.draw_button():   
            c.money+=int(Snake_game.start())
            pygame.display.set_mode((1280,720))  
#Chạy menu
def menu():
    global menu_running
    menu_running=True
    pygame.mixer_music.load(r".\assets\music\menu_music.mp3")
    pygame.mixer_music.play(-1)
    while menu_running:
        clock.tick(60)       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(bg,(0,0))
        if menu_active: 
            game_name()
            menu_display()
        elif play_button_active:
            environment_display()
            evm_choosing()
        elif chr_set_active:
            character_set_display()
            chr_choosing()
        elif chr_set_info:
            chr_set_information()
        elif chr_info:
            chr_information()
        elif distance_active:
            distance_display()
            dis_choosing()
        elif history_button_active:
            history_display()
        elif setting_button_active:
            setting_display()
            setting_language()
        elif shop_button_active:
            shop_display()
            buff_choosing()
        elif buff_info:
            buff_information()
        elif minigame_active:
            minigame_display()
        pygame.display.update()