
class Cursor:
    def __init(self):
        pass
    def handle_mouse_event(self, type, pos):
        if type == pg.MOUSEMOTION:
            self.handle_mouse_move(pos)
        elif type == pg.MOUSEBUTTONDOWN:
            self.handle_mouse_down(pos)
        elif type == pg.MOUSEBUTTONUP:
            self.handle_mouse_up(pos)


    def handle_mouse_move(self, pos):
        if self.bounds.collidepoint(pos):
            if self.state != 'pressed':
                self.state = 'hover'
        else:
            self.state = 'normal'


    def handle_mouse_down(self, pos):
        if self.bounds.collidepoint(pos):
            self.state = 'pressed'


    def handle_mouse_up(self, pos):
        if self.state == 'pressed':
            self.on_click(self)
            self.state = 'hover'
    def on_clicl(self):
        pass