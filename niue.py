#!/usr/bin/env python

import rospy #importar ros para python
from sensor_msgs.msg import Joy # importar mensajes de ROS tipo String y tipo Int32
from geometry_msgs.msg import Twist # importar mensajes de ROS tipo geometry / Twist


class Template(object):
	def __init__(self, args):
		super(Template, self).__init__()
		self.args = args
		self.sub  = rospy.Subscriber('duckiebot/joy', Joy, self.callback)


	#def publicar(self):

	def callback(self,msg):
		msg.axes = list(msg.axes)
		if msg.buttons[1] == 1:
			msg.axes[0] = 0
			msg.axes[1] = 0
			print("CUAC")
		
		Y = msg.axes[0]
		X = msg.axes[1]
		print('Y[0,1].' ,mapeo(0, 1, Y))
		print('Y[-pi/2,pi/2]', mapeo(-3.14*0.5, 3.14*0.5, Y))
		print('Y[-10,10]', mapeo(-10, 10, Y))
		print('X[0,1].' ,mapeo(0, 1, X))
		print('X[-pi/2,pi/2]', mapeo(-3.14*0.5, 3.14*0.5, X))
		print('X[-10,10]', mapeo(-10, 10, X))
		
	
def mapeo(inf, sup, val):
	delta = (abs(sup) - abs(inf))*0.5
	escala = sup - delta
	return 1.0*escala*val + 1.0*delta
	
def main():
	rospy.init_node('test') #creacion y registro del nodo!

	obj = Template('args') # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()

