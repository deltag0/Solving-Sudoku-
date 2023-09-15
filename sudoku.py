import pygame
import random
from collections import Counter 
starting_nums = []
track = []
ctn = False
used = []
colNum = None #used to detect which row 
rowNum = None	
good = True
check = True
rows_confirm = False
columns_confirm = False
c = 0
plop = []
used_total = []
banned = []
banned2 = []
plop2 = []
alt = True
clop = 0
coords = {}
y = 0
x = 0
val = 1
pair = True
row_count = 0
ini = 1
inc = 1
prev = []
leave = None
weird = [1,2,3,4,5,6,7,8,9]
weird_count = 0
dp = {}

pected = [3, 2, 1, 2, 3, 2, 1, 2, 1]
ex = pected[0]
returned = None
for _ in range(81):

	coords[(x,y)] = val
	val += 1
	x += 1
	if x == 9:
		x-=9
		y+=1    # (0,1) = 9
		

#print(coords)




def changColor(image, color):
    colouredImage = pygame.Surface(image.get_size())
    colouredImage.fill(color)
    
    finalImage = image.copy()
    finalImage.blit(colouredImage, (0, 0), special_flags = pygame.BLEND_MULT)
    return finalImage

def sample(l):
	global c, plop
	while True:
		
		v = None
		if clop == 9 and c == 1:
			break
		if clop == 7 and c == 1:
			break
		if clop == 3 and c == 1:
			break
		if c == 3 and clop == 1:
			break
		if c == 2 and clop == 2:
			break
		if c == 2 and clop == 4:
			break	
		if c == 3 and clop == 5:
			break	
		if c == 2 and clop == 6:
			break	
		if c == 2 and clop == 8:
			break				
		i = random.randrange(0,8)

		if i in used:
			con = False
		else:
			con = True
		for x in range(len(columns)):
			if l[i] in columns[x]:
				plop.append(x)
				v = x
				break
		
		for x in range(len(rows)):
			if l[i] in rows[x]:
				plop2.append(x)
				p = x
				break
		for x in list(Counter(plop2).values()):
			if x == 5:
				
				row = list(Counter(plop2).keys())[list(Counter(plop2).values()).index(x)]
				banned2.append(row)
				while row in plop2: 
					plop2.remove(row)
	
		for x in list(Counter(plop).values()):
			if x == 6:
				
				column = list(Counter(plop).keys())[list(Counter(plop).values()).index(x)]
				banned.append(column)
				while column in plop: 
					plop.remove(column)
		
		if v in banned or p in banned:
			#print(v)
			con = False
		if con == True:
			#print("hi", v)
			c +=1
			used.append(i)
			starting_nums.append(l[i])
	used.clear()
	c=0
start = True

def lazy(start):
	l = {start: None, }
	for x in range(8):
		l[next(reversed(l.keys()))+9] = None
	return l

def lazy2(start):
	l = []
	for x in range(9):
		l.append(x+start)
	return l

def lazy3(start):
	l = [start]
	for x in range(8):
		l.append(l[-1]+9)
	return l

def square_maker(start):
	d = {}
	for x in range(9):
		d[start] = None
		if x == 2 or x ==5:
			start += 7
		else:
			start += 1
	return d


def violation(row,col,square):
	verf = []
	for x in row.values():
		if x != None:
			verf.append(x)
	for x in Counter(verf).values():
		if x > 1:
			return True
	verf.clear()
		
	for x in col.values():
		if x != None:
			verf.append(x)
	for x in Counter(verf).values():
		if x > 1:
			return True
	verf.clear()
	for x in square.values():
		if x != None:
			verf.append(x)
	for x in Counter(verf).values():
		if x > 1:
			return True
	verf.clear()
	
	return False

# IMAGES


