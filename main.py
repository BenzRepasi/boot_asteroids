import pygame
import constants

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    pygame.display.set_mode()
    screen=pygame.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])

    while(42):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        pygame.display.flip()



if __name__ == "__main__":
    main()
