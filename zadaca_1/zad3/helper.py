import numpy as np

def printHoursArms():
	center = np.array([256, 127])
	r = 50

	angles = np.array([(2*np.pi*(i/720) - np.pi/2) for i in range(720)])

	discretizedCircle = np.zeros((720,2))

	for i, angle in enumerate(angles):
		x = int(round(center[0] + r*np.cos(angle)))
		y = int(round(center[1] + r*np.sin(angle)))
		print("let hoursPositionsX[" + str(i) + "] = "+ str(x) + ";")
		print("let hoursPositionsY[" + str(i) + "] = "+ str(y) + ";")

def printMinutesArms():
	center = np.array([256, 127])
	r = 75

	angles = np.array([(2*np.pi*(i/60) - np.pi/2) for i in range(60)])

	discretizedCircle = np.zeros((60,2))

	for i, angle in enumerate(angles):
		x = int(round(center[0] + r*np.cos(angle)))
		y = int(round(center[1] + r*np.sin(angle)))
		print("let minutesPositionsX[" + str(i) + "] = "+ str(x) + ";")
		print("let minutesPositionsY[" + str(i) + "] = "+ str(y) + ";")


if __name__ == '__main__':
	#printHoursArms()
	printMinutesArms()