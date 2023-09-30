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
        if 1 <= new_x < 9 and 1 <= new_y < 9:  # Adjusted bounds
            self.x = new_x
            self.y = new_y

def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    clock = pygame.time.Clock()

    character = Character(10)
    character.set_appearance((255, 0, 0))  # Set color to red
    character.set_position(5, 5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    character.move(0, -1)
                elif event.key == pygame.K_DOWN:
                    character.move(0, 1)
                elif event.key == pygame.K_LEFT:
                    character.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    character.move(1, 0)

        screen.fill((0, 0, 0))  # Fill screen with black
        character.draw(screen)
        pygame.draw.rect(screen, (0, 0, 255), (0, 0, 100, 100), 1)  # Draw perimeter wall
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
