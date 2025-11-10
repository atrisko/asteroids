import pygame
import constants
import player
import asteroid 
import asteroidfields
import sysd
from logger import log_state, log_event



def game_loop():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    player.Player.containers = (updatable, drawable)
    asteroidfields.AsteroidField.containers = (updatable,)
    my_asteroid_field = asteroidfields.AsteroidField()
    my_player = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        log_state()
        for sprite in drawable:
            sprite.draw(screen)
        for sprite in asteroids:
            if sprite.collision_with(my_player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit() 
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        
     




def main():
    print("Starting Asteroids! with pygame version: ",pygame.version.ver)
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    
    


if __name__ == "__main__":
    main()
    game_loop()

