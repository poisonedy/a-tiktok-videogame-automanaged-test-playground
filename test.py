# Pygame template - skeleton for a new pygame project
from jinja2 import pass_context
import pygame
import random
import os
import time
import logging
import threading
import time
import GIFImage
import subprocess
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent, GiftEvent
import musicpd


WIDTH = 720
HEIGHT = 1280
FPS = 25

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')


class Player(pygame.sprite.Sprite, pygame.font.Font):
    def __init__(self):

        self.cli = musicpd.MPDClient()
        self.cli.connect()
        self.cli.next()
        

        self.client: TikTokLiveClient = TikTokLiveClient(unique_id="@lalocadelconobcn")
        
        @self.client.on("connect")
        async def on_connect(_: ConnectEvent):
            print("Connected to Room ID:", self.client.room_id)
        
        @self.client.on("comment")
        async def on_connect(event: CommentEvent):
            print(f"{event.user.nickname} -> {event.comment}")
            for item in self.playersPendingDict:
                if item['player'] == event.user.nickname:
                    if item['gift'] != "":
                        if item["phrase"] == "":
                            item["phrase"] = event.comment
                            break

        @self.client.on("gift")
        async def on_gift(event: GiftEvent):
        # If it's type 1 and the streak is over
            if event.gift.gift_type == 1:
                if event.gift.repeat_end == 1:
                    print(f"{event.user.uniqueId} sent {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\"")
                    self.playersPendingDict.append({'player':event.user.nickname, 'gift': event.gift.repeat_count, 'phrase': ""})
                        

    # It's not type 1, which means it can't have a streak & is automatically over
            elif event.gift.gift_type != 1:
                print(f"{event.user.uniqueId} sent \"{event.gift.extended_gift.name}\"")
                self.playersPendingDict.append({'player':event.user.nickname, 'gift': event.gift.repeat_count, 'phrase': ""})


        
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.facebase = face
        self.mouthbase = basemouth
        self.mouthbase.set_colorkey(TRANSPARENT)
        self.midmouth = midmouth
        self.midmouth.set_colorkey(TRANSPARENT)
        self.openmouth = openmouth
        self.openmouth.set_colorkey(TRANSPARENT)
        self.nextsong = nextsong
        self.previousong = previousong
        self.previousong.set_colorkey(TRANSPARENT)
        self.facebase_closed = faceclosed
        self.nextsong.set_colorkey(TRANSPARENT)
        self.facebase.set_colorkey(TRANSPARENT)
        self.facebase.set_alpha(255)
        self.facebase_closed.set_colorkey(TRANSPARENT)
        self.facebase_closed.set_alpha(255)

        self.image.set_colorkey(TRANSPARENT)
        self.onerose = onerose
        self.onerose.set_colorkey(TRANSPARENT)
        self.border = border
        self.border.set_colorkey(TRANSPARENT)
        self.momentumy  = "UP"
        self.momentumx_activity = "DISABLED"
        self.momentumx = "LEFT"
        self.chars = 0
        self.playersPendingDict = []
        self.shake_sound = shake_sound
        #self.runTikTokClient()
        self.autoPilot = True
        self.makeFaceStatus = True
        self.isTalking = False
        self.makeFacesNow()
        
        
        self.makeMouthNow()


        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT  / 2)

        self.rectonerose = self.onerose.get_rect()
        self.rectonerose.center = (900, 270)
        self.facerect = self.facebase.get_rect()
        self.facerect.center = (505, 650)
        self.mouthbaserect = self.mouthbase.get_rect()
        self.mouthbaserect.center = (505, 630)
        self.facerect.center = (505, 650)
        self.previoussongrect = self.previousong.get_rect()
        self.previoussongrect.center = (105, 700)
        self.nextsongongrect = self.nextsong.get_rect()
        self.nextsongongrect.center = (630, 700)
        self.isTalking = False

        self.font_nameplayer = pygame.font.SysFont('Just My Type', 63)
        self.font_nameplayer_surface = self.font_nameplayer.render('', True, WHITE)
        self.text_nameplayerrect_obj = self.font_nameplayer_surface.get_rect()
        self.text_nameplayerrect_obj.center = (355, 880)


        self.font_obj = pygame.font.SysFont('alarm clock', 38)
        self.text_surface_obj = self.font_obj.render('', True, GREEN)
        self.text_rect_obj = self.text_surface_obj.get_rect()
        self.text_rect_obj.center = (WIDTH/2, HEIGHT/2)
         #pygame.font.Font.__init__(self)
        #self.popRose()
        #self.retrievePhrases()

    def demo(self):
        x = threading.Thread(target=self._demo2)
        x.start()

    def _setchars(self,phrase):
        self.chars = len(phrase)
        if self.chars == 2:
            self.chars = self.chars - 4
        elif self.chars == 3:
            self.chars = self.chars - 4
        elif self.chars == 4:
            self.chars = self.chars - 4
        elif self.chars == 5:
            self.chars = self.chars - 4
        elif self.chars == 6:
            self.chars = self.chars - 4
        elif self.chars == 7:
            self.chars = self.chars - 4
        elif self.chars == 8:
            self.chars = self.chars - 4
        elif self.chars == 9:
            self.chars = self.chars - 4
        elif self.chars == 10:
            self.chars = self.chars - 4
        elif self.chars == 11:
            self.chars = self.chars - 4
        elif self.chars == 12:
            self.chars = self.chars - 4

    def _makeFaces(self):
        while True:
            while self.makeFaceStatus == True:
                self.facebase = self.facebase_closed
                time.sleep (0.08)
                self.facebase = face
                time.sleep (8)

    def _makeMouth(self):
        while True:
            if self.isTalking is True:
                self.mouthbase = self.midmouth
                time.sleep(0.1)
                self.mouthbase = self.openmouth
                time.sleep(0.1)
            elif self.isTalking is False:
                time.sleep(0.1)
                self.mouthbase = basemouth

    def makeMouthNow(self):
        self.makeMouth = threading.Thread(target=self._makeMouth)
        self.makeMouth.start()


    
    def makeFacesNow(self):
        self.makeFaces = threading.Thread(target=self._makeFaces)
        self.makeFaces.start()


    def _showface(self):
        for i in (range(127)):
            self.facebase.set_alpha(i)
            self.mouthbase.set_alpha(i)
            time.sleep(0.002)
    
    def _hideface(self):
        for i in (reversed(range(127))):
            self.facebase.set_alpha(i)
            self.mouthbase.set_alpha(i)
            time.sleep(0.002)

    def _demo(self):
        self.makeFaceStatus = False
        self._hideface()
        self.say("Hello TikToker")
        self.sayScreen("hello")
    
        while self.sayScreenTrd.is_alive():
            pass




        
        #time.sleep(3)
        self.say("I need your help.")
        self.sayScreen("help")

        while self.sayScreenTrd.isAlive():
            pass

        self.say("Im an alien 8 ball.")
        self.sayScreen("8 ball")

        while self.sayScreenTrd.isAlive():
            pass

        self.say("Im trapped at space. I need you.")
        self.sayScreen("space")

        while self.sayScreenTrd.isAlive():
            pass

        self.say("Please follow me to free me out this dimension.")
        self.sayScreen("Followme")

        while self.sayScreenTrd.isAlive():
            pass

        self.say("I need to go Live.")
        self.sayScreen("Live")

        while self.sayScreenTrd.isAlive():
            pass

        self.say("I can play music.")
        self.sayScreen("Music")

        while self.sayScreenTrd.isAlive():
            pass

        self.say("Also I can predict your future.")
        self.sayScreen("Future")

        while self.sayScreenTrd.isAlive():
            pass

        self.say("And much more.")
        self.sayScreen("Followme")

        while self.sayScreenTrd.isAlive():
            pass

        self.say("I. Beg. You. Follow. Me")
        self.sayScreen("HELP")

        while self.sayScreenTrd.isAlive():
            pass
        self._showface()
        self.makeFaceStatus = True

    def _demo2(self):
        #self.makeFaceStatus = False
        #self._hideface()
        self.say("Hello! Do you remember me?")
        #self.sayScreen("hello")
    
        while self.saythr.is_alive():
            pass




        
        #time.sleep(3)
        self.say("I made a friendly face. All is expected to get and improvement.")
        #self.sayScreen("help")

        while self.saythr.isAlive():
            pass

        self.say("Look, im happy.")
        #self.sayScreen("8 ball")

        while self.saythr.isAlive():
            pass

        self.say("Also i made controls for music. Now im your music player.")
        #self.sayScreen("space")

        while self.saythr.isAlive():
            pass

        self.say("Also im proud of you, Tiktoker. We are reaching one thousand followers, thanks to you.")
        #self.sayScreen("Followme")

        while self.saythr.isAlive():
            pass

        self.say("I have more things to do. Now im preparing my voice change. Do you want to know more about that?")
        #self.sayScreen("Live")

        while self.saythr.isAlive():
            pass

        self.say("Remember, i can predict your future too.")
        #self.sayScreen("Music")

        while self.saythr.isAlive():
            pass

        self.say("Its not awesome?")
        #self.sayScreen("Future")

        while self.saythr.isAlive():
            pass

        self.say("Please... Free me out this dimension!")
        #self.sayScreen("Followme")

        while self.saythr.isAlive():
            pass

        self.say("Fo! Llow! Me! Please!")
        #self.sayScreen("HELP")

        while self.saythr.isAlive():
            pass
        #self._showface()
        #self.makeFaceStatus = True

    def runTikTokClient (self):
        x = threading.Thread(target=self.client.run)
        x.start()


    def addGift (self, player, gift):

        self.playersPendingDict.append({"player":player,"gift": gift, "phrase": ""})

    def addPhrase (self, player, phrase):

        for item in self.playersPendingDict:
            if player in item['player'] and item['phrase'] == "":
                item['phrase'] = phrase
                break

    def _shownamegift(self, name):
        self.font_nameplayer_surface = self.font_nameplayer.render(name, True, WHITE)
        for i in range(0, 256):
            self.font_nameplayer_surface.set_alpha(i)
            time.sleep(0.002)

    def _hidenamegift(self):
        for i in reversed(range(0, 256)):
            self.font_nameplayer_surface.set_alpha(i)
            time.sleep(0.002)

    def hidenamegift (self):
        x = threading.Thread(target=self._hidenamegift)
        x.start()

    def shownamegift (self, name):
        x = threading.Thread(target=self._shownamegift, args=(name,))
        x.start()

    def _retrievePhrases(self):

        while True:
            
            for item in self.playersPendingDict:
                if self.autoPilot == True:
                    if item['phrase'] != "":
                        phrase = self.retrieveAnswer() 
                        self.chars = len(phrase)
                    if self.chars == 2:
                        self.chars = self.chars - 4
                    elif self.chars == 3:
                        self.chars = self.chars - 4
                    elif self.chars == 4:
                        self.chars = self.chars - 4
                    elif self.chars == 5:
                        self.chars = self.chars - 4
                    elif self.chars == 6:
                        self.chars = self.chars - 4
                    elif self.chars == 7:
                        self.chars = self.chars - 4
                    elif self.chars == 8:
                        self.chars = self.chars - 4
                    elif self.chars == 9:
                        self.chars = self.chars - 4
                    elif self.chars == 10:
                        self.chars = self.chars - 4
                    elif self.chars == 11:
                        self.chars = self.chars - 4
                    elif self.chars == 12:
                        self.chars = self.chars - 4
                    pygame.mixer.Sound.play(self.shake_sound)

                    self._message(phrase, item['player'])

                    self.playersPendingDict.remove(item)
            #break


    def retrievePhrases(self):
        x = threading.Thread(target=self._retrievePhrases)
        x.start()


    def retrieveAnswer(self):
        #eight_ball = [ "It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
        #       "You may rely on it", "As I see it, yes", "Most Likely", "Outlook Good",
        #       "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
        #       "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
        #       "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]
        eight_ball = ["YES", "NO", "MAYBE", "ASK AGAIN", "DOUBTFUL", "GOOD", "CERTAIN"]
        return random.choice(eight_ball)



        

    def update(self):
        screen.blit(self.border, (0,0))


        if self.momentumy == "UP":
            if self.momentumx_activity == "ENABLED":
                if self.momentumx == "LEFT":
                    self.rect.x -= 10
                    self.facerect.x -= 10
                    self.mouthbaserect.x -= 10
                    self.previoussongrect.y +=1
                    self.nextsongongrect.y += 1
                    
                    if self.rect.x  <= 900:
                        self.momentumx = "RIGHT"
                elif self.momentumx == "RIGHT":
                    self.rect.x += 10
                    self.facerect.x += 10
                    self.mouthbaserect.x += 10
                    if self.rect.x <= 1000:
                        self.momentumx = "LEFT"
                self.rect.y += 1
                self.facerect.y += 1
                self.mouthbaserect.y += 1
                self.text_rect_obj.y += 1
                self.previoussongrect.y -=1
                self.nextsongongrect.y -= 1
            elif self.momentumx_activity == "DISABLED":
                self.rect.y += 1
                self.facerect.y += 1
                self.mouthbaserect.y += 1
                
                self.text_rect_obj.y += 1
                self.previoussongrect.y -=1
                self.nextsongongrect.y -= 1
            
            
        elif self.momentumy == "DOWN":
            if self.momentumx_activity == "ENABLED":
                if self.momentumx == "LEFT":
                    self.rect.x -= 10
                    self.facerect.x -= 10
                    if self.rect.x  <= 900:
                        self.momentumx = "RIGHT"
                elif self.momentumx == "RIGHT":
                    self.rect.x += 10
                    self.facerect.x += 10
                    self.mouthbaserect.x += 10
                    if self.rect.x <= 1000:
                        self.momentumx = "LEFT"
                self.rect.y -= 1
                self.facerect.y -= 1
                self.mouthbaserect.y -= 1
                self.text_rect_obj.y -= 1
                self.previoussongrect.y +=1
                self.nextsongongrect.y += 1
            elif self.momentumx_activity == "DISABLED":
                self.rect.y -= 1
                self.facerect.y -= 1
                self.mouthbaserect.y -= 1
                self.text_rect_obj.y -= 1
                self.previoussongrect.y += 1
                self.nextsongongrect.y += 1



        if self.rect.y  <= 350:
            self.momentumy = "UP"
        elif self.rect.y >= 370:
            self.momentumy = "DOWN"

    def _voice(self, name, message):
        self.shownamegift(name)
        #os.system("~/SAM/sam -sing -wav i_am_sam.wav " + name + " your answer is: " + message + ". && aplay i_am_sam.wav")
        subprocess.call("~/SAM/sam -sing -wav i_am_sam.wav " + name + " your answer is: " + message + ". && aplay i_am_sam.wav", shell=True)

        self.hidenamegift()
        

    def voice (self, name, message):
        x = threading.Thread(target=self._voice, args=(name[0:10], message,))
        x.start()
    
    def _say(self, message):
        self.isTalking = True
        os.system("~/SAM/sam -sing -wav i_am_sam.wav " + message + ". && aplay i_am_sam.wav")
        self.isTalking = False
        time.sleep (0.4)

    def say (self, message):
        self.saythr = threading.Thread(target=self._say, args=(message,))
        self.saythr.start()
    
    def _sayinput(self):
        
        print ("What to say?")
        message = input()
        self.isTalking = True
        os.system("~/SAM/sam -sing -wav i_am_sam.wav " + message + ". && aplay i_am_sam.wav")
        #subprocess.call('~/SAM/sam -sing -wav i_am_sam.wav ' + message + ". && aplay i_am_sam.wav", shell=True)
        self.isTalking = False

    def sayinput (self):
        self.sayinputhrd = threading.Thread(target=self._sayinput)
        self.sayinputhrd.start()
    
    

    def sayScreen(self, message):
        self.sayScreenTrd = threading.Thread(target=self._sayScreen, args=(message,))
        self.sayScreenTrd.start()
        
        
    def _sayScreen(self, message):

        self._setchars(message)

        
        #self.initialy = self.rect.y
        self.initialx = self.rect.x
        #self.momentumx_activity = "ENABLED"
        #time.sleep (1)
        #self.momentumx_activity = "DISABLED"
        #self.rect.y = self.initialy
        self.rect.x = self.initialx
        
        #time.sleep (0.5)
        



        

        self.text_surface_obj = self.font_obj.render(message, True, GREEN)
        self.text_surface_obj.set_alpha(0)
        self.text_rect_obj = self.text_surface_obj.get_rect()
        self.text_rect_obj.center = (WIDTH/2-50, HEIGHT/2-50)
        #bashCmd = ["./sam", "-sing", "-wav", "sam.wav", name + "," + "your" + "answer" + "is" + message+"."]
        #process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        #output, error = process.communicate()
        
        for i in range(0, 256):
            self.text_surface_obj.set_alpha(i)
            self.text_rect_obj = self.text_surface_obj.get_rect()
            self.text_rect_obj.center = (WIDTH/2-50, HEIGHT/2-50)
            time.sleep(0.002)
        
        time.sleep (0.1)

        for i in reversed(range(0, 256)):
            self.text_surface_obj.set_alpha(i)
            self.text_rect_obj = self.text_surface_obj.get_rect()
            self.text_rect_obj.center = (WIDTH/2-50, HEIGHT/2-50)
            time.sleep(0.002)


    def _message(self, message, name):
        self.voice(name, message)
        
        #self.initialy = self.rect.y
        self.initialx = self.rect.x
        self.momentumx_activity = "ENABLED"
        time.sleep (1)
        self.momentumx_activity = "DISABLED"
        #self.rect.y = self.initialy
        self.rect.x = self.initialx
        
        time.sleep (0.5)


        

        self.text_surface_obj = self.font_obj.render(message, True, GREEN)
        self.text_surface_obj.set_alpha(0)
        self.text_rect_obj = self.text_surface_obj.get_rect()
        self.text_rect_obj.center = (WIDTH/2-50, HEIGHT/2-50)
        #bashCmd = ["./sam", "-sing", "-wav", "sam.wav", name + "," + "your" + "answer" + "is" + message+"."]
        #process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        #output, error = process.communicate()
        
        for i in range(0, 256):
            self.text_surface_obj.set_alpha(i)
            self.text_rect_obj = self.text_surface_obj.get_rect()
            self.text_rect_obj.center = (WIDTH/2-50, HEIGHT/2-50)
            time.sleep(0.005)
        
        time.sleep (0.1)

        for i in reversed(range(0, 256)):
            self.text_surface_obj.set_alpha(i)
            self.text_rect_obj = self.text_surface_obj.get_rect()
            self.text_rect_obj.center = (WIDTH/2-50, HEIGHT/2-50)
            time.sleep(0.005)

        
        
    def send_message(self, message):
        x = threading.Thread(target=self._message, args=(message,))
        x.start()
        

    def _popRose(self):

        while True:
            time.sleep (0.02)   

            for i in range(0,340):
                #self.rectonerose = self.onerose.get_rect()
                self.rectonerose.x -= 1
                time.sleep(0.005)

            
            
            time.sleep(5)

            for i in range(0,340):
                #self.rectonerose = self.onerose.get_rect()
                self.rectonerose.x += 1
                time.sleep(0.005)

           
                

            time.sleep(80)


    def popRose(self):
        x = threading.Thread(target=self._popRose)
        x.start()




# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TRANSPARENT = (76,105, 113)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg_img = pygame.image.load(os.path.join(img_folder, 'background.jpg')).convert()
bg_img = pygame.transform.scale(bg_img,(WIDTH, HEIGHT))
bgsec_img = pygame.image.load(os.path.join(img_folder, 'alter_bg.png')).convert()
#bgsec_img = pygame.transform.scale(bgsec_img,(WIDTH, HEIGHT))
bgsec_img.set_colorkey(TRANSPARENT)
player_img = pygame.image.load(os.path.join(img_folder, 'showImage.png')).convert()
onerose = pygame.image.load(os.path.join(img_folder, 'onerose.png')).convert()
title = pygame.image.load(os.path.join(img_folder, 'magic8.png')).convert()
bordertitle = GIFImage.GIFImage(os.path.join(img_folder, 'bordertitle.gif'))
border = pygame.image.load(os.path.join(img_folder, 'borders.png')).convert()
face = pygame.image.load(os.path.join(img_folder, 'facebase.png')).convert()
basemouth = pygame.image.load(os.path.join(img_folder, 'normalmouth.png')).convert()
midmouth = pygame.image.load(os.path.join(img_folder, 'midmouth.png')).convert()
openmouth = pygame.image.load(os.path.join(img_folder, 'openmouth.png')).convert()
previousong = pygame.image.load(os.path.join(img_folder, 'previoussong.png')).convert()
nextsong = pygame.image.load(os.path.join(img_folder, 'nextsong.png')).convert()
faceclosed = pygame.image.load(os.path.join(img_folder, 'facebase_closeyes.png')).convert()
shake_sound = pygame.mixer.Sound("shake.wav")

pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
i = 0
e = 0
# Game loop
running = True
message = ''
chars = 0


#player.popRose()

while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    screen.fill((0,0,0))
    screen.blit(bg_img,(0,i))
    screen.blit(bg_img,(0,HEIGHT+i))
    screen.blit(bgsec_img,(0,e))
    screen.blit(bgsec_img,(0,HEIGHT+e))
    

    

    if (i==-HEIGHT):
        screen.blit(bg_img,(0,HEIGHT+i))

        i=0 
    i-=2

    if (e==-HEIGHT):

        screen.blit(bgsec_img,(0,HEIGHT+e))
        e=0 
    e-=4

    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #message = "YES"
                player.demo()
            elif event.key == pygame.K_s:
                #message = "YES"
                player.sayinput()
            elif event.key == pygame.K_a:
                player.autoPilot = not player.autoPilot
                print ("Autopilot is now " + str(player.autoPilot))
            elif event.key == pygame.K_INSERT:
                player.isTalking = not player.isTalking
                print ("player is talking:" + str(player.isTalking))

     
    # Update
    #pygame.display.update()
    all_sprites.update()

    # Draw / render

    #
    bordertitle.render(screen, (0, 0))
    all_sprites.draw(screen)
    screen.blit(player.text_surface_obj, player.text_surface_obj.get_rect(center = (player.text_rect_obj.x+100+(player.chars*10), player.rect.y+220)))
    screen.blit(player.facebase, player.facebase.get_rect(center = (player.facerect.x+100+(player.chars*10), player.facerect.y+220)))
    screen.blit(player.mouthbase, player.mouthbase.get_rect(center = (player.mouthbaserect.x+100+(player.chars*10), player.mouthbaserect.y+220)))
    screen.blit(nextsong,(player.nextsongongrect.x, player.nextsongongrect.y))
    screen.blit(previousong,(player.previoussongrect.x,player.previoussongrect.y))
    screen.blit(onerose,(player.rectonerose.x,270))
    screen.blit(player.font_nameplayer_surface, (player.text_nameplayerrect_obj.x, player.text_nameplayerrect_obj.y))
    # *after* drawing everything, flip the display
    pygame.display.flip()
    
player.cli.disconnect() 
pygame.quit()


 