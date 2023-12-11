#Các biến sử dụng
text_x=640 #Vị trí x tiêu đề game
text_y=100 #Vị trí y tiêu đề game
dtext=-0.3 #Độ tăng giảm y tiêu đề game
menu_active=True #Kích hoạt menu
play_button_active=False #Kích hoạt nút Play(Chơi), hiện màn hình chọn môi trường
ev_choosing=False #Chọn môi trường
ev='' #Chỉ số môi trường(1,2,3)
chr_set_active=False #Hiện màn hình chọn set nhân vật
chr_set_choosing=False #Chọn set nhân vật
unit=0 #Biến trong set nhân vật
chr_set_info=False #Thông tin set nhân vật'
chr_set='' #Tên set nhân vật
chr_set_index=0 #Chỉ số set nhân vật(1,2,3,4,5)
chr_info=False #Thông tin nhân vật
chr=0 #Chỉ số nhân vật(1->25)
distance_active=False #Hiện màn hình chọn khoảng cách đường đua
distance_choosing=False #Chọn độ dài đường đua
distance='' #Độ dài đường đua đã chọn
actual_dis=0 #Chỉ số đường đua đã chọn
menu_running=True #Khởi tạo, tắt màn hình menu
history_button_active=False #Kích hoạt lịch sử trò chơi
u=0 #Biến trong history
v=6 #Biến trong history
dvl=1.0 #Biến độ tăng giảm âm lượng
setting_button_active=False #Kích hoạt cài đặt trò chơi
switch_language=False #Kích hoạt thay đổi ngôn ngữ
switch_resolution=False #Kích hoạt thay đổi kích thước màn hình
lg_count=0 #Biến thay đổi trạng thái hiển thị ngôn ngữ
rs_count=0 #Biến đếm index thay đổi màn hình
shop_button_active=False #Kích hoạt giao diện cửa hàng
buff_choice=False #Chọn buff cần mua
buff_info=False #Thông tin buff
buff=0 #Chỉ số buff
actual_buff=0 #Chỉ số buff đã mua
get_money=False #Kích hoạt minigame khi không đủ tiền trong shop
minigame_active=False #Kích hoạt minigame
clicked=False #Biến nhấp chuột trong class button
lg_list=['English','Tiếng Việt', #0
         'Play', 'Chơi', #2
         'History', 'Lịch Sử', #4
         'Setting', 'Cài đặt', #6
         'Quit', 'Thoát', #8
         'Shop', 'Cửa hàng', #10
         'Minigame', 'Trò chơi nhỏ', #12
         'Back','Quay lại', #14
         'Forest', 'Rừng rậm', #16 
         'Grassland', 'Thảo nguyên', #18
         'Sunset', 'Hoàng hôn', #20
         'Environment', 'Môi trường', #22
         'Yes', 'Có', #24
         'No', 'Không', #26
         'Confirm the selection of \n environment?','Xác nhận chọn môi trường \n?', #28
         'Confirm the selection of Animal Set','Xác nhận chọn Nhóm Động Vật', #30
         'Confirm the selection of Chibi Set','Xác nhận chọn Nhóm Người Tí Hon', #32
         'Confirm the selection of Medieval Set','Xác nhận chọn Nhóm Trung Cổ', #34
         'Confirm the selection of Monster Set','Xác nhận chọn Nhóm Quái Vật', #36
         'Confirm the selection of Car Set','Xác nhận chọn Nhóm Xe Hơi', #38
         'Character Set','Nhóm nhân vật', #40
         'Next', 'Tiếp tục', #42
         'Cancel','Hủy', #44
         'More Info','Thêm thông tin', #46
         'Short','Ngắn', #48
         'Medium','Trung bình', #50
         'Long', 'Dài', #52
         'Track lenght','Độ dài đường đua', #54
         'Confirm the selection of \n track length?', 'Xác nhận chọn đường đua \n', #56
         'Previous', 'Trước đó', #58
         'Volume', 'Âm lượng', #60
         'Language', 'Ngôn ngữ', #62
         'Resolution', 'Độ phân giải', #64
         'Choose the buff you need!', 'Chọn bùa tăng cường mà bạn cần!', #66
         'Buy', 'Mua', #68
         'Confirm the purchase of \n buff?', 'Xác nhận chọn bùa tăng cường \n?', #70
         "You don't have enough money, play minigame to get more!", 'Bạn không có đủ tiền, chơi trò chơi nhỏ để kiếm thêm!', #72
         'Play Minigame', 'Chơi trò chơi nhỏ', #74
         'Choose Minigame', 'Chọn trò chơi nhỏ', #76
         'Animal Set', 'Nhóm Động Vật', #78
         'Chibi Set', 'Nhóm Người Tí Hon', #80
         'Medieval Set', 'Nhóm Trung Cổ', #82
         'Monster Set', 'Nhóm Quái Vật', #84
         'Car Set', 'Nhóm Xe Hơi' #86
         ] 
