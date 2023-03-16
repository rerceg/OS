import numpy as np

def printClockArms(radius, nOfPoints, name):
	center = np.array([256, 127])

	angles = np.array([(2*np.pi*(i/nOfPoints) - np.pi/2) for i in range(nOfPoints)])

	discretizedCircle = np.zeros((nOfPoints,2))

	for i, angle in enumerate(angles):
		x = int(round(center[0] + radius*np.cos(angle)))
		y = int(round(center[1] + radius*np.sin(angle)))
		print("let " + name + "PositionsX[" + str(i) + "] = "+ str(x) + ";")
		print("let " + name + "PositionsY[" + str(i) + "] = "+ str(y) + ";")


if __name__ == '__main__':
	printClockArms(50, 720, "hours")
	printClockArms(75, 60, "minutes")