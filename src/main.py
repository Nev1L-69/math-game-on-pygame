import random
import pygame

pygame.init()

# Установите размеры экрана
SCREEN_WIDTH = 1400 
SCREEN_HEIGHT = 600

# screen and title
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Math simulator buble game")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)
YELLOW = (255,255,0)
LIGHT_BLACK = (37,37,37)
GREEN = (0,255,0)


# Надписи
font = pygame.font.Font(None, 25)
big_font = pygame.font.Font(None, 35)

text_1 = big_font.render("1", True, RED)
text_1_pressed = big_font.render("1", True, BLACK)
text_1_rect = text_1.get_rect(center = (1050, 300))

text_2 = big_font.render("2", True, RED)
text_2_pressed = big_font.render("2", True, BLACK)
text_2_rect = text_1.get_rect(center = (1100, 300))

text_3 = big_font.render("3", True, RED)
text_3_pressed = big_font.render("3", True, BLACK)
text_3_rect = text_1.get_rect(center = (1150, 300))

text_4 = big_font.render("4", True, RED)
text_4_pressed = big_font.render("4", True, BLACK)
text_4_rect = text_1.get_rect(center = (1050, 350))

text_5 = big_font.render("5", True, RED)
text_5_pressed = big_font.render("5", True, BLACK)
text_5_rect = text_1.get_rect(center = (1100, 350))

text_6 = big_font.render("6", True, RED)
text_6_pressed = big_font.render("6", True, BLACK)
text_6_rect = text_1.get_rect(center = (1150, 350))

text_7 = big_font.render("7", True, RED)
text_7_pressed = big_font.render("7", True, BLACK)
text_7_rect = text_1.get_rect(center = (1050, 400))

text_8 = big_font.render("8", True, RED)
text_8_pressed = big_font.render("8", True, BLACK)
text_8_rect = text_1.get_rect(center = (1100, 400))

text_9 = big_font.render("9", True, RED)
text_9_pressed = big_font.render("9", True, BLACK)
text_9_rect = text_1.get_rect(center = (1150, 400))

text_0 = big_font.render("0", True, RED)
text_0_pressed = big_font.render("0", True, BLACK)
text_0_rect = text_1.get_rect(center = (1100, 450))


text_title = big_font.render("Your answer? ", True, GREEN)
text_title_rect = text_title.get_rect(center = (1100, 110))

text_score = big_font.render("Your score: ", True, GREEN)
text_score_rect = text_score.get_rect(center = (1070, 50))

text_lose_score = big_font.render("Your score: ", True, RED)
text_lose_score_rect = text_lose_score.get_rect(center = (700, 400))

text_lost = big_font.render("The city burned, you have lost!", True, RED)
text_lost_rect = text_lost.get_rect(center = (700, 200))

text_win = big_font.render("The city saved, you win", True, YELLOW)
text_win_rect = text_win.get_rect(center = (700, 200))

text_to_main_menu = big_font.render("To main menu", True, RED)
text_to_main_menu_rect = text_to_main_menu.get_rect(center = (700, 300))


text_main_menu_start = big_font.render("Deffend the city", True, YELLOW)
text_main_menu_start_rect = text_main_menu_start.get_rect(center = (700,270))


# картинки меню
main_menu_city_image = pygame.image.load('src/images/city/MainMenuCity.png').convert_alpha()

city_in_game_image = pygame.image.load('src/images/city/CityInGame.png').convert_alpha()

in_game_background = pygame.image.load('src/images/city/sky.png').convert_alpha()

lose_background = pygame.image.load('src/images/city/LoseCity.png').convert_alpha()

calc_menu = pygame.image.load('src/images/Calculator/CalcMenu.png').convert_alpha()