character_name=['PyBird','PyCat','PyDog','PyBear','PyFox','PyChibi Archer','PyChibi Enchantress','PyChibi Knight','PyChibi Swordsman',
                'PyChibi Wizard','PyArcher','PyCommander','PyBlueKnight','PyRedKnight','PySamurai','PyKarasu Tengu','PyKitsune',
                'PyYamabushi Tengu','PyYurei','PyOgre','PyNo 2','PyNo 3','PyDestroyer','PyInfantryman','PySwordman','PyCarBao','PyCarDuy',
                'PyCarDanh','PyCarAn','PyCarBinh']
info=[r'.\Assets\Character_Info\animal\Bird\PyBird_Info0.png', r'.\Assets\Character_Info\animal\Bird\PyBird_Info1.png', r'.\Assets\Character_Info\animal\Bird\PyBird_Info2.png', r'.\Assets\Character_Info\animal\Bird\PyBird_Info3.png',
      r'.\Assets\Character_Info\animal\Cat\PyCat_Info0.png', r'.\Assets\Character_Info\animal\Cat\PyCat_Info1.png', r'.\Assets\Character_Info\animal\Cat\PyCat_Info2.png', r'.\Assets\Character_Info\animal\Cat\PyCat_Info3.png',
      r'.\Assets\Character_Info\animal\Dog\PyDog_Info0.png', r'.\Assets\Character_Info\animal\Dog\PyDog_Info1.png', r'.\Assets\Character_Info\animal\Dog\PyDog_Info2.png', r'.\Assets\Character_Info\animal\Dog\PyDog_Info3.png',
      r'.\Assets\Character_Info\animal\Bear\PyBear_Info0.png', r'.\Assets\Character_Info\animal\Bear\PyBear_Info1.png', r'.\Assets\Character_Info\animal\Bear\PyBear_Info2.png', r'.\Assets\Character_Info\animal\Bear\PyBear_Info3.png',
      r'.\Assets\Character_Info\animal\fox\PyFox_Info0.png', r'.\Assets\Character_Info\animal\fox\PyFox_Info1.png', r'.\Assets\Character_Info\animal\fox\PyFox_Info2.png', r'.\Assets\Character_Info\animal\fox\PyFox_Info3.png',
      r'.\Assets\Character_Info\chibi\Archer\PyChibiArcher_Info0.png', r'.\Assets\Character_Info\chibi\Archer\PyChibiArcher_Info1.png', r'.\Assets\Character_Info\chibi\Archer\PyChibiArcher_Info2.png', r'.\Assets\Character_Info\chibi\Archer\PyChibiArcher_Info3.png',
      r'.\Assets\Character_Info\chibi\Enchantress\PyChibiEnchantress_Info0.png', r'.\Assets\Character_Info\chibi\Enchantress\PyChibiEnchantress_Info1.png', r'.\Assets\Character_Info\chibi\Enchantress\PyChibiEnchantress_Info2.png', r'.\Assets\Character_Info\chibi\Enchantress\PyChibiEnchantress_Info3.png',
      r'.\Assets\Character_Info\chibi\Knight\PyChibiKnight_Info0.png', r'.\Assets\Character_Info\chibi\Knight\PyChibiKnight_Info1.png', r'.\Assets\Character_Info\chibi\Knight\PyChibiKnight_Info2.png', r'.\Assets\Character_Info\chibi\Knight\PyChibiKnight_Info3.png',
      r'.\Assets\Character_Info\chibi\Swordsman\PyChibiSwordsman_Info0.png', r'.\Assets\Character_Info\chibi\Swordsman\PyChibiSwordsman_Info1.png', r'.\Assets\Character_Info\chibi\Swordsman\PyChibiSwordsman_Info2.png', r'.\Assets\Character_Info\chibi\Swordsman\PyChibiSwordsman_Info3.png',
      r'.\Assets\Character_Info\chibi\Wizard\PyChibiWizard_Info0.png', r'.\Assets\Character_Info\chibi\Wizard\PyChibiWizard_Info1.png', r'.\Assets\Character_Info\chibi\Wizard\PyChibiWizard_Info2.png', r'.\Assets\Character_Info\chibi\Wizard\PyChibiWizard_Info3.png',
      r'.\Assets\Character_Info\medieval\archer\PyArcher_Info0.png', r'.\Assets\Character_Info\medieval\archer\PyArcher_Info1.png', r'.\Assets\Character_Info\medieval\archer\PyArcher_Info2.png', r'.\Assets\Character_Info\medieval\archer\PyArcher_Info3.png',
      r'.\Assets\Character_Info\medieval\commander\PyCommander_Info0.png', r'.\Assets\Character_Info\medieval\commander\PyCommander_Info1.png', r'.\Assets\Character_Info\medieval\commander\PyCommander_Info2.png', r'.\Assets\Character_Info\medieval\commander\PyCommander_Info3.png',
      r'.\Assets\Character_Info\medieval\knight_blue\PyBlueKnight_Info0.png', r'.\Assets\Character_Info\medieval\knight_blue\PyBlueKnight_Info1.png', r'.\Assets\Character_Info\medieval\knight_blue\PyBlueKnight_Info2.png', r'.\Assets\Character_Info\medieval\knight_blue\PyBlueKnight_Info3.png',
      r'.\Assets\Character_Info\medieval\knight_red\PyRedKnight_Info0.png', r'.\Assets\Character_Info\medieval\knight_red\PyRedKnight_Info1.png', r'.\Assets\Character_Info\medieval\knight_red\PyRedKnight_Info2.png', r'.\Assets\Character_Info\medieval\knight_red\PyRedKnight_Info3.png',
      r'.\Assets\Character_Info\medieval\samurai\PySamurai_Info0.png', r'.\Assets\Character_Info\medieval\samurai\PySamurai_Info1.png', r'.\Assets\Character_Info\medieval\samurai\PySamurai_Info2.png', r'.\Assets\Character_Info\medieval\samurai\PySamurai_Info3.png',
      r'.\Assets\Character_Info\monster\Karasu_tengu\PyKarasuTengu_Info0.png', r'.\Assets\Character_Info\monster\Karasu_tengu\PyKarasuTengu_Info1.png', r'.\Assets\Character_Info\monster\Karasu_tengu\PyKarasuTengu_Info2.png', r'.\Assets\Character_Info\monster\Karasu_tengu\PyKarasuTengu_Info3.png',
      r'.\Assets\Character_Info\monster\Kitsune\PyKitsune_Info0.png', r'.\Assets\Character_Info\monster\Kitsune\PyKitsune_Info1.png', r'.\Assets\Character_Info\monster\Kitsune\PyKitsune_Info2.png', r'.\Assets\Character_Info\monster\Kitsune\PyKitsune_Info3.png',
      r'.\Assets\Character_Info\monster\Yamabushi_tengu\PyYamabushiTengu_Info0.png', r'.\Assets\Character_Info\monster\Yamabushi_tengu\PyYamabushiTengu_Info1.png', r'.\Assets\Character_Info\monster\Yamabushi_tengu\PyYamabushiTengu_Info2.png', r'.\Assets\Character_Info\monster\Yamabushi_tengu\PyYamabushiTengu_Info3.png',
      r'.\Assets\Character_Info\monster\Yurei\PyYurei_Info0.png', r'.\Assets\Character_Info\monster\Yurei\PyYurei_Info1.png', r'.\Assets\Character_Info\monster\Yurei\PyYurei_Info2.png', r'.\Assets\Character_Info\monster\Yurei\PyYurei_Info3.png',
      r'.\Assets\Character_Info\monster\ogre\PyOgre_Info0.png', r'.\Assets\Character_Info\monster\ogre\PyOgre_Info1.png', r'.\Assets\Character_Info\monster\ogre\PyOgre_Info2.png', r'.\Assets\Character_Info\monster\ogre\PyOgre_Info3.png',
      r'.\Assets\Character_Info\car\1\PyCarAn_Info0.png', r'.\Assets\Character_Info\car\1\PyCarAn_Info1.png', r'.\Assets\Character_Info\car\1\PyCarAn_Info2.png', r'.\Assets\Character_Info\car\1\PyCarAn_Info3.png',
      r'.\Assets\Character_Info\car\2\PyCarBao_Info0.png', r'.\Assets\Character_Info\car\2\PyCarBao_Info1.png', r'.\Assets\Character_Info\car\2\PyCarBao_Info2.png', r'.\Assets\Character_Info\car\2\PyCarBao_Info3.png',
      r'.\Assets\Character_Info\car\3\PyCarBinh_Info0.png', r'.\Assets\Character_Info\car\3\PyCarBinh_Info1.png', r'.\Assets\Character_Info\car\3\PyCarBinh_Info2.png', r'.\Assets\Character_Info\car\3\PyCarBinh_Info3.png',
      r'.\Assets\Character_Info\car\4\PyCarDanh_Info0.png', r'.\Assets\Character_Info\car\4\PyCarDanh_Info1.png', r'.\Assets\Character_Info\car\4\PyCarDanh_Info2.png', r'.\Assets\Character_Info\car\4\PyCarDanh_Info3.png',
      r'.\Assets\Character_Info\car\5\PyCarDuy_Info0.png', r'.\Assets\Character_Info\car\5\PyCarDuy_Info1.png', r'.\Assets\Character_Info\car\5\PyCarDuy_Info2.png', r'.\Assets\Character_Info\car\5\PyCarDuy_Info3.png',
      'It is the buff 01, which can help your character with its First effect!', 'Đây là buff 1, thứ giúp bạn với hiệu ứng đầu tiên của nó',
      'It is the buff 02, which can help your character with its Second effect!', 'Đây là buff 2, thứ giúp bạn với hiệu ứng thứ hai của nó',
      'It is the buff 03, which can help your character with its Third effect!', 'Đây là buff 3, thứ giúp bạn với hiệu ứng thứ ba của nó',
      'It is the buff 04, which can help your character with its Fourth effect!', 'Đây là buff 4, thứ giúp bạn với hiệu ứng thứ tư của nó',
      ]
