import pygame
import sys

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


def main():
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    clock = pygame.time.Clock()

    character = Character(10)
    character.set_appearance((255, 0, 0))  # Set color to red
    character.set_position(5, 5)

    # Dictionary to keep track of key states
    keys = {pygame.K_UP: False, pygame.K_DOWN: False, pygame.K_LEFT: False, pygame.K_RIGHT: False}

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key in keys:
                    keys[event.key] = True

            if event.type == pygame.KEYUP:
                if event.key in keys:
                    keys[event.key] = False

        dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])  # Calculate x movement
        dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP])  # Calculate y movement
        character.move(dx, dy)

        screen.fill((0, 0, 0))  # Fill screen with black
        character.draw(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
