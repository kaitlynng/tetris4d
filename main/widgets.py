class Button:
    def __init__(self, button_text, button_coor, button_dim):
        self.coor = button_coor
        self.dim = button_dim
        self.fill_color = 0
        self.border_color = 255
        self.label = button_text
        self.text_color = 200
        self.text_size = button_dim[1]/2
    
    def display(self):
        fill(self.fill_color)
        stroke(self.border_color)
        pushMatrix()
        translate(self.coor[0]-self.dim[0]/2, self.coor[1]-self.dim[1]/2, self.coor[2])
        rect(0,0,self.dim[0], self.dim[1])
        popMatrix()
        textAlign(CENTER, CENTER)
        textMode(SCREEN)
        textSize(self.text_size)
        fill(self.text_color)
        text(self.label, self.coor[0], self.coor[1], self.coor[2])

class Options:
    def __init__(self, list_items, list_coor, list_dim, select):
        self.items = list_items
        self.coor = list_coor
        self.dim = list_dim
        self.select = select
        self.text_padding = 20
        self.text_height = (self.dim[1]+self.text_padding)/len(self.items)-self.text_padding
        self.text_size = self.text_height/2
        self.text_color = 255
    
    def display(self):
        pushMatrix()
        translate(*self.coor)
        textMode(SCREEN)
        textAlign(LEFT, CENTER)
        textSize(self.text_size)
        for i in range(len(self.items)):
            text(self.items[i], -self.dim[0]/2+self.dim[0]/5*2, -self.dim[1]/2 + (self.text_height+self.text_padding)*i + self.text_height/2, 0)
        text('>', -self.dim[0]/2, -self.dim[1]/2 + (self.text_height+self.text_padding)*self.select + self.text_height/2, 0)
        
        popMatrix()
        
class Controls():
    def __init__(self, disp_coor, disp_dim):
        self.coor = disp_coor
        self.dim = disp_dim
        self.cell_num = [4, 6]
        self.cell_dim = [disp_dim[0]/self.cell_num[0], disp_dim[1]/self.cell_num[1]]
        self.cell_color = 0
        self.border_color = 255
        self.text_size = self.cell_dim[1]/3
        self.text_color = 255
        self.headings = ['Movement', 'Rotation']
        self.data = [['Keys', 'Axis', 'Keys', 'Rotation', 'Keys', 'Rotation'],
                     ['W, S', 'Z-axis', 'R, F', 'X-U plane', 'T, G', 'Y-U plane'],
                     ['Q, E', 'Y-axis', 'Y, H', 'Z-U plane', 'U, J', 'X-Z plane'],
                     ['A, D', 'X-axis', 'I, K', 'X-Y plane', 'O, L', 'Y-Z plane']]
        
    def display(self):
        textSize(self.text_size)
        textMode(SCREEN)
        textAlign(CENTER, CENTER)
        pushMatrix()
        translate(*self.coor)
        #display headings
        self.displayCell(self.headings[0], [0, 0], [2,1])
        self.displayCell(self.headings[1], [2, 0], [4,1])
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                self.displayCell(self.data[i][j], [j, i+1], [1,1])
        
        popMatrix()
    
    def displayCell(self, label, cell_index, cell_span):
        pushMatrix()
        translate(-self.dim[0]/2+cell_index[0]*self.cell_dim[0], -self.dim[1]/2+cell_index[1]*self.cell_dim[1], 0)
        fill(self.cell_color)
        stroke(self.border_color)
        rect(0, 0, self.cell_dim[0]*cell_span[0], self.cell_dim[1]*cell_span[1])
        fill(self.text_color)
        text(label, self.cell_dim[0]/2*cell_span[0], self.cell_dim[1]/2*cell_span[1], 0)
        popMatrix()
