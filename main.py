import pygame
from logger import log_state
from constants import *
def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	log_state()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return
	screen.fill("black")
	pygame.display.flip()
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print("Screen width: 1280")
	print("Screen height: 720")

if __name__ == "__main__":
    main()
