import random
import sys
import time

import psycopg2
import pygame

from config import config

pygame.init()
WIDTH, HEIGHT = 600, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 213, 128)
BROWN = (150, 75, 0)
LEVEL_CONSTANT = 4
NUMBER_OF_WALLS = 12

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BLOCK_SIZE = 30
pygame.display.set_caption('Snake v0')


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Food:
    def __init__(self, x, y):
        self.location = Point(x, y)
        self.weight = random.randint(1, 3)

    @property
    def x(self):
        return self.location.x

    @property
    def y(self):
        return self.location.y

    def update(self):
        pygame.draw.rect(
            SCREEN,
            YELLOW,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )


class Wall:
    def __init__(self, x, y):
        self.location = Point(x, y)

    @property
    def x(self):
        return self.location.x

    @property
    def y(self):
        return self.location.y

    def update(self):
        pygame.draw.rect(
            SCREEN,
            BROWN,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )


class Snake:
    def __init__(self):
        self.points = [
            Point(WIDTH // BLOCK_SIZE // 2, HEIGHT // BLOCK_SIZE // 2),
            Point(WIDTH // BLOCK_SIZE // 2 + 1, HEIGHT // BLOCK_SIZE // 2),
        ]

    def update(self):
        head = self.points[0]

        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        for body in self.points[1:]:
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )

    def move(self, dx, dy):
        for idx in range(len(self.points) - 1, 0, -1):
            self.points[idx].x = self.points[idx - 1].x
            self.points[idx].y = self.points[idx - 1].y

        self.points[0].x += dx
        self.points[0].y += dy

        head = self.points[0]
        if head.x > WIDTH // BLOCK_SIZE:
            head.x = 0
        elif head.x < 0:
            head.x = WIDTH // BLOCK_SIZE - 1
        elif head.y > HEIGHT // BLOCK_SIZE:
            head.y = 0
        elif head.y < 0:
            head.y = HEIGHT // BLOCK_SIZE - 1

    def check_collision(self, food):
        if self.points[0].x != food.x:
            return False
        if self.points[0].y != food.y:
            return False
        return True


def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, (x, 0), (x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, (0, y), (WIDTH, y), width=1)


username: str = ""
user_id: int = -1


def main():
    running = True
    snake = Snake()
    food = Food(5, 5)
    dx, dy = 0, 0

    def gen_food():
        while True:
            food_x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
            food_y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
            if walls.count(Wall(food_x, food_y)) == 0:
                break
        food.location.x = food_x
        food.location.y = food_y
        food.weight = random.randint(1, 3)

    walls = []
    for _ in range(NUMBER_OF_WALLS):
        while True:
            wall_x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
            wall_y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
            if walls.count(Wall(wall_x, wall_y)) == 0:
                break

        walls.append(Wall(wall_x, wall_y))
    # added speed and level constants
    speed = 5
    level, counter = get_user_score(user_id)
    font = pygame.font.Font('freesansbold.ttf', 22)

    # disappear food
    DISAPPEAR_FOOD = pygame.USEREVENT + 1
    pygame.time.set_timer(DISAPPEAR_FOOD, 10000)
    saved = False
    while running:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == DISAPPEAR_FOOD:
                gen_food()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    if saved:
                        saved = False
                    else:
                        save_score(level, counter)
                        saved = True
                elif saved:
                    continue
                elif event.key == pygame.K_UP:
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, +1
                elif event.key == pygame.K_LEFT:
                    dx, dy = -1, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = +1, 0
        if not saved:
            snake.move(dx, dy)
        for ww in walls:
            if snake.check_collision(ww):
                SCREEN.fill(RED)
                font = pygame.font.Font('freesansbold.ttf', 55)
                text = font.render(f'Level: {level}, Score: {counter}', True, GREEN, ORANGE)
                SCREEN.blit(text, (WIDTH // BLOCK_SIZE / 2, HEIGHT // BLOCK_SIZE / 2))

                pygame.display.update()

                time.sleep(2)
                pygame.quit()
                sys.exit()

        if snake.check_collision(food):
            for _ in range(food.weight):
                snake.points.append(Point(food.x, food.y))
                counter += 1
                if counter // LEVEL_CONSTANT > level - 1:
                    level += 1
                    # increase speed of snake by 50%
                    speed *= 1.5

            gen_food()

        # added level
        text = font.render(f'Level: {level}, Score: {counter}', True, GREEN, ORANGE)
        SCREEN.blit(text, (0, 0))

        for ww in walls:
            ww.update()
        food.update()
        snake.update()
        draw_grid()

        pygame.display.flip()
        clock.tick(speed)

    save_score(username, level, counter)


def get_by_username(username):
    sql = f"SELECT * FROM users where username = '{username}';"
    conn = None
    res = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # get all the data
        cur.execute(sql)
        res = cur.fetchall()
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return res


def insert_username(username):
    sql = """INSERT INTO users (username)
             VALUES(%s) RETURNING id;"""
    conn = None
    id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (username,))
        # get the generated id back
        id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id


def insert_score(user_id, level, counter):
    sql = """INSERT INTO user_score (user_id, current_level, score)
             VALUES(%s, %s, %s) RETURNING id;"""
    conn = None
    id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (user_id, level, counter,))
        # get the generated id back
        id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id


def get_user_score(user_id):
    sql = f"SELECT * FROM user_score where user_id = {user_id};"
    conn = None
    res = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # get all the data
        cur.execute(sql)
        res = cur.fetchall()
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    if res:
        return res[-1][1], res[-1][2]
    return 1, 0


def save_score(level, counter):
    sav_id = insert_score(user_id, level, counter)
    print(f"saved!: {sav_id}")


def login():
    global username
    global user_id
    while not username:
        username = input("please enter username:\n")

    qq = get_by_username(username)
    print(qq)
    if len(qq):
        user_id = qq[0][0]
    else:
        user_id = insert_username(username)


if __name__ == '__main__':
    login()
    main()
