import pygame
from net.server.Server import Server


def run(server):
    clock = pygame.time.Clock()
    server.server.start()

    while server.play:
        server.receive()
        server.handler()
        server.update(clock.get_time())
        server.send()
        clock.tick(240)


def main():
    server = Server('localhost', 5050)
    run(server)


if __name__ == '__main__':
    main()
