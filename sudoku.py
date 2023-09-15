import pygame
import random
from collections import Counter 
starting_nums = [] # position of the numbers that are given
track = [] # list to prevent starting nums from being in a square
ctn = False # checks to see if we need to continue to check if we repeat a number in columns after rows was checked
used = [] # used numbers for a square, resets
colNum = None # used to detect which col 
rowNum = None # used to detect whcih row
good = True # confirms that we can put the chosen number between 1-9 in its position
check = True # verifies final condition of the game


c = 0
plop = [] # helps with choosing starting nums
used_total = [] # every position used
banned = [] # prevents numbers used twice in a row
banned2 = [] # prevents numbers used twice in a col
plop2 = [] # helps with choosing starting nums
clop = 0 # square number for starting nums
coords = {} # coordinate in the form of (col, row) for every position and its value associated
y = 0 #starting coords
x = 0
val = 1 # variable used to make coords
ini = 1 # number the sudoku solver is inserting
inc = 1 # position the sudoku solver is at
prev = [] # previous squares the sudoku solver can go to (backtracking)
leave = None # special case for backtracking, helps us avoid error
weird = [1,2,3,4,5,6,7,8,9] # if no options are left for backtracking
weird_count = 0 # how many times it's happened
dp = {} # value for every position (easier to navigate than coords)

pected = [3, 2, 1, 2, 3, 2, 1, 2, 1] # how many given numbers for each square
ex = pected[0] # initialising the amount of given positions for a square
returned = None # if we are backtracking, this will change to True

for _ in range(81): # makes coords

	coords[(x,y)] = val
	val += 1
	x += 1
	if x == 9:
		x-=9
		y+=1    # (0,1) = 9
		






def changColor(image, color): # changes color for given squares
    colouredImage = pygame.Surface(image.get_size())
    colouredImage.fill(color)
    
    finalImage = image.copy()
    finalImage.blit(colouredImage, (0, 0), special_flags = pygame.BLEND_MULT)
    return finalImage

def sample(l): # gives us the position for given nums
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
			
			con = False
		if con == True:
		
			c +=1
			used.append(i)
			starting_nums.append(l[i])
	used.clear()
	c=0
start = True

def lazy(start): # function that makes dictionary with the position for every column. We make one for column 0, 1, 2, etc.
	l = {start: None, }
	for x in range(8):
		l[next(reversed(l.keys()))+9] = None
	return l

def lazy2(start): # function that makes a list for all rows
	l = []
	for x in range(9):
		l.append(x+start)
	return l

def lazy3(start): # function that makes a list for all columns
	l = [start]
	for x in range(8):
		l.append(l[-1]+9)
	return l

def square_maker(start): # function that makes list for every position in a square
	d = {}
	for x in range(9):
		d[start] = None
		if x == 2 or x ==5:
			start += 7
		else:
			start += 1
	return d


def violation(row,col,square): # checks if there is a violation after we place a number in a col, row and square. returns True if there is
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

squares = [square1, square2, square3, square4, square5, square6, square7, square8, square9] # List with position of every square
squares_dict = [square_maker(1), square_maker(4), square_maker(7), square_maker(28), square_maker(31), square_maker(34), square_maker(55), square_maker(58), square_maker(61)] # position of squares with values
#coul've used the keys from the squares_dict, but it was an oversight


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

# COLUMNS


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


# MAKING STARTING NUMS

for x in range(9):
	clop += 1
	
	sample(squares[x])
starting_nums_COPY = [x for x in starting_nums]

# END


used = []
counts = -1
done = False
#function for the sprites of the game which are just each individual position
class Sprite(pygame.sprite.Sprite):
	def __init__(self, color, height, width):
		pygame.sprite.Sprite.__init__(self)
		self.past = None
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		
		self.rect = self.image.get_rect()
	def update(self):
		global counts, done, ctn, ex, used, num
		
		if start == True: # starting function, just setting up the starting nums and choosing an appropriate value to insert
			while True:
				lol = random.randrange(0,8)
				

				
		# 3, 2, 1, 3, 2, 2, 1, 2, 1
				

				
				used_total.append(lol)
				if counts == ex:
					
					
					used.clear()
				
				if lol in used:
					
					
					good = False
					used_total.pop()
					continue
				else:
					good = True

					
				
				for x in range(len(rows)):
					if starting_nums[i] in rows[x]:
						if lol+1 in list(rows_dict[x].values()):
							
							good = False
							used_total.pop()
							ctn = True
							break
						
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
		
		
		if num == 32: # codes for every click to change the value of the position
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
		

# Setting up the screen (not monitor screen sensitive)
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
	
		
		ex = pected[counts2]
	starting = pygame.sprite.Group()
	track.append(starting_nums[x])

start = False

#Function UPDATE will control the randomization of numbers (as well as other things), just inserting the starting squares into a sprite group
#END 



while run:
	#CHECKING IF GAME IS COMPLETED
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
		
		exit()
	# END


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
					
					break
			for s in range(9):
				if columns_sprite.sprites()[s].rect.collidepoint(pos):
					
					paps1 = s
					break
			


		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE or event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9:
				clicked_sprites.update()
				clicked_sprites = pygame.sprite.Group()

		# If p is pressed, then the sudoku solver starts		
			if event.key == pygame.K_p:
				while True:
					
					
					ini = 1
					if inc not in starting_nums: # making sure we don't modify a starting position
						
						while True:
							if ini == 10: # ini is = 10 only if we ran out of options, then we backtrack
								returned = True
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
									
								break
							# tries a number in every position
							for y in range(len(columns_dict)):
								if inc in columns[y]:
									if returned == True:
										if columns_dict[y][inc] == 9:
											
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

							
								
							if violation(rows_dict[r], columns_dict[c], squares_dict[s]) == False and ini != 10: # if placing the number is ok, this runs
								
								dp[inc] = ini
								break
							elif ini != 10: # otherwise, we try a larger number
								
								ini += 1

					if returned == True:
						
					if returned != True and inc not in starting_nums: # keeping track of each previous position
						
						prev.append(inc)
					if returned != True: # incrementing the position by 1 every time
						inc += 1	
					ini = 1
					if inc == 82: # when inc is 82, it's over, the rest of the code displays the solved sudoku
						
						
						sprites_needed = pygame.sprite.Group()
						
						paps1, paps = 1,1
						for x in range(81):
							if (x+1) not in starting_nums and x != 81:
								sprites_needed.add(all_sprites_list.sprites()[x])
								
								if dp[x+1] == 1:
									nums = 49

									sprites_needed.update()
									sprites_needed = pygame.sprite.Group()
									continue
								if dp[x+1] == 2:
									nums = 50
									sprites_needed.update()
									sprites_needed = pygame.sprite.Group()
									
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
								
								
								
								
								
								
							sprites_needed = pygame.sprite.Group()

						break
		

pygame.quit()
