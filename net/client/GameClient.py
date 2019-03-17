import pygame

from net.client.Client import Client


def run(client):
    client.connect_to_server('localhost', 5050)
    clock = pygame.time.Clock()
    while client.play:
        client.receive()
        client.handler()
        client.update_display()
        client.send()
        clock.tick(60)


def main():
    client = Client((1280, 720), 60, "norm")
    run(client)


if __name__ == '__main__':
    main()
