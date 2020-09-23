# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 08:38:28 2020

@author: A.RAfi Muzakki
"""





#number 1
print('Enter your height.')
Feet=int(input('Feet:'))
Inches=int(input('Inches:'))
board=(Feet*30.48+Inches*2.54)*0.88
print('Suggested board length:',board,'cm')







#number2
mass=float
force=float
mass, force=eval(input('Enter the mass in kg and the force in N:'))
acceleration=force/mass
print('The acceleration:',acceleration)                 
                  



                       
                     
                       
#Number 3
print('A Shinigami [verb] my [adjective] [noun] out of the [noun] as if he were a vegetarian fishing a [noun] out of his salad. ')
verb=(input('Enter a verb:'))
adjective=(input('Enter an adjective:'))
noun1=(input('Enter a noun:'))
noun2=(input('Enter a noun:'))
noun3=(input('Enter noun:'))
print('')
print('A Shinigami',verb,'my',adjective,noun1,'out of the',noun2,'as if he were a vegetarian fishing a',noun3,'out of his salad.')
                       