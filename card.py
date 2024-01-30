class Card:
    def __init__(self, image):
        self.type = -1
        self.show = False
        self.image = image
        self.hitBox = self.image.get_rect()
        self.x = -1
        self.y = -1
        self.hitBox = None
