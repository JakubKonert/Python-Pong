class Text():
    def __init__(self,font):
        self.font = font

    def createText(self, text_to_write,color):
        return self.font.render(f"{text_to_write}",False,color)

    def putText(self,text_to_write,color,screen,x,y):
        screen.blit(self.createText(text_to_write,color),(x,y))
        