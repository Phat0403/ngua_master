


import ast,pygame
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pygame, sys, random, button


WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 675

GREEN = (13, 255, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 3, 3)
GRAY = (80, 80, 80)
WHITE = (255, 255, 255)



clock = pygame.time.Clock()
FPS = 60


class Horse(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y, type, ran, group):
		super().__init__()
		self.has_boost = False
		self.type = type
		self.speed = ran
		self.animate_fps = .4
		self.sprites = []
		for i in range(7):
			image = pygame.image.load(f"./asset/character/horse{main_game.index + 1}/{self.type}/{i + 1}.png")
			scale = image.get_width() / image.get_height()
			image = pygame.transform.scale(image, (scale * 150, 150))
			self.sprites.append(image)
		
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]
		self.rect = self.image.get_rect()
		self.rect.bottomleft = (pos_x, pos_y)
		self.positonx = pos_x
		self.group = group
	
	def update(self, bua):
		if self.rect.right == main_game.rect_bua.left:
			main_game.showbua = False
		
		if self.rect.right <= WINDOW_WIDTH:
			
			self.positonx += (self.speed) * bua + 1
			
			self.rect.x = (self.positonx)
			
			self.animate(self.animate_fps)
		else:
			
			for ngua in self.group.sprites():
				if ngua == self:
					continue
				if not ngua.has_boost:
					ngua.speed += 2
					ngua.has_boost = True
			# main_game.rank.append(self)
			if len(main_game.rank) >= 1:
				main_game.speed_map = main_game.stop_map
	
	def animate(self, fps):
		self.current_sprite += fps
		if self.current_sprite >= 6:
			self.current_sprite = 0
		self.image = self.sprites[int(self.current_sprite)]
class Button1():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.hover=(x,y)
        self.unhover=(x,y+3)
        self.clicked = False

    def draw(self, surface):
        action = False
		#get mouse position
        pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            self.rect.topleft=self.hover
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        else: 
            self.rect.topleft=self.unhover

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

		#draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action


