if __name__ == "__main__":
    import pygame, random

    pygame.init()
    pygame.mixer.init() 

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.color = GREEN
            self.radius = 10
            self.speed = 5
            self.live = True
            self.rect = pygame.Rect(((WIDTH // 4)*3 - self.radius, HEIGHT // 2 - self.radius), (self.radius * 2, self.radius * 2))

        def draw(self, screen):
            self.rect = pygame.Rect((self.rect.x, self.rect.y), (self.radius * 2, self.radius * 2))
            pygame.draw.circle(screen, self.color, self.rect.center, self.radius)

        def move(self):
            global player, bg
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
            if self.live:
                if keys[pygame.K_LEFT]:
                    self.rect.x -= self.speed
                if keys[pygame.K_RIGHT]:
                    self.rect.x += self.speed
                if keys[pygame.K_UP]:
                    self.rect.y -= self.speed
                if keys[pygame.K_DOWN]:
                    self.rect.y += self.speed

                if self.rect.x <=0:
                    self.rect.x = 0
                if self.rect.x >= WIDTH:
                    self.rect.x = WIDTH
                if self.rect.y <= 0:
                    self.rect.y = 0
                if self.rect.y >= HEIGHT:
                    self.rect.y = HEIGHT
            '''if not self.live:
                if keys[pygame.K_SPACE]:
                    player=None
                    player=Player()
                    bg=BROWN
                    player.live=True'''
            
            if self.rect.x <=0:
                self.rect.x = 0
            elif self.rect.right >= WIDTH:
                self.rect.right = WIDTH
            if self.rect.y <= 0:
                self.rect.y = 0
            elif self.rect.bottom >= HEIGHT:
                self.rect.bottom = HEIGHT

        def colliderect(self, other):
            return self.rect.colliderect(other.rect)

        def update(self):
            self.move()
            self.draw(SCREEN)

    class Player_2(pygame.sprite.Sprite):
        global WIDTH, HEIGHT
        def __init__(self):
            super().__init__()
            self.color = GREEN_2
            self.radius = 10
            self.speed = 5
            self.live = True
            self.rect = pygame.Rect((WIDTH // 4 - self.radius, HEIGHT // 2 - self.radius), (self.radius * 2, self.radius * 2))

        def draw(self, screen):
            self.rect = pygame.Rect((self.rect.x, self.rect.y), (self.radius * 2, self.radius * 2))
            pygame.draw.circle(screen, self.color, self.rect.center, self.radius)

        def move(self):
            global player, bg
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
            if self.live:
                if keys[pygame.K_a]:
                    self.rect.x -= self.speed
                if keys[pygame.K_d]:
                    self.rect.x += self.speed
                if keys[pygame.K_w]:
                    self.rect.y -= self.speed
                if keys[pygame.K_s]:
                    self.rect.y += self.speed
            '''if not self.live:
                if keys[pygame.K_SPACE]:
                    player=None
                    player=Player()
                    bg=BROWN
                    player.live=True'''
            
            if self.rect.x <=0:
                self.rect.x = 0
            elif self.rect.right >= WIDTH:
                self.rect.right = WIDTH
            if self.rect.y <= 0:
                self.rect.y = 0
            elif self.rect.bottom >= HEIGHT:
                self.rect.bottom = HEIGHT

        def colliderect(self, other):
            return self.rect.colliderect(other.rect)

        def update(self):
            self.move()
            self.draw(SCREEN)

    class Enemy(pygame.sprite.Sprite):
        global RED, RED2, RED3
        def __init__(self):
            super().__init__()
            self.color = random.choice([RED, RED2, RED3])
            self.radius = 8
            self.counter = 0
            self.speed = random.randint(3, 5)
            self.tick_x = random.randint(1, 150)
            self.tick_y = random.randint(1, 150)
            self.direction_x = random.choice(['LEFT', 'RIGHT'])
            self.direction_y = random.choice(['UP', 'DOWN'])
            self.rect = pygame.Rect((random.randint(0, WIDTH), random.randint(0, HEIGHT)), (self.radius * 2, self.radius * 2))
            self.live = True

        def draw(self, screen):
            self.rect = pygame.Rect((self.rect.x, self.rect.y), (self.radius * 2, self.radius * 2))
            pygame.draw.circle(screen, self.color, self.rect.center, self.radius)

        def move(self):
            if self.live:
                self.counter += 1
                if self.counter % self.tick_x==0:
                    self.direction_x = random.choice(['LEFT', 'RIGHT', 'NO_X'])
                if self.counter % self.tick_y==0:
                    self.direction_y = random.choice(['UP', 'DOWN', 'NO_Y'])
                else:
                    if self.direction_x == 'LEFT':
                        self.rect.x -= self.speed
                    elif self.direction_x == 'RIGHT':
                        self.rect.x += self.speed
                    if self.direction_y == 'UP':
                        self.rect.y -= self.speed
                    elif self.direction_y == 'DOWN':
                        self.rect.y += self.speed

        def stop(self):
            if self.rect.x <=0 or self.rect.x >= WIDTH or self.rect.y <= 0 or self.rect.y >= HEIGHT:
                self.direction_x = random.choice(['LEFT', 'RIGHT'])
                self.direction_y = random.choice(['UP', 'DOWN'])

        def colliderect(self, other):
            return self.rect.colliderect(other.rect)
        
        def update(self):
            self.move()
            self.stop()
            self.draw(SCREEN)

    class Points(pygame.sprite.Sprite):
        global WHITE, WHITE2, WHITE3
        def __init__(self):
            super().__init__()
            self.color = random.choice([WHITE, WHITE2, WHITE3])
            self.radius = random.randint(4,6)
            self.rect = pygame.Rect((random.randint(0, WIDTH), random.randint(0, HEIGHT)), (self.radius * 2, self.radius * 2))

        def draw(self, screen):
            pygame.draw.circle(screen, self.color, self.rect.center, self.radius)

        def colliderect(self, other):
            return self.rect.colliderect(other.rect)

        def update(self):
            self.draw(SCREEN)

    def collision():
        global bg, death_enemies
        if not player.live and not player_2.live:
            bg=RED
            points.empty()
            enemies.empty()
        for enemy in enemies:
            if player_2.colliderect(enemy):
                if player_2.radius >= enemy.radius:
                    player_2.radius += 2
                    enemies.remove(enemy)
                    death_enemies += 1
                else:
                    player_2.color = BLACK
                    player_2.live = False
            if player.colliderect(enemy):
                if player.radius >= enemy.radius:
                    player.radius += 2
                    enemies.remove(enemy)
                    death_enemies += 1
                else:
                    player.color = BLACK
                    player.live = False
                    
            for enemy2 in enemies:
                if enemy != enemy2 and enemy.colliderect(enemy2):
                    if enemy.radius >= enemy2.radius:
                        enemy.radius += enemy2.radius // 2
                        enemies.remove(enemy2)
                    else:
                        enemy2.radius += enemy.radius // 2
                        enemies.remove(enemy)

        for point in points:
            if player.colliderect(point) and player.live:
                player.radius += 1
                points.remove(point)
            if player_2.colliderect(point) and player_2.live:
                player_2.radius += 1
                points.remove(point)
            for enemy in enemies:
                if enemy.colliderect(point):
                    enemy.radius += 2
                    points.remove(point)

        if player.colliderect(player_2) and not player_2.live:
            player_2.live = True
            player_2.color = GREEN_2
            player.radius += 1
        if player_2.colliderect(player) and not player.live:
            player.live = True
            player.color = GREEN
            player_2.radius += 1

    def adding():
        if len(enemies)==0 and player.live:
            for i in range(15):
                enemy=Enemy()
                enemies.add(enemy)
        if random.randint(0,30)==1 and player.live:
            point=Points()
            points.add(point)
        if len(enemies) < 15 and player.live:
            #if random.randint(0,10)==1:
                enemy=Enemy()
                enemies.add(enemy)
    
    def text():
        global bg, player, player_2, death_enemies, starting,level, win_score
        if not starting:
            font = pygame.font.Font(None, 36)
            text_surface = font.render(f'Sötétzöld tömeg : {player.radius-9}', True, BLACK)
            text_rect = text_surface.get_rect(topright=(WIDTH-30, 30))
            SCREEN.blit(text_surface, text_rect)

            font = pygame.font.Font(None, 36)
            text_surface = font.render(f'Világoszöld tömeg: {player_2.radius-9}', True, BLACK)
            text_rect = text_surface.get_rect(topleft=(30, 30))
            SCREEN.blit(text_surface, text_rect)

            font = pygame.font.Font(None, 48)
            text_surface = font.render(f'{level}. szint - Győzz még le: {win_score-death_enemies}', True, BLACK)
            text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT-30))
            SCREEN.blit(text_surface, text_rect)

        if not player.live and not player_2.live:   
            font = pygame.font.Font(None, 56)
            text_surface = font.render(f'MEGHALTÁL!', True, WHITE)
            text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            SCREEN.blit(text_surface, text_rect)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                    player=None
                    player_2=None
                    player=Player()
                    player_2=Player_2()
                    bg=BROWN
                    death_enemies=0
                    win_score=10
                    level=1

        if starting:
            #SCREEN.fill(BROWN)
            font = pygame.font.Font(None, 92)
            text_surface = font.render(f'Agar.1848!', True, RED)
            text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            SCREEN.blit(text_surface, text_rect)

            font = pygame.font.Font(None, 36)
            text_surface = font.render(f'Csapataink harcban állnak!', True, GREEN)
            text_rect = text_surface.get_rect(center=(WIDTH // 2, (HEIGHT // 2)+60))
            SCREEN.blit(text_surface, text_rect)

            font = pygame.font.Font(None, 36)
            text_surface = font.render(f'Gyűjts magad köré a tömeget!', True, GREEN)
            text_rect = text_surface.get_rect(center=(WIDTH // 2, (HEIGHT // 2)+100))
            SCREEN.blit(text_surface, text_rect)

            font = pygame.font.Font(None, 36)
            text_surface = font.render(f'Győzd le az ellenséges csapatokat!', True, GREEN)
            text_rect = text_surface.get_rect(center=(WIDTH // 2, (HEIGHT // 2)+140))
            SCREEN.blit(text_surface, text_rect)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                    starting=False

        if death_enemies>=win_score:   
            SCREEN.fill(GREEN)
            SCREEN.blit(bg_surf, (0, 0))
            enemies.empty()
            points.empty()
            font = pygame.font.Font(None, 96)
            text_surface = font.render(f'GYŐZELEM!', True, WHITE)
            text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            SCREEN.blit(text_surface, text_rect)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                    player=None
                    player_2=None
                    player=Player()
                    player_2=Player_2()
                    bg=BROWN
                    death_enemies=0
                    enemies.empty()
                    points.empty()
                    level+=1
                    win_score=10*level

    RED=(255,0,0)
    RED2=(124,10,2)
    RED3=(164,90,82)
    WHITE=(255,255,255)
    WHITE2=(255,250,200)
    WHITE3=(245,245,220)
    GREEN=(3,100,64)
    GREEN_2=(0,150,0)
    BLUE=(0,0,255)
    BLACK=(0,0,0)
    BROWN=(193,162,141,128)
    FPS=60
    bg=BROWN
    death_enemies=0 
    level=1
    win_score=10
    music='assets/music-1.wav'
    pygame.mixer.music.load(music)
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)

    #PLATFORM_WIDTH=3000
    #PLATFORM_HEIGHT=3000

    MONITOR=pygame.display.Info()
    WIDTH=MONITOR.current_w
    HEIGHT=MONITOR.current_h
    transparent_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    transparent_surface.fill(BROWN)
    SCREEN = pygame.display.set_mode((0, 0), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN )
    background_image = pygame.image.load("assets/bg-11.png").convert_alpha()
    original_width, original_height = background_image.get_size()
    new_width = WIDTH
    new_height = int(original_height * (WIDTH / original_width))
    bg_surf = pygame.transform.scale(background_image, (new_width, new_height))
    #SCREEN1 = pygame.Surface((WIDTH//2, HEIGHT))
    #SCREEN2 = pygame.Surface((WIDTH//2, HEIGHT))

    pygame.display.set_caption('Agar.1848')
    clock=pygame.time.Clock()

    player=Player()
    player_2=Player_2()
    enemies=pygame.sprite.Group()
    points=pygame.sprite.Group()

    starting = True
    running=True 
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

        '''SCREEN1.fill(bg) 
        SCREEN2.fill(bg)
        SCREEN.blit(SCREEN1, (0, 0))
        SCREEN.blit(SCREEN2, (WIDTH//2, 0))'''
        
        SCREEN.fill(bg)
        SCREEN.blit(bg_surf, (0, 0))
        text()
        if not starting:
            player.update()
            player_2.update()
            enemies.update()
            points.update()
            collision()
            adding()

        pygame.display.update() 
        clock.tick(FPS)

    pygame.quit()