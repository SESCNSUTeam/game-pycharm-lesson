import sys, pygame
import Object as obj
size = width, height = 1280, 920

speed = [1,1]
black = 0, 0, 0
screen = pygame.display.set_mode(size)
image = pygame.image.load("ball.png")
object = obj.Object(image, 30, 30, width, height)
timer = pygame.time.Clock()


def main():
    while True:
        update()
        render()
        timer.tick(frame_rate)

def render():
    screen.fill(black)
    object.render(screen)
    pygame.display.flip()

def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    object.update()


main()