class Game():
	def __init__(self):

		
		self.WINDOW_WIDTH = 1200
		self.WINDOW_HEIGHT = 675
		
		# hinh anh background
		background = pygame.image.load('./asset/img/cloud.png')
		scale = background.get_width() / background.get_height()
		self.background = pygame.transform.scale(background, (scale * 1200, 700))
		img_bua = pygame.image.load(f"./asset/bua/bua.png")
		self.img_bua = pygame.transform.scale(img_bua, (100, 100))
		self.rect_bua = self.img_bua.get_rect()
		#ngua
		HORSE1 = [
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse1/1/4.png"), (100, 100)), "ten1_1"],
			# tự đổi tên chỗ đây
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse1/2/4.png"), (100, 100)), "ten1_2"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse1/3/4.png"), (100, 100)), "ten1_3"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse1/4/4.png"), (100, 100)), "ten1_4"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse1/5/4.png"), (100, 100)), "ten1_5"]
		]
		# set 2
		HORSE2 = [
            [pygame.transform.scale(pygame.image.load(r"asset/character/horse2/1/4.png"), (100, 100)), "ten2_1"],
            [pygame.transform.scale(pygame.image.load(r"asset/character/horse2/2/4.png"), (100, 100)), "ten2_2"],
            [pygame.transform.scale(pygame.image.load(r"asset/character/horse2/3/4.png"), (100, 100)), "ten2_3"],
            [pygame.transform.scale(pygame.image.load(r"asset/character/horse2/4/4.png"), (100, 100)), "ten2_4"],
            [pygame.transform.scale(pygame.image.load(r"asset/character/horse2/5/4.png"), (100, 100)), "ten2_5"]
		]
		# set /
		HORSE3 = [
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse3/1/4.png"), (100, 100)), "ten3_1"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse3/2/4.png"), (100, 100)), "ten3_2"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse3/3/4.png"), (100, 100)), "ten3_3"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse3/4/4.png"), (100, 100)), "ten3_4"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse3/5/4.png"), (100, 100)), "ten3_5"]
		]
		HORSE4 = [
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse4/1/4.png"), (100, 100)), "ten4_1"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse4/2/4.png"), (100, 100)), "ten4_2"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse4/3/4.png"), (100, 100)), "ten4_3"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse4/4/4.png"), (100, 100)), "ten4_4"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse4/5/4.png"), (100, 100)), "ten4_5"]
		]
		HORSE5 = [
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse5/1/4.png"), (100, 100)), "ten5_1"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse5/2/4.png"), (100, 100)), "ten5_2"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse5/3/4.png"), (100, 100)), "ten5_3"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse5/4/4.png"), (100, 100)), "ten5_4"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse5/5/4.png"), (100, 100)), "ten5_5"]
		]
		self.HORSE = [HORSE1, HORSE2, HORSE3, HORSE4,HORSE5]
		# Bua
		self.showbua = True
		self.rank = []
		self.bua_x = []
		self.list_horse = []
		for i in range(0, 5):
			self.bua_x.append(random.randint(200, 800))
		# tien
		
		self.coin = 30
		#tien cuoc
		self.coin_bet=30
		# loai ngua
		self.index = 0
		# loai map
		self.map = 0
		# chay map
		self.stop_map = 0
		self.speed_map = 2
		
		#
		self.menu_music = pygame.mixer.Sound("./asset/sound/music.mp3")
		self.menu_music.set_volume(.2)
	
	def load_bg(self):
		self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
		self.menu_music.play(-1)
		img1 = pygame.image.load('./asset/img/bg1.png')
		background = pygame.transform.scale(img1, (1200, 800))
		img2 = pygame.image.load('./asset/img/cloud.png')
		cloud = pygame.transform.scale(img2, (1200, 600))
		img_button_start = pygame.image.load('./asset/img/button_start.png')
		button_start = pygame.transform.scale(img_button_start, (200, 100))
		button_start = button.Button(610, 150, 1, button_start)
		img_button_setting = pygame.image.load('./asset/img/button_setting.png')
		button_setting = pygame.transform.scale(img_button_setting, (240, 90))
		button_setting = button.Button(607, 280, 1, button_setting)
		running = True
		cloud_x = 0
		
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					pos = pygame.mouse.get_pos()
					if button_start.rect.collidepoint(pos):
						self.option_horse()
					
					if button_setting.rect.collidepoint(pos):
						print('danh')
			
			self.screen.blit(cloud, (cloud_x, -50))
			self.screen.blit(cloud, (cloud_x + 1170, -50))
			
			cloud_x -= 1
			self.screen.blit(background, (0, -125))
			if cloud_x == -1170:
				cloud_x = 0
			button_start.draw(self.screen)
			button_setting.draw(self.screen)
			pygame.display.update()
	
	def option_horse(self):
		running = True
		RECT = pygame.transform.scale(pygame.image.load(r"asset/img/rect.png"), (120, 120))
		RECT_hover = pygame.transform.scale(pygame.image.load(r"asset/img/rect.png"), (120, 120))
		START_BTN = button.Button(610, 600, 0.3, pygame.image.load(r"asset/img/button_start.png"))
		
		# tự đổi map chỗ đây
		MAP = [
			pygame.transform.scale(pygame.image.load(r"asset/map/map1.png"), (400, 200)),  # MAP1
			pygame.transform.scale(pygame.image.load(r"asset/map/map2.png"), (400, 200)),  # MAP2
			pygame.transform.scale(pygame.image.load(r"asset/map/map3.png"), (400, 200)),  # MAP3
			pygame.transform.scale(pygame.image.load(r"asset/map/map4.png"), (400, 200)),  # MAP4
			pygame.transform.scale(pygame.image.load(r"asset/map/map5.png"), (400, 200))   # MAP5
		]
		# set 1
		# tự chọn con ngựa khác cũng đc
		
		
		button_go_back = button.Button(50, 50, 0.1, pygame.image.load(r"asset/button/go_back.png"))
		button_shop = button.Button(100, 600, 0.4, pygame.image.load(r"asset/img/shop.png"))
		
		BG_x = 0
		
		rect_x = 260
		rect_y = 200
		
		horse_btn = []
		
		for i in range(0, 5):
			temp = button.Button_Horse(rect_x + 60 + 10, rect_y + 60 + 10, 1, self.HORSE[self.index][i][0])
			horse_btn.append(temp)
			rect_x += 150
		
		#CLick variable
		has_click_horse = False
		
		user_text = f"{min(30, int(self.coin) // 2)}"
		font = pygame.font.Font("./asset/img/SourceCodePro-Black.ttf", 24)
		coin_text = font.render(f'COIN: {self.coin}', True, YELLOW)
		coin_text_rect = coin_text.get_rect()
		coin_text_rect.topright = (WINDOW_WIDTH - 20, 20)
		
		bet_text = font.render(f' BET: {user_text}', True, YELLOW)
		
		bet_text_rect = bet_text.get_rect()
		bet_text_rect.left = .36 * WINDOW_WIDTH
		bet_text_rect.centery = .22 * WINDOW_HEIGHT
		
		text_box = pygame.Rect(1, 1, WINDOW_WIDTH // 3.5,
		                       WINDOW_HEIGHT // 12)
		text_box.centerx = WINDOW_WIDTH // 2
		text_box.centery = .22 * WINDOW_HEIGHT
		
		color = YELLOW
		active = False
		error = False
		
		while running:
			clock.tick(60)
			
			#error bet
			error = (len(user_text) >= 15) or (not user_text.isdigit()) or (int(user_text) <= 0) or (
					int(user_text) > int(self.coin))
			
			if active:
				if error:
					color = RED
				else:
					color = GREEN
			else:
				color = YELLOW
				
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				
				if event.type == pygame.KEYDOWN:
					if active:
						if event.key == pygame.K_BACKSPACE:
							user_text = user_text[0: -1]
						else:
							if len(user_text) <= 16 and event.unicode.isdigit():
								user_text += event.unicode
					if 	user_text!='':		
						self.coin_bet=int(user_text)
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					pos = pygame.mouse.get_pos()
					for i in range(5):
						if horse_btn[i].rect.collidepoint(pos):
							self.bet = i + 1
							horse_btn[i].click = True
							has_click_horse = True
							for horse in horse_btn:
								if horse != horse_btn[i]:
									horse.click = False
									
					# Check Click Box
					if text_box.collidepoint(pos):
						active = True
					else:
						active = False
						
					if button_go_back.rect.collidepoint(event.pos):
						running = False
					# right_map
					# shopping
					if button_shop.rect.collidepoint(event.pos):
						self.shop()
					if pygame.Rect((829, 380), (130, 130)).collidepoint(event.pos):
						if self.map == 4:
							self.map = 0
						else:
							self.map += 1
					# left_map
					if pygame.Rect((330, 380), (130, 130)).collidepoint(event.pos):
						if self.map == 0:
							self.map = 4
						else:
							self.map -= 1
					# right_chose_hourse
					if pygame.Rect((1000, 182), (100, 100)).collidepoint(event.pos):
						if self.index == 4:
							self.index = 0
						else:
							self.index += 1
						for i, btn in enumerate(horse_btn):
							btn.image = self.HORSE[self.index][i][0]
						
					
					# left_chose_hourse
					if pygame.Rect((182, 190), (100, 100)).collidepoint(event.pos):
						if self.index == 0:
							self.index = 4
						else:
							self.index -= 1
						for i, btn in enumerate(horse_btn):
							btn.image = self.HORSE[self.index][i][0]
					
					if not error and pygame.Rect((490, 580), (250, 100)).collidepoint(event.pos) and has_click_horse==True:
						# LẤY GIÁ TRỊ MAP VỚI 5 CON NGỰA VÀ TÊN 5 CON NGỰA ĐỂ HIỂN THỊ ĐƯỜNG ĐUA TƯƠNG ỨNG
						self.maingame()
			#
			
			rect_x = 260
			rect_y = 200
			
			
			
			self.screen.blit(pygame.transform.scale(pygame.image.load("./asset/img/cloud.png").convert(), (1200, 900)),
			                 (BG_x, 0))
			
			for i in range(0, 5):
				horse_btn[i].draw(self.screen)
				# tên 5 con ngựa
				self.screen.blit(
					pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 20).render(f'{self.HORSE[self.index][i][1]}',
					                                                                  True, (246, 142, 2)),
					(rect_x + 20, rect_y - 25))
				rect_x += 150
			self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 100).render(f'<', True, (246, 142, 2)),
				(182, 190))  # đổi màu nút left tại đây
			self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 100).render(f'>', True, (246, 142, 2)),
				(1000, 190))  # có thể đổi màu
			self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 50).render(f'TÙY CHỈNH CHẾ ĐỘ', True,
				                                                                  (246, 142, 2)),
				(370, 50))  # có thể đổi màu
			self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 130).render(f'<', True, (246, 142, 2)),
				(330, 350))  # có thể đổi màu
			self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 130).render(f'>', True, (246, 142, 2)),
				(829, 350))  # có thể đổi màu
			
			self.screen.blit(MAP[self.map], (420, 350))
			self.screen.blit(MAP[self.map], (420, 350))
			START_BTN.draw(self.screen)
			button_go_back.draw(self.screen)
			button_shop.draw(self.screen)
			self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 50).render(f'SHOP', True, (246, 142, 2)),
				(50, 450))
			
			#rerender
			bet_text = font.render(f' BET: {user_text}', True, YELLOW)
			coin_text = font.render(f'COIN: {self.coin}', True, YELLOW)
			
			# blit bet
			self.screen.blit(bet_text, bet_text_rect)
			self.screen.blit(coin_text, coin_text_rect)
			pygame.draw.rect(self.screen, color, text_box, 3)
			
			pygame.display.update()

	def shop(self):
		self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
		background = pygame.image.load('./asset/img/background.png').convert() 
		#font for betting box
		base_font = pygame.font.Font(None,32)

		
		#create button
		item1 = pygame.image.load("./asset/img/bua1.png").convert()
		item2 = pygame.image.load("./asset/img/bua2.png").convert()
		#back = pygame.image.load("item1.png").convert_alpha()
		coin = pygame.image.load("./asset/img/coin.png").convert_alpha()
		cost1 = pygame.image.load("./asset/img/cost1.png").convert_alpha()
		cost2 = pygame.image.load("./asset/img/cost2.png").convert_alpha()
		cost1_1 = pygame.image.load("./asset/img/cost11.png").convert_alpha()
		cost2_1 = pygame.image.load("./asset/img/cost22.png").convert_alpha()
		#scale
		background = pygame.transform.scale(background,(1200,800))
		item1 = pygame.transform.scale(item1,(300,350))
		item2 = pygame.transform.scale(item2,(300,350))
		coin = pygame.transform.scale(coin,(50,50))
		cost1 = pygame.transform.scale(cost1,(200,100))
		cost2 = pygame.transform.scale(cost2,(200,100))
		cost1_1 = pygame.transform.scale(cost1_1,(100,50))
		cost2_1 = pygame.transform.scale(cost2_1,(100,50))
		#create Button instance
		cost1_button = Button1(250, 600,cost1 , 0.5)
		cost2_button = Button1(850,600, cost2, 0.5)
		#attention
		button_go_back=button.Button(50,50,0.1,pygame.image.load(r"asset/button/go_back.png"))

		#loop
		count1 = 0
		count2 = 0
		self.number1=0
		self.number2=0
		run = True
		while run:
        
			self.screen.blit(background,(0,0))
			self.screen.blit(item1, (150,200))
			self.screen.blit(item2, (750,200))
			self.screen.blit(coin, (1150,0))
			temp = int(self.coin)
			
			if cost1_button.draw(self.screen) and count1 == 0:
				self.coin = (temp-10)
				self.number1+=1
			if cost2_button.draw(self.screen) and count2 == 0:
				self.coin = (temp-20)
				self.number2+=1
			if temp < 10:
				self.screen.blit(cost1_1,(250,600))
				count1 += 1
			if temp < 20:
				self.screen.blit(cost2_1,(850,600))
				count2 +=1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
				if event.type==pygame.MOUSEBUTTONDOWN:
					if button_go_back.rect.collidepoint(event.pos):
						run = False
			
			coin_surface = base_font.render(str(self.coin), True, (255,255,255))
			self.screen.blit(coin_surface,(1120,14))
			button_go_back.draw(self.screen)
			for i in range(1,10):
				if self.number1==i:
					self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 30).render(f'x{self.number1}', True,
				                                                                  (246, 142, 2)),
				(150, 500))
				if self.number2==i:
					self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 30).render(f'x{self.number2}', True,
				                                                                  (246, 142, 2)),
				(750, 500))
		
			pygame.display.update()
