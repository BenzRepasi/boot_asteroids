import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from weapon import Shot

def main():
    pygame.init()

    clock = pygame.time.Clock()
    delta_time = 0

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    #containers
    Player.containers = (updatable, drawable) # type: ignore
    Asteroid.containers = (asteroids, updatable, drawable) # type: ignore
    AsteroidField.containers = updatable # type: ignore
    Shot.containers = (shots, updatable, drawable) # type: ignore

    #object inits
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.display.set_mode()
    screen=pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])    



    while(42):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(delta_time)

        for ast in asteroids:
            if ast.collision(player):
                print("Game over!")
                return
            for bull in shots:
                if ast.collision(bull):
                    ast.split()
                    bull.kill()
        screen.fill(color="black")

        for x in drawable:
            x.draw(screen)

        pygame.display.flip()
        delta_time = clock.tick(60)/1000




if __name__ == "__main__":
    main()
