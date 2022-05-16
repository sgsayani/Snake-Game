
import pygame
from pygame.locals import *
import time
import random

BACKGROUND_COLOR = (30, 117, 54)
class food:
    def __init__(self,parent_screen):
       self.parent_screen = parent_screen
       self.image=pygame.image.load("food.jpg").convert()
       self.x = 80
       self.y = 80
    def draw(self):
        self.parent_screen.blit(self.image, (self.x,self.y))
        pygame.display.flip()
    def move(self):
        self.x=random.randint(1,24)*20
        self.y= random.randint(1,24)*20    

class snake:
    def __init__(self,parent_screen):
        self.parent_screen = parent_screen
        self.blc=pygame.image.load("snake.jpg").convert()
        self.length = 1
        self.x=[50]
        self.y=[50]
        self.direction ='down'
        
    def move_up(self):
        self.direction = 'up'
    def move_down(self):
        self.direction = 'down'
    def move_left(self):
        self.direction = 'left'
    def move_right(self):
        self.direction = 'right'
    
     
    def walk(self):
     for i in range(self.length-1,0,-1):
         self.x[i] = self.x[i-1]
         self.y[i] = self.y[i-1]
     if self.direction=='left':
         self.x[0] -=20
     elif self.direction=='right':
         self.x[0] +=20
     elif self.direction=='up':
         self.y[0] -=20
     elif self.direction=='down':
         self.y[0] +=20
     self.draw()       
    
    def draw(self):
        self.parent_screen.fill((BACKGROUND_COLOR))
        for i in range(self.length):
            self.parent_screen.blit(self.blc, (self.x[i],self.y[i]))
        pygame.display.flip() 
    
    def increase_length(self):
        self.length +=1
        self.x.append(-1)
        self.y.append(-1)
        
        
class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.surface=pygame.display.set_mode((550,550)) #winsow size
        self.snake = snake(self.surface)
        self.snake.draw()
        self.food=food(self.surface)
        self.food.draw()
    def reset(self):
        self.snake = snake(self.surface)
        self.food=food(self.surface)  
          
    def is_collision(self,x1,y1,x2,y2):
        if x1>=x2 and x1<x2 + 20:
            if y1>=y2 and y1<y2 +20:
                return True
        return False
    
    
    
    def play(self):
        self.snake.walk()
        self.food.draw()
        self.score()
        pygame.display.flip()
        
        for i in range(self.snake.length):
            if self.is_collision(self.snake.x[i], self.snake.y[i], self.food.x, self.food.y):
                self.snake.increase_length()
                self.food.move()
            
            
        for i in range(3,self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
              raise  "collition" 
        # snake colliding with the boundries of the window
        if not (0 <= self.snake.x[0] <= 550 and 0 <= self.snake.y[0] <= 550):
            
            raise "Hit the boundry error"
               
    
    def score(self):
        font = pygame.font.SysFont('italic', 30)
        score= font.render(f"Score : {self.snake.length}", True,(250,250,250) )
        self.surface.blit(score,(450,10))
        
    def show_game_over(self):
        self.surface.fill(BACKGROUND_COLOR)  
        font = pygame.font.SysFont('italic', 30)
        line1 = font.render(f"Game is over !!!!!  Score : {self.snake.length}", True,(250,250,250) )
        self.surface.blit(line1,(200,300)) 
        line2 = font.render("Play Again ", True,(250,250,250) )  
        self.surface.blit(line2, (200,350)) 
        pygame.display.flip()
        
        
  
    
    
    def run(self):
       
       running = True
       pause = False
       
       while running:
            for event in pygame.event.get():
               if event.type == KEYDOWN:
                   if event.key == K_ESCAPE:
                       running =False
                   if event.key == K_RETURN:
                        pause = False
                   if not pause:
                        if event.key==K_UP:
                            self.snake.move_up()
                        if event.key ==K_DOWN:
                            self.snake.move_down()
                        if event.key ==K_LEFT:
                            self.snake.move_left()
                        if event.key ==K_RIGHT:
                            self.snake.move_right()
                           
               elif event.type ==QUIT:
                    running = False
            try:
               if not pause:
                   self.play()
            except Exception as e:
               self.show_game_over()
               pause = True
               self.reset()
               
            time.sleep(.1)
if __name__=="__main__":
    game=Game()
    game.run()

    
    
   
    
    
    
    
    
    