# đặt cược

	def maingame(self):
		self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
		print(main_game.index)
		self.menu_music.stop()
		ran = random.randint(2, 100) / 100
		horse_group = pygame.sprite.Group()
		horse1 = Horse(0, 260 + 110 * 0, 0 + 1, ran, horse_group)
		horse_group.add(horse1)
		ran = random.randint(2, 100) / 100
		horse2 = Horse(0, 260 + 110 * 1, 1 + 1, ran, horse_group)
		horse_group.add(horse2)
		ran = random.randint(2, 100) / 100
		horse3 = Horse(0, 260 + 110 * 2, 2 + 1, ran, horse_group)
		horse_group.add(horse3)
		ran = random.randint(2, 100) / 100
		horse4 = Horse(0, 260 + 110 * 3, 3 + 1, ran, horse_group)
		horse_group.add(horse4)
		ran = random.randint(2, 100) / 100
		horse5 = Horse(0, 260 + 110 * 4, 4 + 1, ran, horse_group)
		horse_group.add(horse5)
		racing = True
		dem = 0
		horse_x = [0, 0, 0, 0, 0]
		hidden = [True, True, True, True, True]  # hidden của bùa
		active = [False, False, False, False, False]  # trạng thái kích hoạt bùa
		horse = [horse1, horse2, horse3, horse4, horse5]  # lấy ra 5 con ngụaư cho dễ gọi vòng for
		bua = [3, 0.5, 0, -100, 100, 500]
		# tăng tốc
		# giảm tốc
		# choáng
		# tốc biến ngược
		# tốc biến until
		# về đích
		bua_get = [1, 1, 1, 1, 1, 1]  # bùa tạm thời
		end_bua = [0, 0, 0, 0, 0, 0]  # đêm vòng lặp để kết thúc trạng thái bùa
		bua_input = [1, 1, 1, 1, 1, 1]  # bùa truyền con ngựa
		end_horse = [False, False, False, False, False]  # trạng thái về đích của ngựa
		font = pygame.font.Font("./asset/img/SourceCodePro-Black.ttf", 24)
		coin_text = font.render(f'COIN: {self.coin}', True, YELLOW)
		coin_text_rect = coin_text.get_rect()
		coin_text_rect.topright = (WINDOW_WIDTH - 20, 20)
		while racing:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			
			image = pygame.image.load(f'./asset/map/map{self.map + 1}.png')
			scale = image.get_width() / image.get_height()
			
			image_map = pygame.transform.scale(image, (scale * 800, 675))
			self.screen.blit(self.background, (0, 0))
			self.speed_map -= 2
			
			self.screen.blit(image_map, (self.speed_map, 0))
			self.screen.blit(image_map, (self.speed_map + 600, 0))
			self.screen.blit(image_map, (self.speed_map + 600 * 2, 0))
			
			if self.speed_map == -600:
				self.speed_map = 0
			# =========
			for index, horse in enumerate(horse_group.sprites()):
				horse.update(bua_input[index])
				horse_x[index] = horse.positonx
			
			'''horses1.update(bua_input[0])
			horse_x[0] = horse1.positonx
			horses2.update(bua_input[1])
			horse_x[1] = horse2.positonx
			horses3.update(bua_input[2])
			horse_x[2] = horse3.positonx
			horses4.update(bua_input[3])
			horse_x[3] = horse4.positonx
			horses5.update(bua_input[4])
			horse_x[4] = horse5.positonx'''
			
			for i in range(5):
				# kích hoạt bùa và ẩn hình ảnh bùa
				if (horse_x[i] + 50) >= self.bua_x[i] and hidden[i]:
					hidden[i] = False
					active[i] = True
					bua_get[i] = random.randint(0, 5)  # random  bùa nhận được
			for i in range(5):
				if active[i] and int(end_bua[i]) <= 160:  # kiểm tra điều kiện kích hoạt bùa
					if 3 <= bua_get[i] <= 4:
						horse_group.sprites()[i].positonx += bua[bua_get[i]]
						end_bua[i] = 170
					
					elif bua_get[i] == 5:
						horse_group.sprites()[i].positonx = bua[bua_get[i]]
						end_bua[i] = 170
					else:
						bua_input[i] = bua[bua_get[i]]
						end_bua[i] += 1
				elif end_bua[i] > 20:
					bua_input[i] = 1
				if horse_group.sprites()[i].rect.right >= WINDOW_WIDTH and (not end_horse[i]):
					self.rank.append(i)
					end_horse[i] = True
					print(self.rank)
			if len(self.rank) == 5:
				self.end()
			# =============
			horse_group.draw(self.screen)
			for i in range(1, 6):
				if self.showbua and hidden[i - 1]:
					self.screen.blit(self.img_bua, (self.bua_x[i - 1], 40 + i * 105))
			
			pygame.draw.rect(self.screen,GRAY,(1035,5,150,60),100,0)
			self.screen.blit(coin_text, coin_text_rect)
			pygame.display.flip()
			clock.tick(60)
	def end(self):
		self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
		ending=True
		if self.bet==self.rank[0]+1:
			self.coin+=self.coin_bet
		else:
			self.coin-=self.coin_bet
		font = pygame.font.Font("./asset/img/SourceCodePro-Black.ttf", 24)
		coin_text = font.render(f'COIN: {self.coin}', True, YELLOW)
		coin_text_rect = coin_text.get_rect()
		coin_text_rect.topright = (WINDOW_WIDTH - 20, 20)
		img_button_start = pygame.image.load('./asset/img/button_start.png')
		button_start = pygame.transform.scale(img_button_start, (200, 100))
		button_start = button.Button(1000, 600, 1, button_start)
		self.coin_after=self.coin
		
		
		
		while ending:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					pos = pygame.mouse.get_pos()
					if button_start.rect.collidepoint(pos):
						self.rank=[]
						self.load_bg()
			self.screen.blit(pygame.transform.scale(self.background,(1200,800)),(0,0))
			# hạng 1
			self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 100).render(f'1: ', True, GRAY),
				(50, 50))
			self.screen.blit(pygame.transform.scale(pygame.image.load(f"./asset/character/horse{self.index+1}/{self.rank[0]+1}/1.png"),(100,100)), (200,50))
			#hạng 2
			self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 100).render(f'2: ', True, GRAY),
				(50, 150))
			self.screen.blit(pygame.transform.scale(pygame.image.load(f"./asset/character/horse{self.index+1}/{self.rank[1]+1}/1.png"),(100,100)), (200,150))
			#hạng 3
			self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 100).render(f'3: ', True, GRAY),
				(50, 250))
			self.screen.blit(pygame.transform.scale(pygame.image.load(f"./asset/character/horse{self.index+1}/{self.rank[2]+1}/1.png"),(100,100)), (200,250))
			#hạng 4
			self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 100).render(f'4: ', True, GRAY),
				(50, 350))
			self.screen.blit(pygame.transform.scale(pygame.image.load(f"./asset/character/horse{self.index+1}/{self.rank[3]+1}/1.png"),(100,100)), (200,350))
			#hạng 5
			self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 100).render(f'5: ', True, GRAY),
				(50, 450))
			self.screen.blit(pygame.transform.scale(pygame.image.load(f"./asset/character/horse{self.index+1}/{self.rank[4]+1}/1.png"),(100,100)), (200,450))

			if self.bet==self.rank[0]+1:
				self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 50).render(f'YOU WON', True, GRAY),
				(450, 100))
				
			else: 
				self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 50).render(f'DEFEAT', True, GRAY),
				(450, 100))
				
			
			self.screen.blit(coin_text, coin_text_rect)
			button_start.draw(self.screen)
			pygame.display.update()


