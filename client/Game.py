from client.GameClient import GameClient
from classes.interface.menu import *


def run(client):
    while client.play:
        client.sits([[], 1])
        client.event_handling()
        data = client.rifs()
        if data:
            for obj in data[0]:
                if obj['act_id'] == 0:
                    client.create_object(obj)

                if obj['act_id'] == 1:
                    try:
                        client.move_object(obj)
                    except(KeyError):
                        client.create_object(obj)

        client.update_display()
        client.clock.tick(client.fps)


def main():
    client = GameClient((600, 480), 60, "norm")
    client.connect_to_server('localhost', 9090)
    men = build_stock_interface(4, client.resolution)
    for b in men:
        client.load_button(b)
    run(client)


if __name__ == '__main__':
    main()
