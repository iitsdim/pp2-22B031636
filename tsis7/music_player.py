import pygame
import os
from dotenv import load_dotenv

load_dotenv()
path = r'C:\Users\User\PycharmProjects\pp2-22B031636\tsis7\musics'

songs = os.listdir(path)
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
print(songs)

play = True
SONG_END = pygame.USEREVENT + 1

cursor = 0

pygame.mixer.music.load(f'{path}\\{songs[0]}')
pygame.mixer.music.play(0)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if play:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.play(0)
                play = not play
            if event.key == pygame.K_RIGHT:
                cursor = (cursor + 1) % len(songs)
                pygame.mixer.music.load(f'{path}\\{songs[cursor]}')
                pygame.mixer.music.play(0)
            if event.key == pygame.K_LEFT:
                cursor = (cursor - 1 + len(songs)) % len(songs)
                pygame.mixer.music.load(f'{path}\\{songs[cursor]}')
                pygame.mixer.music.play(0)
    if play and not pygame.mixer.music.get_busy():
        cursor = (cursor + 1) % len(songs)
        pygame.mixer.music.load(f'{path}\\{songs[cursor]}')
        pygame.mixer.music.play(0)
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont(None, 24)
    img = font.render(f'{"play" if play else "pause"}: {songs[cursor]}', True, pygame.color.THECOLORS['aliceblue'])
    screen.blit(img, (10, 50))

    pygame.display.flip()

pygame.mixer.music.stop()