history_text = ['Winrate: \n%', 'Number of games played: \n', 'Time played: \n', 'Bet Character: \n', 'Rank: \n', 'Money Bet: $\n', 'Winning Bet Money: $\n', 'Lost Bet Money: $\n']
#history_list=['13:20:52', 'PyArcher', 1, 200, 600, 0, '00:20:52', 'PyBear', 2, 300, 0, 300, '07:07:07', 'PyChibi Acher', 5, 100, 0, 100, '22:52:52', 'PyOgre', 1, 300, 723, 0,]
history_list = []
rs_list=['1280x720','FULLSCREEN']
image_list=[r".\Assets\UI\Button\UI_Flat_Button_Large_Lock_01a1.png", r".\Assets\UI\Button\UI_Flat_Button_Large_Lock_01a2.png", r".\Assets\UI\Button\UI_Flat_Button_Large_Lock_01a3.png", #1
            r".\Assets\Environment\Forest\forest0.png", r".\Assets\Environment\Forest\forest1.png", r".\Assets\Environment\Forest\forest2.png", #4
            r".\Assets\Environment\Grassland\grassland0.png", r".\Assets\Environment\Grassland\grassland1.png", r".\Assets\Environment\Grassland\grassland2.png", #7
            r".\Assets\Environment\Sunset\sunset0.png", r".\Assets\Environment\Sunset\sunset1.png", r".\Assets\Environment\Sunset\sunset2.png", #10
            r".\Assets\Track_Distance\Short\forest_short0.png", r".\Assets\Track_Distance\Short\forest_short1.png", r".\Assets\Track_Distance\Short\forest_short2.png", #13
            r".\Assets\Track_Distance\Medium\forest_medium0.png", r".\Assets\Track_Distance\Medium\forest_medium1.png", r".\Assets\Track_Distance\Medium\forest_medium2.png", #16
            r".\Assets\Track_Distance\Long\forest_long0.png", r".\Assets\Track_Distance\Long\forest_long1.png", r".\Assets\Track_Distance\Long\forest_long2.png", #19
            r".\Assets\Character_Set_Image\Animal\Animal0.png", r".\Assets\Character_Set_Image\Animal\Animal1.png", r".\Assets\Character_Set_Image\Animal\Animal2.png", #22
            r".\Assets\Character_Set_Image\Chibi\Chibi0.png", r".\Assets\Character_Set_Image\Chibi\Chibi1.png", r".\Assets\Character_Set_Image\Chibi\Chibi2.png", #25
            r".\Assets\Character_Set_Image\Medival\medival0.png", r".\Assets\Character_Set_Image\Medival\medival1.png", r".\Assets\Character_Set_Image\Medival\medival2.png", #28
            r".\Assets\Character_Set_Image\Monster\Monster0.png", r".\Assets\Character_Set_Image\Monster\Monster1.png", r".\Assets\Character_Set_Image\Monster\Monster2.png", #31         
            r".\Assets\Character_Set_Image\Car\Car0.png", r".\Assets\Character_Set_Image\Car\Car1.png", r".\Assets\Character_Set_Image\Car\Car2.png", #34
            r".\Assets\char\animal\Bird\PyBird0.png", r".\Assets\char\animal\Bird\PyBird1.png", r".\Assets\char\animal\Bird\PyBird2.png", #37
            r".\Assets\char\animal\Cat\PyCat0.png", r".\Assets\char\animal\Cat\PyCat1.png", r".\Assets\char\animal\Cat\PyCat2.png", #40
            r".\Assets\char\animal\Dog\PyDog0.png", r".\Assets\char\animal\Dog\PyDog1.png", r".\Assets\char\animal\Dog\PyDog2.png", #43
            r".\Assets\char\animal\Bear\PyBear0.png", r".\Assets\char\animal\Bear\PyBear1.png", r".\Assets\char\animal\Bear\PyBear2.png", #46
            r".\Assets\char\animal\fox\PyFox0.png", r".\Assets\char\animal\fox\PyFox1.png", r".\Assets\char\animal\fox\PyFox2.png", #49
            r".\Assets\char\chibi\Archer\PyChibi_Archer0.png", r".\Assets\char\chibi\Archer\PyChibi_Archer1.png", r".\Assets\char\chibi\Archer\PyChibi_Archer2.png", #52
            r".\Assets\char\chibi\Enchantress\PyChibi_Enchantress0.png", r".\Assets\char\chibi\Enchantress\PyChibi_Enchantress1.png", r".\Assets\char\chibi\Enchantress\PyChibi_Enchantress2.png", #55
            r".\Assets\char\chibi\Knight\PyChibi_Knight0.png", r".\Assets\char\chibi\Knight\PyChibi_Knight1.png", r".\Assets\char\chibi\Knight\PyChibi_Knight2.png", #58
            r".\Assets\char\chibi\Swordsman\PyChibi_Swordsman0.png", r".\Assets\char\chibi\Swordsman\PyChibi_Swordsman1.png", r".\Assets\char\chibi\Swordsman\PyChibi_Swordsman2.png", #61
            r".\Assets\char\chibi\Wizard\PyChibi_Wizard0.png", r".\Assets\char\chibi\Wizard\PyChibi_Wizard1.png", r".\Assets\char\chibi\Wizard\PyChibi_Wizard2.png", #64
            r".\Assets\char\medieval\archer\PyArcher0.png", r".\Assets\char\medieval\archer\PyArcher1.png", r".\Assets\char\medieval\archer\PyArcher2.png", #67
            r".\Assets\char\medieval\commander\PyCommander0.png", r".\Assets\char\medieval\commander\PyCommander1.png", r".\Assets\char\medieval\commander\PyCommander2.png", #70
            r".\Assets\char\medieval\knight_blue\PyBlueKnight0.png", r".\Assets\char\medieval\knight_blue\PyBlueKnight1.png", r".\Assets\char\medieval\knight_blue\PyBlueKnight2.png", #73
            r".\Assets\char\medieval\knight_red\PyRedKnight0.png", r".\Assets\char\medieval\knight_red\PyRedKnight1.png", r".\Assets\char\medieval\knight_red\PyRedKnight2.png", #76
            r".\Assets\char\medieval\samurai\PySamurai0.png", r".\Assets\char\medieval\samurai\PySamurai1.png", r".\Assets\char\medieval\samurai\PySamurai2.png", #79
            r".\Assets\char\monster\Karasu_tengu\PyKarasu_Tengu0.png", r".\Assets\char\monster\Karasu_tengu\PyKarasu_Tengu1.png", r".\Assets\char\monster\Karasu_tengu\PyKarasu_Tengu2.png", #82
            r".\Assets\char\monster\Kitsune\PyKitsune0.png", r".\Assets\char\monster\Kitsune\PyKitsune1.png", r".\Assets\char\monster\Kitsune\PyKitsune2.png", #85
            r".\Assets\char\monster\Yamabushi_tengu\PyYamabushi_Tengu0.png", r".\Assets\char\monster\Yamabushi_tengu\PyYamabushi_Tengu1.png", r".\Assets\char\monster\Yamabushi_tengu\PyYamabushi_Tengu2.png", #88
            r".\Assets\char\monster\Yurei\PyYurei0.png", r".\Assets\char\monster\Yurei\PyYurei1.png", r".\Assets\char\monster\Yurei\PyYurei2.png", #91
            r".\Assets\char\monster\ogre\PyOgre0.png", r".\Assets\char\monster\ogre\PyOgre1.png", r".\Assets\char\monster\ogre\PyOgre2.png", #94
            r".\Assets\char\car\PyCarAn0.png", r".\Assets\char\car\PyCarAn1.png", r".\Assets\char\car\PyCarAn2.png", #97
            r".\Assets\char\car\PyCarBao0.png", r".\Assets\char\car\PyCarBao1.png", r".\Assets\char\car\PyCarBao2.png", #100
            r".\Assets\char\car\PyCarBinh0.png", r".\Assets\char\car\PyCarBinh1.png", r".\Assets\char\car\PyCarBinh2.png", #103
            r".\Assets\char\car\PyCarDanh0.png", r".\Assets\char\car\PyCarDanh1.png", r".\Assets\char\car\PyCarDanh2.png", #106
            r".\Assets\char\car\PyCarDuy0.png", r".\Assets\char\car\PyCarDuy1.png", r".\Assets\char\car\PyCarDuy2.png", #109
            r".\Assets\Menu_Background\title_frame0.png", r".\Assets\Menu_Background\title_frame1.png", r".\Assets\Menu_Background\query_frame.png", #112
            r".\Assets\Menu_Background\volume_frame.png", r".\Assets\Menu_Background\volume.png", r".\assets\Menu_Background\history_background.jpg", #115
            r".\Assets\minigame_image\minigame1_0.png", r".\Assets\minigame_image\minigame1_1.png", r".\Assets\minigame_image\minigame1_2.png", #118
            r".\Assets\minigame_image\minigame2_0.png", r".\Assets\minigame_image\minigame2_1.png", r".\Assets\minigame_image\minigame2_2.png", #121
            r".\Assets\minigame_image\minigame3_0.png", r".\Assets\minigame_image\minigame3_1.png", r".\Assets\minigame_image\minigame3_2.png", #124
            r".\Assets\minigame_image\minigame4_0.png", r".\Assets\minigame_image\minigame4_1.png", r".\Assets\minigame_image\minigame4_2.png", #127
            r".\assets\Menu_Background\history_list1.jpg",]