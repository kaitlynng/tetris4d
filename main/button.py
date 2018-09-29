class Button:
    def __init__(self, button_text, button_coor, button_dim):
        self.button_coor = button_coor
        self.button_dim = button_dim
        self.button_color = 0
        self.button_border_color = 255
        self.button_text = button_text
        self.button_text_color = 200
        self.text_size = button_dim[1]/2
    
    def display(self):
        fill(self.button_color)
        stroke(self.button_border_color)
        pushMatrix()
        translate(self.button_coor[0]-self.button_dim[0]/2, self.button_coor[1]-self.button_dim[1]/2, self.button_coor[2])
        rect(0,0,self.button_dim[0], self.button_dim[1])
        popMatrix()
        textAlign(CENTER, CENTER)
        textSize(self.text_size)
        fill(self.button_text_color)
        text(self.button_text, self.button_coor[0], self.button_coor[1], self.button_coor[2])
                
