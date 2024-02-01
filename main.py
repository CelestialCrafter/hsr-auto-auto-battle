import numpy as np, pyautogui, cv2, time, sys

def mse(imageA, imageB):
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])

	return err

def execute(screenshot, name, threshold):
	original = cv2.imread(f'data/{name}.png')
	mask = cv2.imread(f'data/{name}_mask.png', 0)
	error = mse(cv2.bitwise_and(original, original, mask=mask), cv2.bitwise_and(screenshot, screenshot, mask=mask))
	if len(sys.argv) > 1 and sys.argv[1] == 'debug':
		if len(sys.argv) > 2 and sys.argv[2] == name or sys.argv[2] == 'all':
			print(f'{name} - {error}')
	return error < threshold

while True:
	screenshot = pyautogui.screenshot()
	screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

	if execute(screenshot,'finish', 500):
		pyautogui.click(x=1180, y=950)

	elif execute(screenshot, 'resin', 100):
		pyautogui.click(x=1180, y=735)

	elif execute(screenshot, 'resin2', 100):
		pyautogui.click(x=1400, y=690)
		time.sleep(1)
		pyautogui.click(x=1180, y=800)
	elif execute(screenshot, 'resin3', 100):
		pyautogui.click(x=950, y=950)

	time.sleep(1 / 15)