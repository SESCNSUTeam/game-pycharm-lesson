class Activity:
    def __init__(self, resolution, gsm):
        self.gsm = gsm
        self.resolution = resolution

    def update(self, dt):
        pass

    def update_display(self):
        pass

    def handler(self):
        pass

    def up_load(self, *args):
        pass

    def change_activity(self, activity):
        self.gsm.push(activity)