meteor = [
          pygame.image.load('src/images/meteor/rotationY1.png').convert_alpha(),
          pygame.image.load('src/images/meteor/rotationY2.png').convert_alpha(),
          pygame.image.load('src/images/meteor/rotationY3.png').convert_alpha(),
          pygame.image.load('src/images/meteor/rotationY4.png').convert_alpha(),
          pygame.image.load('src/images/meteor/rotationY5.png').convert_alpha(),
          pygame.image.load('src/images/meteor/rotationY6.png').convert_alpha(),
          pygame.image.load('src/images/meteor/rotationY7.png').convert_alpha(),
          pygame.image.load('src/images/meteor/rotationY8.png').convert_alpha(),
          pygame.image.load('src/images/meteor/rotationY9.png').convert_alpha(),
          pygame.image.load('src/images/meteor/rotationY10.png').convert_alpha(),
          pygame.image.load('src/images/meteor/rotationY11.png').convert_alpha(),
          pygame.image.load('src/images/meteor/rotationY12.png').convert_alpha(),
          pygame.image.load('src/images/meteor/rotationY13.png').convert_alpha(),
          pygame.image.load('src/images/meteor/rotationY14.png').convert_alpha(),
          pygame.image.load('src/images/meteor/rotationY15.png').convert_alpha(),
          pygame.image.load('src/images/meteor/rotationY16.png').convert_alpha(),
          pygame.image.load('src/images/meteor/rotationY17.png').convert_alpha(),
          pygame.image.load('src/images/meteor/rotationY18.png').convert_alpha(),
]


explosion = [
    pygame.image.load('src/images/explosion/Explosion1.png').convert_alpha(),
    pygame.image.load('src/images/explosion/Explosion2.png').convert_alpha(),
    pygame.image.load('src/images/explosion/Explosion3.png').convert_alpha(),
    pygame.image.load('src/images/explosion/Explosion4.png').convert_alpha(),
    pygame.image.load('src/images/explosion/Explosion5.png').convert_alpha(),
    pygame.image.load('src/images/explosion/Explosion6.png').convert_alpha(),
    pygame.image.load('src/images/explosion/Explosion7.png').convert_alpha(),
    pygame.image.load('src/images/explosion/Explosion8.png').convert_alpha(),
    pygame.image.load('src/images/explosion/Explosion9.png').convert_alpha(),
    pygame.image.load('src/images/explosion/Explosion10.png').convert_alpha(),
    pygame.image.load('src/images/explosion/Explosion11.png').convert_alpha(),
    pygame.image.load('src/images/explosion/Explosion12.png').convert_alpha(),
    

]



# Определите ограничение по FPS
clock = pygame.time.Clock()
FPS = 60  # Максимальное количество кадров в секунду


def generate_num1():
    return random.randint(10,40)

def generate_num2():
    return random.randint(10,40)


def generate_sum_eq(num1, num2):
    return num1+num2

def generate_diff_eq(num1, num2): 
    return num1 - num2 

# кдасс каждого кружочка с выражением
class Buble:
    def __init__(self):
        self.radius = 35
        self.x = random.randint(self.radius, 800 - self.radius)
        self.y = -self.radius
        self.speed = 1.2
        self.a = random.randint(1,2)
        self.num1 = generate_num1()
        self.num2 = generate_num2()
        self.explode_trigger = 0
        self.cnt = 0
        if self.a == 1:
            self.answer = generate_sum_eq(self.num1, self.num2)
            
        else: 
            self.answer = generate_diff_eq(self.num1, self.num2)
            



    def move(self):
        self.y += self.speed

    def explode(self):
        if self.explode_trigger == 1:
            screen.blit(explosion[self.cnt], (self.x-50, self.y-50))
            self.cnt+=1
            self.y -= self.speed
            self.y -= 5
            if self.cnt > 11:
                self.explode_trigger = 2

    def draw(self, screen, cnt):
        if self.explode_trigger == 0:
            pygame.draw.circle(screen, RED, (self.x, int(self.y)), self.radius)
            screen.blit(meteor[cnt], (self.x - 52, self.y - 41))

            text1 = font.render(str(self.num1), True, WHITE)
            text_rect1 = text1.get_rect(center=(self.x, int(self.y - 15)))

            text2 = font.render(str(self.num2), True, WHITE)
            text_rect2 = text2.get_rect(center=(self.x, int(self.y + 15)))
            screen.blit(text1, text_rect1)
            if self.a == 1:
                plus = font.render(str("+"), True, WHITE)
                plus_rect = plus.get_rect(center = (self.x, int(self.y)))
                screen.blit(plus, plus_rect)
            else:
                minus = font.render(str("-"), True, WHITE)
                minus_rect = minus.get_rect(center = (self.x, int(self.y)))
                screen.blit(minus, minus_rect)
            screen.blit(text2, text_rect2)