white = pygame.image.load(r"white.png")
one=pygame.image.load(r"1.png")
two=pygame.image.load(r"C:\Users\ioan1\2.png")
three=pygame.image.load(r"C:\Users\ioan1\3.png")
four=pygame.image.load(r"C:\Users\ioan1\4.png")
five=pygame.image.load(r"C:\Users\ioan1\5.png")
six=pygame.image.load(r"C:\Users\ioan1\6.png")
seven=pygame.image.load(r"C:\Users\ioan1\7.png")
eight=pygame.image.load(r"C:\Users\ioan1\8.png")
nine=pygame.image.load(r"C:\Users\ioan1\9.png")

white = pygame.transform.scale(white, (160,83))
white_column = pygame.transform.scale(one, (160,1500))
white_row = pygame.transform.scale(one, (1500,83))
one = pygame.transform.scale(one, (160,83))
two = pygame.transform.scale(two, (160,83))
three = pygame.transform.scale(three, (160,83))
four = pygame.transform.scale(four, (160,83))
five = pygame.transform.scale(five, (160,83))
six = pygame.transform.scale(six, (160,83))
seven = pygame.transform.scale(seven, (160,83))
eight = pygame.transform.scale(eight, (160,83))
nine = pygame.transform.scale(nine, (160,83))

# END OF IMAGES
imgs = [one,two,three,four,five,six,seven,eight,nine]


#indexes for every square 

square1 = [1,2,3,10,11,12,19,20,21]
square2 = [4,5,6,13,14,15,22,23,24]
square3 = [7,8,9,16,17,18,25,26,27]
square4 = [28,29,30,37,38,39,46,47,48]
square5 = [31,32,33,30,41,42,49,50,51]
square6 = [34,35,36,43,44,45,52,53,54]
square7 = [55,56,57,64,65,66,73,74,75]
square8 = [58,59,60,67,68,69,76,77,78]
square9 = [61,62,63,70,71,72,79,80,81]
starting_nums = []

squares = [square1, square2, square3, square4, square5, square6, square7, square8, square9]
squares_dict = [square_maker(1), square_maker(4), square_maker(7), square_maker(28), square_maker(31), square_maker(34), square_maker(55), square_maker(58), square_maker(61)]
#print(squares_dict[5])
# ROWS

row1 = {}
for x in range(9):
	row1[x+1] = None

row2 = {}
for x in range(9):
	row2[x+10] = None

row3 = {}
for x in range(9):
	row3[x+19] = None

row4 = {}
for x in range(9):
	row4[x+28] = None

row5 = {}
for x in range(9):
	row5[x+37] = None

row6 = {}
for x in range(9):
	row6[x+46] = None

row7 = {}
for x in range(9):
	row7[x+55] = None

row8 = {}
for x in range(9):
	row8[x+64] = None

row9 = {}
for x in range(9):
	row9[x+73] = None

rows = [lazy2(1),lazy2(10),lazy2(19),lazy2(28),lazy2(37),lazy2(46),lazy2(55),lazy2(64),lazy2(73)]
rows_dict = [row1,row2,row3,row4,row5,row6,row7,row8,row9]
#print(rows[8])
# COLUMNS
#print(rows_dict[0])

column1 = lazy(1)
column2 = lazy(2)
column3 = lazy(3)
column4 = lazy(4)
column5 = lazy(5)
column6 = lazy(6)
column7 = lazy(7)
column8 = lazy(8)
column9 = lazy(9)

columns = [lazy3(1),lazy3(2),lazy3(3),lazy3(4),lazy3(5),lazy3(6),lazy3(7),lazy3(8),lazy3(9)]
columns_dict = [column1,column2,column3,column4,column5,column6,column7, column8,column9]
#print(columns[8])
#print(column1)