pygame.init()
main_game = Game()




root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#95a5a6")
root.resizable(False,False)
#hình nền của đăng nhập
path='./login.png'
img = Image.open(path)
img = img.resize((450, 500), 	Image.Resampling.LANCZOS)
test = ImageTk.PhotoImage(img)
Label(root, image=test, bg='#95a5a6').place(x=0, y=0)
#@@@@@@@@@@@@@@@@@@@
frame=Frame(root,width=350, height=350, bg='white')
frame.place(x=480, y=70)
heading=Label(frame,text='LOGIN',fg='#57a18f',bg='white',font=('Comic Sans MS',23, 'bold'))
heading.place(x=120,y=5)



#######################################____________________________
def signin():
	username=user.get()
	password=code.get()	
	file =open('datasheet.txt', 'r')
	d=file.read()
	r=ast.literal_eval(d)
	file.close()
	main_game.coin=(r['coin '+username])
    
    
    
    # print(r.keys())
    # print(r.values()) 
	if username in r.keys() and password==r[username]:
		root.destroy()
		pygame.init()
		main_game.load_bg()
		
		
        
	else:
		messagebox.showerror('Invalid','Invalid username or password')

def signup_command():
                  #Dang ki
	window=Toplevel(root)
	window.title('Sign Up')
	window.geometry('925x500+300+200')
	window.configure(bg="#95a5a6")
	window.resizable(False,False)
    
	def signup():
		username=user.get()
		password=code.get()
		conform=conform_code.get()
		gold='coin '+username
		if password==conform:
			try:

				file=open('datasheet.txt','r+')
				d=file.read()
				r=ast.literal_eval				
				dict2={username:password,'coin '+username:200}
				r.update(dict2)
				file.truncate(0)
				file.close				
				file=open('datasheet.txt','w')
				w=file.write(str(r))
				messagebox.showinfo('Signup','Sucessfully sign up')
				window.destroy()
			except:
				file=open('datasheet.txt','w')
				pp=str({'Username':'Password'})
				file.write(pp)
				file.close()
		else:
			messagebox.showerror('Invalid','Both Password should match')
	
	def sign():
		window.destroy()
	signup.gold
    #hiÌ€nh nÃªÌ€n cuÌ‰a Ä‘Äƒng nhÃ¢Ì£p
	path='./signup.png'
	img1 = Image.open(path)
	img1 = img1.resize((450, 500), 	Image.Resampling.LANCZOS)
	test1 = ImageTk.PhotoImage(img1)
	Label(window, image=test1, bg='#95a5a6').place(x=0, y=0)

	frame=Frame(window, width=350, height=350, bg='white')
	frame.place(x=480,y=50)	
	heading=Label(frame, text='Sign up', fg='#57a1f8', bg='white', font=('Comic Sans MS',23, 'bold'))
	heading.place(x=120,y=5)
	################------------------------1
	def on_enter(e):
		user.delete(0,'end')
	def on_leave(e):
		if user.get()=='':
			user.insert(0,'Username')
	user=Entry(frame, width=25, fg='black',border=0,bg='white', font=('Comic Sans MS',11))
	user.place(x=30,y=80)
	user.insert(0, 'Username')
	user.bind('<FocusIn>',on_enter)
	user.bind('<FocusOut>',on_leave)	
	Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
	################------------------------2
	def on_enter(e):
		code.delete(0,'end')
	def on_leave(e):
		if code.get()=='':
			code.insert(0,'Password')
	code=Entry(frame, width=25, fg='black',border=0,bg='white' ,font=('Comic Sans MS',11))
	code.place(x=30,y=150)
	code.insert(0, 'Password')
	code.bind('<FocusIn>',on_enter)
	code.bind('<FocusOut>',on_leave)

	Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
	################------------------------3
	def on_enter(e):
		conform_code.delete(0,'end')
	def on_leave(e):
		if conform_code.get()=='':
			conform_code.insert(0,'Conform password')
	conform_code=Entry(frame, width=25, fg='black',border=0,bg='white', font=('Comic Sans MS',11))
	conform_code.place(x=30,y=220)
	conform_code.insert(0, 'Conform password')
	conform_code.bind('<FocusIn>',on_enter)
	conform_code.bind('<FocusOut>',on_leave)

	Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

    ################------------------------
	Button(frame,width=39,pady=7,text='Sign up',bg='#57a1f8',command=signup,border=0).place(x=35,y=280)
	label=Label(frame,text='I have an account ? ', fg='black',bg='white', font=('Comic Sans MS',9))
	label.place(x=90,y=320)	
	signin=Button(frame,width=6,text='Sign in', border=0,bg='white',cursor='hand2',command=sign,fg='#57a1f8')
	signin.place(x=200,y=320)
	################------------------------	
	window.mainloop()


#het phan dang ki
##########--------------------
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
user=Entry(frame, width=25, fg='black',border=0,bg='white',font=('Comic Sans MS',11))
user.place(x=30,y=80)
user.insert(0,'User name')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2, bg='black').place(x=25,y=107)

###########---------------------------------
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')
code=Entry(frame, width=25, fg='black',border=0,bg='white',font=('Comic Sans MS',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2, bg='black').place(x=25,y=177)

###########-----------------------------------------

Button(frame,width=39,pady=7, text='Sign in',bg='#57a1f8',fg='black',command=signin,border=0).place(x=35, y=204)
label1=Label(frame,text="Don't have account ?",fg='black',bg='white',font=('cambria',9))
label1.place(x=75,y=270)

sign_up=Button(frame,width=6, text='Sign Up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup_command)
sign_up.place(x=215,y=270)
root.mainloop()
