from gamePycharmLesson.classes import CommonGameObject

class squad(CommonGameObject):
    Id = 3                                               #class id

    def __init__(self, x, y, w, h, sq_id, monsterList):
        CommonGameObject.__init__(self, x, y, w, h)
        self.squad_Id = sq_id                           #constant id of squade(squad number)
        self.monster_list = monsterList                 #list of monsters in the squad
        self.senter_x = None                            #start squad senter x coordinate
        self.senter_y = None                            #start squad senter y coordinate

    def update(self):
        if self.monster_list.size == 0:                 #if there are no monsters in the squad - delete this squad
            self = None
        for i in range(len(self.monster_list)):         #updating all monsters in the squad
            self.monster_list[i].update

