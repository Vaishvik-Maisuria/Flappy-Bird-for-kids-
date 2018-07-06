'''This is a Integer Varible'''
## This variable controls speed of the game - you can  change its value to make the game go faster or slower
game_speed = 30


'''This is a variable that stores a tuple of 3 Strings'''
## This is variable stores a pathway to images that represent the three possible position of the bird flap'
red_bird =  ('assets/sprites/redbird-upflap.png','assets/sprites/redbird-midflap.png','assets/sprites/redbird-downflap.png',)



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

def pixelCollision(rect1, rect2, hitmask1, hitmask2):
    """Checks if two objects collide and not just their rects"""
    rect = rect1.clip(rect2)
    
    if rect.width == 0 or rect.height == 0:
        return False

    x1, y1 = rect.x - rect1.x, rect.y - rect1.y
    x2, y2 = rect.x - rect2.x, rect.y - rect2.y

for x in xrange(rect.width):
    for y in xrange(rect.height):
        if hitmask1[x1+x][y1+y] and hitmask2[x2+x][y2+y]:
            return True
    return False

def getHitmask(image):
    """returns a hitmask using an image's alpha."""
    mask = []
    for x in xrange(image.get_width()):
        mask.append([])
        for y in xrange(image.get_height()):
            mask[x].append(bool(image.get_at((x,y))[3]))
    return mask

