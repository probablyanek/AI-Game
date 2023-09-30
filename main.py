import pygame
import sys
import random
import time, os

def nextCoord():
    # Generate a random coordinate
    x = random.randint(1, 50)
    y = random.randint(1, 50)
    return (x, y)

class Character:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.x = 0
        self.y = 0
        self.image = pygame.Surface((grid_size, grid_size))
        self.image.fill((255, 255, 255))  # Default color is white

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def set_appearance(self, color):
        self.image.fill(color)

    def draw(self, screen):
        screen.blit(self.image, (self.x * self.grid_size, self.y * self.grid_size))

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        
        # Check if the new position is within the grid
        if 1 <= new_x < 51 and 1 <= new_y < 51:  # Adjusted bounds
            self.x = new_x
            self.y = new_y

    def draw(self, screen):
        screen.blit(self.image, (self.x * self.grid_size, self.y * self.grid_size))
        
        # Draw a box around the allowed area
        pygame.draw.rect(screen, (0, 255, 0), (self.grid_size, self.grid_size, 50 * self.grid_size, 50 * self.grid_size), 1)

class MovingObject(Character):
    def update_position(self):
        self.set_position(*nextCoord())

def check_collision(red, blue):
    return red.x == blue.x and red.y == blue.y


def main():
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    game_over_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "game_over.png"))
    game_over_image = pygame.transform.scale(game_over_image, (700, 700))

    clock = pygame.time.Clock()

    character = Character(10)
    character.set_appearance((255, 0, 0))  # Set color to red
    character.set_position(5, 5)

    moving_object = MovingObject(10)
    moving_object.set_appearance((0, 0, 255))  # Set color to blue
    moving_object.set_position(25, 21)  # Centered at middle of screen

    last_blue_update_time = pygame.time.get_ticks()  # Get the current time

    while True:
        current_time = pygame.time.get_ticks()  # Get the current time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        dx = 0
        dy = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            dy = -1
        elif keys[pygame.K_DOWN]:
            dy = 1
        if keys[pygame.K_LEFT]:
            dx = -1
        elif keys[pygame.K_RIGHT]:
            dx = 1

        character.move(dx, dy)
        screen.fill((0, 0, 0))  # Fill screen with black
        character.draw(screen)

        moving_object.draw(screen)

        if current_time - last_blue_update_time >= 1000:  # Check if one second has passed
            moving_object.update_position()  # Update blue's position
            last_blue_update_time = current_time  # Update last update time

        pygame.draw.rect(screen, (0, 255, 0), (character.grid_size, character.grid_size, 50 * character.grid_size, 50 * character.grid_size), 1)

        if check_collision(character, moving_object):
            screen.fill((0, 0, 0))  # Fill screen with black
            screen.blit(game_over_image, (0, 0))
            pygame.display.flip()

            pygame.time.wait(30000)  # Wait for 3 seconds (3000 milliseconds)
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