# Класс поля которого если касаться то проиграешь
class Rectangle:
    def __init__(self):
        self.width = 800
        self.height = 30
        self.x = 0
        self.y = SCREEN_HEIGHT - self.height

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height))
        screen.blit(city_in_game_image, (0,460))
        
   

# вывод циферблата
def blit_numbers():
    screen.blit(text_1, text_1_rect)
    screen.blit(text_2, text_2_rect)
    screen.blit(text_3, text_3_rect)
    screen.blit(text_4, text_4_rect)
    screen.blit(text_5, text_5_rect)
    screen.blit(text_6, text_6_rect)
    screen.blit(text_7, text_7_rect)
    screen.blit(text_8, text_8_rect)
    screen.blit(text_9, text_9_rect)
    screen.blit(text_0, text_0_rect)


# Создание объектов
circles = []
rectangle = Rectangle()
total_answer = ""

timer = pygame.USEREVENT + 1 
timer_fast = pygame.USEREVENT + 1 
button_cnt = 0
buble_cnt = 0
button_ready = True
total_score = 0
hearts = 5
hearts_text = "Your hearts: " + str(hearts)

# частота появления
frequancy = 25

is_minus = 0

# таймер
pygame.time.set_timer(timer, 100)
pygame.time.set_timer(timer_fast, 100)

# Основной игровой цикл
running = True
start_game = False
main_menu = True
lost = False
win = False
answer_cnt = 0
cnt = 0


#Звуки
explosion_sound = pygame.mixer.Sound('src/sounds/explodemini.wav')
pop_sound = pygame.mixer.Sound('src/sounds/pop2.ogg')




