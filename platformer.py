""" platformer """

import pygame, simpleGE

class Charlie(simpleGE.SuperSprite):
    def __init__(self, scene, position):
        super().__init__(scene)
        self.setImage("Charlie.png")
        self.setSize(50, 50)
        self.setPosition(position)
        self.inAir = True
        
            
    def checkEvents(self):
        check = False;
        if self.scene.isKeyPressed(pygame.K_p):
            check = True;
        if check == False:
            if self.inAir:
                self.addForce(.2, 270)
            
            if self.y > 450:
                self.inAir = False
                self.y = 450
                self.setDY(0)
            
            if self.x < 0:
                self.x = 0
            
            if self.scene.isKeyPressed(pygame.K_RIGHT):
                self.x += 5
            if self.scene.isKeyPressed(pygame.K_LEFT):
                self.x -= 5
                
            if self.scene.isKeyPressed(pygame.K_UP):
                if not self.inAir:
                    #self.y -= 10
                    self.addForce(4, 90)
                    self.inAir = True
                
        platform = self.collidesGroup(self.scene.platformGroup)
        if platform:
            if self.dy > 0:
                overlap = platform.rect.top - self.rect.bottom
                self.changeYby(overlap + 1)
                self.setDY(0)
                self.inAir = False
        else:
            self.inAir = True
            
        wall = self.collidesGroup(self.scene.wallGroup)
        if wall:
            if self.y +25 > wall.rect.top:
                self.inAir = False
                self.y = wall.rect.top -25
                self.setDY(0)
        
        
                

class Platform(simpleGE.SuperSprite):
    def __init__(self, scene, position):
        super().__init__(scene)
        self.setPosition(position)
        self.imageMaster = pygame.Surface((50, 50))
        self.imageMaster.fill(pygame.Color("blue"))
        
    def update(self):
        super().update()
        if self.mouseDown():
            self.setPosition(pygame.mouse.get_pos())
            
class Wall(simpleGE.SuperSprite):
    def __init__(self, scene, position, size):
        super().__init__(scene)
        self.setPosition(position)
        self.imageMaster = pygame.Surface(size)
        self.imageMaster.fill(pygame.Color("green"))

class Win(simpleGE.SuperSprite):
    def __init__(self, scene, position, size):
        super().__init__(scene)
        self.setPosition(position)
        self.imageMaster = pygame.Surface(size)
        self.imageMaster.fill(pygame.Color("yellow"))
        
        
class Intro(simpleGE.Scene):
    def __init__(self):
        simpleGE.Scene.__init__(self)
        instructions = simpleGE.MultiLabel()
        instructions.textLines = [
            "you are trapped in a dungeon",
            "the only way out is to solve",
            "the puzzles before you."]
        
        instructions.size = (400,300)
        instructions.fgColor = (0xFF, 0xFF, 0xFF)
        instructions.bgColor = (0, 0, 0)
        instructions.center = (320,200)
        
        self.button = simpleGE.Button()
        self.button.center = (320,400)
        self.button.text = "Play"
        
        self.setCaption("title of game")
        
        self.sprites = [instructions, self.button]
    def update(self):
        select = Select()
        if self.button.clicked:
            self.stop()
            select.start()
        
        
class Select(simpleGE.Scene):
    def __init__(self):
        simpleGE.Scene.__init__(self)
        self.button1 = simpleGE.Button()
        self.button1.center = (320,100)
        self.button1.text = "Level 1"
        
        self.button2 = simpleGE.Button()
        self.button2.center = (320, 200)
        self.button2.text = "Level 2"
        
        self.button3 = simpleGE.Button()
        self.button3.center = (320, 300)
        self.button3.text = "Level 3"
        
        self.sprites = [self.button1, self.button2, self.button3]
    def update(self):
        level1 = Level1()
        level2 = Level2()
        if self.button1.clicked:
            self.stop()
            level1.start()
        if self.button2.clicked:
            self.stop()
            level2.start()
        if self.button3.clicked:
            self.stop()
            level1.start()
            


class Level1(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setCaption("arrows to move and jump. drag platforms around")

        self.charlie = Charlie(self, (20,350))

        platforms = [Platform(self, (200, 275)), Platform(self, (300, 275)), 
                     ]
        walls = [Wall(self, (0,400), (200, 300)), Wall(self, (600,400), (100,300))]
        
        win = Win(self, (600,225), (50,50))
        
        self.platformGroup = self.makeSpriteGroup(platforms)
        self.addGroup(self.platformGroup)
        
        self.wallGroup = self.makeSpriteGroup(walls)
        self.addGroup(self.wallGroup)
        
        self.sprites = [self.charlie, win]
        
        select = Select()
        if self.charlie.x > win.rect.left:
            self.stop()
            select.Start()

class Level2(simpleGE.Scene):
    def __init(self):
        super().__init__()
        self.setCaption("arrows to move and jump. drag platforms around")

        self.charlie = Charlie(self, (20,350))

        platforms = [Platform(self, (200, 275)), Platform(self, (300, 275)), 
                     ]
        walls = [Wall(self, (0,400), (200, 300)), Wall(self, (600,400), (100,300))]
        
        win = Win(self, (600,225), (50,50))
        
        self.platformGroup = self.makeSpriteGroup(platforms)
        self.addGroup(self.platformGroup)
        
        self.wallGroup = self.makeSpriteGroup(walls)
        self.addGroup(self.wallGroup)
        
        self.sprites = [self.charlie, win]
        
        select = Select()
        if self.charlie.x > win.rect.left:
            self.stop()
            select.Start()

def main():
    intro = Intro()
    
    intro.start()
    
    
    
if __name__ == "__main__":
    main()
    