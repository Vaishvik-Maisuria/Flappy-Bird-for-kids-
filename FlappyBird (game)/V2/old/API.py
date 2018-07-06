

''' VARIABLES '''

'''This is a string variable'''
## this variable contains the name of the game which shoes up on the title bar. 
name_of_game = 'Flappy Bird'

'''This is a Integer Varible'''
## This variable controls speed of the game - you can  change its value to make the game go faster or slower
game_speed = 30     

'''This is a Boolean Variable (229) - Idk how to replace this variable needd to ask...'''
## This is a variable that stores if the player flaps
player_flap = False

'''This is a variable that stores a tuple of 3 Strings'''
## This is variable stores a pathway to images that represent the three possible position of the bird flap'
red_bird =  ('assets/sprites/redbird-upflap.png','assets/sprites/redbird-midflap.png','assets/sprites/redbird-downflap.png',)


'''functions'''


def when_esc_clicked(self):
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
        	pygame.quit()
        	sys.exit()


def when_space_up_clicked(self):
	for event in pygame.event.get():
		if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
        	if playery > -2 * IMAGES['player'][0].get_height():
            	playerVelY = playerFlapAcc
            	playerFlapped = True
            	return playerFlapped
    return False

def play_wing_sound(self):
		
	pygame.init()

    self.sounds = {}
    self.sounds['wing'] = pygame.mixer.Sound('assets/audio/wing.wav')
		
	SOUNDS['wing'].play()

def play_die_sound(self):

	pygame.init()

    self.sounds = {}
    self.sounds['die'] = pygame.mixer.Sound('assets/audio/die.wav')
  	
	SOUNDS['die'].play()

def play_hit_sound(self):
	pygame.init()

    self.sounds = {}
    self.sounds['hit'] = pygame.mixer.Sound('assets/audio/hit.wav')
		
	SOUNDS['hit'].play()


def play_point_sound(self):

	pygame.init()

    self.sounds = {}
     self.sounds['point'] = pygame.mixer.Sound('assets/audio/point.wav')
		
	SOUNDS['point'].play()


def play_swoosh_sound(self):

	pygame.init()

    self.sounds = {}
   	self.sounds['swoosh'] = pygame.mixer.Sound('assets/audio/swoosh.wav')
	SOUNDS['swoosh'].play()


def checkCrash(player, upperPipes, lowerPipes):
    """returns True if player collders with base or pipes."""
    pi = player['index']
    player['w'] = IMAGES['player'][0].get_width()
    player['h'] = IMAGES['player'][0].get_height()

    # if player crashes into ground
    if player['y'] + player['h'] >= BASEY - 1:
        return [True, True]
    else:

        playerRect = pygame.Rect(player['x'], player['y'],
                      player['w'], player['h'])
        pipeW = IMAGES['pipe'][0].get_width()
        pipeH = IMAGES['pipe'][0].get_height()

        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            # upper and lower pipe rects
            uPipeRect = pygame.Rect(uPipe['x'], uPipe['y'], pipeW, pipeH)
            lPipeRect = pygame.Rect(lPipe['x'], lPipe['y'], pipeW, pipeH)

            # player and upper/lower pipe hitmasks
            pHitMask = HITMASKS['player'][pi]
            uHitmask = HITMASKS['pipe'][0]
            lHitmask = HITMASKS['pipe'][1]

            # if bird collided with upipe or lpipe
            uCollide = pixelCollision(playerRect, uPipeRect, pHitMask, uHitmask)
            lCollide = pixelCollision(playerRect, lPipeRect, pHitMask, lHitmask)

            if uCollide or lCollide:
                return [True, False]

    return [False, False]


def when_hit_the ground(self, playerx, playery, playerIndex  ):


'''IF STATEMENTS'''





'''WHILE LOOPS'''






'''BASIC FUNCTIONS '''



'''BASIC I/O'''