while running:

    mouse = pygame.mouse.get_pos() 
    keys = pygame.key.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == timer: 
            buble_cnt +=1
        
        if event.type == timer_fast:
            cnt+=1
            if cnt > 17:
                cnt = 0
            
        # проверка на нажатые клавиши для циферблата
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                total_answer += "1"
                screen.blit(text_1_pressed, text_1_rect)

            if event.key == pygame.K_2:
                total_answer += "2"
                screen.blit(text_2_pressed, text_2_rect)

            if event.key == pygame.K_3:
                total_answer += "3"
                screen.blit(text_3_pressed, text_3_rect)

            if event.key == pygame.K_4:
                total_answer += "4"
                screen.blit(text_4_pressed, text_4_rect)

            if event.key == pygame.K_5:
                total_answer += "5"
                screen.blit(text_5_pressed, text_5_rect)

            if event.key == pygame.K_6:
                total_answer += "6"
                screen.blit(text_6_pressed, text_6_rect)
                
            if event.key == pygame.K_7:
                total_answer += "7"
                screen.blit(text_7_pressed, text_7_rect)

            if event.key == pygame.K_8:
                total_answer += "8"
                screen.blit(text_8_pressed, text_8_rect)

            if event.key == pygame.K_9:
                total_answer += "9"
                screen.blit(text_9_pressed, text_9_rect)

            if event.key == pygame.K_0:
                total_answer += "0"
                screen.blit(text_0_pressed, text_0_rect)

            if event.key == pygame.K_MINUS:
                if is_minus == 0:
                    total_answer = "-" + total_answer
                    is_minus = 1
                else:
                    total_answer = total_answer[1:]
                    is_minus = 0
                screen.blit(text_0_pressed, text_0_rect)

            if event.key == pygame.K_BACKSPACE:
                if total_answer != "" or total_answer != "-":
                    total_answer = total_answer[:-1]

            if event.key == pygame.K_RETURN and total_answer!="" and total_answer!="-":
                for circle in circles:
                    if int(total_answer) == circle.answer:
                        circles.remove(circle)
                        pop_sound.set_volume(0.2)
                        pop_sound.play()
                        total_score += 100
                        answer_cnt+=1
                        if answer_cnt % 2 == 0:
                            frequancy -=1
                        
                total_answer = ""
                is_minus = 0  



    if main_menu:
        screen.blit(main_menu_city_image, (0,0))
        screen.blit(main_menu_city_image, (960,0))
        
        screen.blit(text_main_menu_start, text_main_menu_start_rect)
        if text_main_menu_start_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            start_game = True
            hearts = 5
            hearts_text = "Your hearts: " + str(hearts)
            frequancy = 25
            total_score = 0
            buble_cnt = 0
            circles = []
            main_menu = False
            screen.fill(BLACK)
    
    if lost:
        screen.fill(WHITE)
        screen.blit(lose_background, (0,0))
        screen.blit(lose_background, (480,0))
        screen.blit(lose_background, (960,0))

        text_total_score = big_font.render(str(total_score), True, RED)
        text_total_score_rect = text_total_score.get_rect(center = (850, 400))


        screen.blit(text_total_score, text_total_score_rect)
        screen.blit(text_lost, text_lost_rect)
        screen.blit(text_to_main_menu, text_to_main_menu_rect)
        screen.blit(text_lose_score, text_lose_score_rect)


        if text_to_main_menu_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            lost = False
            main_menu = True



    if win:
        screen.blit(main_menu_city_image, (0,-200))
        screen.blit(main_menu_city_image, (960,-200))


        screen.blit(text_win, text_win_rect)
        text_to_main_menu = big_font.render("To main menu", True, YELLOW)
        text_to_main_menu_rect = text_to_main_menu.get_rect(center = (700, 300))
        screen.blit(text_to_main_menu, text_to_main_menu_rect)



        if text_to_main_menu_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            win = False
            main_menu = True

            


    if start_game:
        # создает кружочек с выражением раз в какойто период

        screen.fill(LIGHT_BLACK)
        screen.blit(in_game_background, (0,0))
        screen.blit(in_game_background, (320,0))
        screen.blit(calc_menu, (950, 140))

        rectangle.draw(screen)

        if total_score>1000:
            start_game = False
            win = True

        if hearts<=0:
            start_game = False
            lost = True
        
        if buble_cnt == frequancy:
            circles.append(Buble())
            buble_cnt = 0


        # Обновление позиции кружочков
        for circle in circles:
            circle.move()
            circle.explode()
            if circle.explode_trigger == 2:
                circles.remove(circle)

            if circle.y > SCREEN_HEIGHT + circle.radius:  # Если кружочек вышел за пределы экрана, удаляем его
                circles.remove(circle)

        # Проверка столкновения кружочков с прямоугольником
        for circle in circles:
            if (circle.y + circle.radius > rectangle.y) and (circle.x > rectangle.x and circle.x < rectangle.x + rectangle.width):
                hearts -=1
                hearts_text = "Your hearts: " + str(hearts)
                circle.explode_trigger = 1
                explosion_sound.set_volume(0.1)
                explosion_sound.play()
                
                
        

        # Отрисовка
        screen.blit(text_title, text_title_rect)
        
        blit_numbers()

        
        
        answer_text = font.render(total_answer, True, RED)
        answer_text_rect = answer_text.get_rect(center = (1100, 260))

        text_total_score = big_font.render(str(total_score), True, GREEN)
        text_total_score_rect = text_total_score.get_rect(center = (1170, 50))

        text_health = big_font.render(hearts_text, True, GREEN)
        text_health_rect = text_health.get_rect(center = (1300, 90))

        screen.blit(answer_text, answer_text_rect)
        screen.blit(text_health, text_health_rect)
        screen.blit(text_score, text_score_rect)
        screen.blit(text_total_score, text_total_score_rect)
        
        for circle in circles:
            circle.draw(screen, cnt)


    # Обновление экрана
    pygame.display.flip()
    
    # Ограничение по FPS
    clock.tick(FPS)

pygame.quit()
