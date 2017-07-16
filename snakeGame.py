#snake Game!

import pygame, sys, random, time

check_errors = pygame.init()
if check_errors[1]> 0:
	print("(!) Had {0} initializing errors, exiting....".format(check_errors[1]))
	sys.exit(-1)
else:
	print("(+) Pygame initialized successfully.")

