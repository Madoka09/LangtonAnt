import turtle

class Map():
    def __init__(self, map_size, fastmode=False):
        self.screen = turtle.Screen()
        self.screen.bgcolor('white')
        self.screen.setup(width=map_size[0], height=map_size[1])
        self.fastmode = fastmode
        if self.fastmode:
            self.screen.tracer(0,0)

class Ant():
    def __init__(self, ant_speed=0, move_steps=10, max_iterations=11000):
        self.ant = turtle.Turtle()
        #self.ant.setpos(init_cords[0], init_cords[1])
        self.ant.shape('square')
        self.ant.turtlesize(0.5)
        self.ant.speed(ant_speed)
        self.ant.hideturtle()

        #Parametros para el apuntador
        self.ant_pointer = turtle.Turtle()
        self.ant_pointer.shape('square')
        self.ant_pointer.turtlesize(0.5)
        self.ant_pointer.speed(ant_speed)
        self.ant_pointer.fillcolor('red')
        self.ant_pointer.color('red')

        #Parametros adicionales de la hormiga
        self.info = {}
        self.position = self.get_ant_pos(self.ant)
        self.steps = 0
        self.move_steps = move_steps
        self.max_iterations = int(max_iterations)

    def white_square(self):
        #Declarar el color de hormiga como negro
        self.ant.fillcolor('black')

        #Rotar la hormiga 90 grados en sentido horario
        self.ant.right(90)
        self.ant_pointer.right(90)

        #Estampar una copia de la hormiga
        self.ant.stamp()

        #Guardar en ant_info la coordenada de la hormiga y su color
        self.save_ant_pos(self.ant, 'black')


    def black_square(self):
        #Declarar el color de hormiga como blanco
        self.ant.fillcolor('white')

        #Rotar la hormiga 90 grados en sentido anti-horario
        self.ant.left(90)
        self.ant_pointer.left(90)

        #Estampar una copia de la hormiga
        self.ant.stamp()

        #Guardar en ant_info, la estampa y las coordenadas de la hormiga
        self.save_ant_pos(self.ant, 'white')


    def get_ant_pos(self, ant):
        return (round(ant.xcor()), round(ant.ycor()))
    
    def save_ant_pos(self, ant, color):
        self.info[self.get_ant_pos(ant)] = color

        #mover la tortuga
        self.ant.forward(self.move_steps)
        self.ant_pointer.forward(self.move_steps)

        #Guardar el valor de la posicion de la hormiga
        self.position = self.get_ant_pos(self.ant)

        #Incrementar el contador de pasos
        self.steps += 1

map = Map((1280, 720), fastmode=True)
ant = Ant(ant_speed=0, max_iterations=11000)

#Imprimir el numero de paso de la hormiga en la pantalla

while True:

    if ant.position not in ant.info or ant.info[ant.position] == 'white':
        ant.white_square()
    elif ant.info[ant.position] == 'black':
        ant.black_square()

    if map.fastmode:
        map.screen.update()

    if ant.max_iterations <= ant.steps:
        turtle.done()
        
    print(f'NUMERO DE PASOS: {ant.steps}')