for x in range(9):
	clop += 1
	if float(x//2) == float(x/2):
		alt = True
	else:
	 	alt = False
	sample(squares[x])
starting_nums_COPY = [x for x in starting_nums]
#print(starting_nums_COPY)


used = []
counts = -1
done = False
#function for the sprites of the game which are just each individual square
class Sprite(pygame.sprite.Sprite):
	def __init__(self, color, height, width):
		pygame.sprite.Sprite.__init__(self)
		self.past = None
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		
		self.rect = self.image.get_rect()
	def update(self):
		global counts, done, ctn, ex, used, num
		#print(starting_nums_COPY)
		if start == True:
			while True:
				lol = random.randrange(0,8)
				

				
		# 3, 2, 1, 3, 2, 2, 1, 2, 1
				

				
				used_total.append(lol)
				if counts == ex:
					print(used)
					
					used.clear()
				
				if lol in used:
					
					
					good = False
					used_total.pop()
					continue
				else:
					good = True

					# (list(Counter(list(d.values())).values()))
				
				#for y in (list(Counter(list(rows_dict[x].values())).values())):
				
				for x in range(len(rows)):
					if starting_nums[i] in rows[x]:
						if lol+1 in list(rows_dict[x].values()):
							#print(x, "hi")
							#print(rows_dict[x])
							#print(lol)
							good = False
							used_total.pop()
							ctn = True
							break
						#rows_dict[x][starting_nums[i]-1] = lol
						good = True
						ctn = False
						break
				if ctn == False:		
					for x in range(len(columns)):			
						if starting_nums[i] in columns[x]:
							if lol+1 in list(columns_dict[x].values()):
								good = False
								used_total.pop()
								ctn = False
								break
							#columns_dict[x][starting_nums[i]-1] = lol
							good = True
							break
				for x in list(Counter(used_total).values()):
					if x >= 5:
						good = False
						used_total.pop()
						break

				if good == True:
					color = (0,0,255)
					self.image = changColor(imgs[lol], color)
					for x in range(len(rows)):
						if starting_nums_COPY[0] in rows[x]:
							rows_dict[x][starting_nums_COPY[0]] = lol+1
							break

					for x in range(len(columns)):
						if starting_nums_COPY[0] in columns[x]:
							columns_dict[x][starting_nums_COPY[0]] = lol+1
							break
					for x in range(len(squares_dict)):
						if starting_nums_COPY[0] in squares[x]:
							squares_dict[x][starting_nums_COPY[0]] = lol + 1

					starting_nums_COPY.pop(0)
					used.append(lol)
					ctn = False
					
					

					return
				
				
		color = (0,0,0)
		num = event.key
		
		balls = coords[(paps1,paps)]	
		num = nums
		
		
		if num == 32:
			self.image = white
			columns_dict[paps1][balls] = None
			rows_dict[paps][balls] = None
		if num == 49:
			self.image = one
			columns_dict[paps1][balls] = 1
			rows_dict[paps][balls] = 1
		if num == 50:
			self.image = two
			columns_dict[paps1][balls] = 2
			rows_dict[paps][balls] = 2
			
		if num == 51:
			self.image = three
			columns_dict[paps1][balls] = 3
			rows_dict[paps][balls] = 3
		if num == 52:
			self.image = four
			columns_dict[paps1][balls] = 4
			rows_dict[paps][balls] = 4
		if num == 53:
			self.image = five
			columns_dict[paps1][balls] = 5
			rows_dict[paps][balls] = 5
		if num == 54:
			self.image = six
			columns_dict[paps1][balls] = 6
			rows_dict[paps][balls] = 6
		if num == 55:
			self.image = seven
			columns_dict[paps1][balls] = 7
			rows_dict[paps][balls] = 7
		if num == 56:
			self.image = eight	
			columns_dict[paps1][balls] = 8
			rows_dict[paps][balls] = 8
		if num == 57:
			self.image = nine
			columns_dict[paps1][balls] = 9
			rows_dict[paps][balls] = 9
		


pygame.init()
rectx = 3.5
columns_sprite = pygame.sprite.Group()
for x in range(9):
	recty = 3.5
	sprite = Sprite((255,255,255), 800, 160)
	sprite.rect.x = rectx
	sprite.rect.y = recty
	#pygame.draw.rect(win, (255,255,0), (rectx, recty, 1500, 85))
	columns_sprite.add(sprite)
	rectx += 160

rows_sprite = pygame.sprite.Group()	
recty = 3.5
for x in range(9):
	
	rectx = 3.5
	sprite = Sprite((255,255,255), 88, 1500)
	sprite.rect.x = rectx
	sprite.rect.y = recty
	rows_sprite.add(sprite)
	recty+=88
	




clicked_sprites = pygame.sprite.Group()
sizex = 166.66 #size of a square 
sizey = 88.89
all_sprites_list = pygame.sprite.Group() #sprite group
column = 0
rectx = 3.5
recty = 3.5


win = pygame.display.set_mode((1500, 800)) #windows of game
pygame.display.set_caption("Sudoku") #name of game
run = True
bold = 0

for x in range(81):	#making a sprite for each individual square
	if column == 9:
		rectx = 3.5
		recty += sizey
		column = 0

	sprite = Sprite((255,255,255), 83.89, 160) #sprite for squares
	sprite.rect.x = rectx
	sprite.rect.y = recty
	rectx += sizex
	column += 1
	all_sprites_list.add(sprite)

#we need to add 3 random numbers to each square START:
counts2 = 0
print(starting_nums)
starting = pygame.sprite.Group()
for x in range(len(starting_nums)):
	starting.add(all_sprites_list.sprites()[starting_nums[x]-1])
	i = x
	counts += 1
	starting.update()
	if counts == pected[counts2]:
		if counts2 != 8:
			counts2+= 1
		counts = 0
		print(counts2)
		
		ex = pected[counts2]
	starting = pygame.sprite.Group()
	track.append(starting_nums[x])

start = False

#Function UPDATE will control the randomization of numbers (as well as other things), just inserting the starting squares into a sprite group
#END 



while run:
	for column in columns_dict:
		for x in Counter(column.values()).values():
			if x != 1:
				check = False
				break
		if check == False:
			columns_confirm = False
			break
		columns_confirm = True
	check = True
	
	for row in rows_dict:
		for x in Counter(row.values()).values():
			if x != 1:
				check = False
				break
		if check == False:
			row_confirm = False
			break
		row_confirm = True	
	check = True	
	if row_confirm == True and columns_confirm == True:
		print("CONGRATS")
		exit()

	for event in pygame.event.get(): #exit loop
		if event.type == pygame.QUIT:
			run = False

	
		
	
	
	xcord = 166.66
	pos = False
	

	pygame.draw.rect(win, (255,255,255), (0,0, 1500, 1500)) #white background
	pygame.draw.rect(win, (0,0,0), (0,0, 1500, 1500), width = 3) #black border
	pygame.draw.line(win, (0,0,0), (0,266.66), (1500, 266.66), width = 3 ) #seperate it in to thirds
	pygame.draw.line(win, (0,0,0), (0,266.66), (1500, 266.66), width = 3 )

	for x in range(9):
		bold += 1 
		if bold == 3:
			pygame.draw.line(win, (0,0,0), (xcord, 0), (xcord, 1500), width= 3) #cut it in ninths vertically
			bold = 0
		pygame.draw.line(win, (0,0,0), (xcord, 0), (xcord, 1500), width= 1 )
		xcord += 166.66
	bold = 0
	xcord = 88.89
	for x in range(9):	
		bold +=1													#cut it in ninths horizontally
		if bold == 3:
			pygame.draw.line(win, (0,0,0), (0, xcord), (1500, xcord), width= 3)
			bold = 0
		pygame.draw.line(win, (0,0,0), (0, xcord), (1500, xcord), width= 1 )
		xcord += 88.89

	#pygame.display.update()
	
	all_sprites_list.draw(win)
	pygame.display.flip()
	ev = pygame.event.get()
	
	for event in ev:



		if event.type == pygame.MOUSEBUTTONUP: 	#detect if square was clicked
			pos = pygame.mouse.get_pos()	
			
			for s in all_sprites_list:
				if s.rect.collidepoint(pos):
					clicked_sprites.add(s)
					events = pygame.event.get()
					
			for s in range(9):
				if rows_sprite.sprites()[s].rect.collidepoint(pos):
					paps = s
					#print(f"row {s}")
					break
			for s in range(9):
				if columns_sprite.sprites()[s].rect.collidepoint(pos):
					#print(f"column {s}")
					paps1 = s
					break
			#print(paps1,paps)

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE or event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9:
				clicked_sprites.update()
				clicked_sprites = pygame.sprite.Group()
				#print(event.key)
			if event.key == pygame.K_p:
				while True:
					
					
					ini = 1
					if inc not in starting_nums:
						
						while True:
							if ini == 10:
								returned = True
								columns_dict[c][inc] = None
								rows_dict[r][inc] = None
								squares_dict[s][inc] = None
								print(prev)
								#if len(prev) != 0:
								try:
									inc = prev[-1]
									prev.pop()
								except:
									columns_dict[c][inc] = weird[weird_count]
									rows_dict[r][inc] = weird[weird_count]
									squares_dict[s][inc] = weird[weird_count]
									weird_count += 1
									
								break
							
							for y in range(len(columns_dict)):
								if inc in columns[y]:
									if returned == True:
										if columns_dict[y][inc] == 9:
											print('jeez')
											columns_dict[c][inc] = None
											rows_dict[r][inc] = None
											squares_dict[s][inc] = None
											try:
												inc = prev[-1]
												prev.pop()
											except:
												columns_dict[c][inc] = weird[weird_count]
												rows_dict[r][inc] = weird[weird_count]
												squares_dict[s][inc] = weird[weird_count]
												weird_count += 1
											leave = True
											returned = True
											break
										ini = columns_dict[y][inc] + 1 
										returned = False
									columns_dict[y][inc] = ini
									c = y
							if leave == True:
								leave = False
								break
							for y in range(len(rows_dict)):

								if inc in rows[y]:
									rows_dict[y][inc] = ini
									r=y
							for y in range(len(rows_dict)):
								if inc in squares[y]:
									squares_dict[y][inc] = ini
									s=y

							
								
							if violation(rows_dict[r], columns_dict[c], squares_dict[s]) == False and ini != 10:
								print(ini)
								dp[inc] = ini
								break
							elif ini != 10:
								print('cum', ini)
								ini += 1

					if returned == True:
						print('hey', ini)
					if returned != True and inc not in starting_nums:
						
						prev.append(inc)
					if returned != True:
						inc += 1	#problem is here when returned is True
					ini = 1
					if inc == 82:
						print("nice")
						print(rows_dict[8])
						sprites_needed = pygame.sprite.Group()
						print(dp)
						paps1, paps = 1,1
						for x in range(81):
							if (x+1) not in starting_nums and x != 81:
								sprites_needed.add(all_sprites_list.sprites()[x])
								print(sprites_needed)
								if dp[x+1] == 1:
									nums = 49

									sprites_needed.update()
									sprites_needed = pygame.sprite.Group()
									continue
								if dp[x+1] == 2:
									nums = 50
									sprites_needed.update()
									sprites_needed = pygame.sprite.Group()
									deez = "goofy"
									print('sasasdas')
									continue
									
								if dp[x+1] == 3:
									nums = 51
									sprites_needed.update()
									sprites_needed = pygame.sprite.Group()
									continue
								if dp[x+1] == 4:
									nums = 52
									sprites_needed.update()
									sprites_needed = pygame.sprite.Group()
									continue
								if dp[x+1] == 5:
									nums = 53
									sprites_needed.update()
									sprites_needed = pygame.sprite.Group()
									continue
								if dp[x+1] == 6:
									nums = 54
									sprites_needed.update()
									sprites_needed = pygame.sprite.Group()
									continue
								if dp[x+1] == 7:
									nums = 55
									sprites_needed.update()
									sprites_needed = pygame.sprite.Group()
									continue
								if dp[x+1] == 8:
									nums = 56
									sprites_needed.update()
									sprites_needed = pygame.sprite.Group()
									continue
								if dp[x+1] == 9:
									nums = 57
									sprites_needed.update()
									sprites_needed = pygame.sprite.Group()
									continue
								
								
								print(x+1)
								
								
								
							sprites_needed = pygame.sprite.Group()

						break
		

pygame.quit()
