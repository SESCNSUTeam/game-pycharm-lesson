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
        clock.tick(120)


def main():
    server = Server('192.168.43.106', 25565)
    run(server)


if __name__ == '__main__':
    main()
