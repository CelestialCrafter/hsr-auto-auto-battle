import numpy as np, pyautogui, cv2, time, fire

def mse(imageA, imageB):
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])

	return err

def execute(screenshot, name, threshold, debug=''):
	original = cv2.imread(f'data/{name}.png')
	mask = cv2.imread(f'data/{name}_mask.png', 0)
	error = mse(cv2.bitwise_and(original, original, mask=mask), cv2.bitwise_and(screenshot, screenshot, mask=mask))
	if debug == 'all' or debug == name:
		print(f'{name} - {error}')
	return error < threshold

def main_loop(trailblaze_power_refill=True, debug=''):
	while True:
		screenshot = pyautogui.screenshot()
		screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

		if execute(screenshot, 'finish', 500, debug=debug):
			pyautogui.click(x=1180, y=950)

		elif trailblaze_power_refill:
			if execute(screenshot, 'tb_power', 450, debug=debug):
				pyautogui.click(x=1180, y=735)

			elif execute(screenshot, 'tb_power2', 100, debug=debug):
				pyautogui.click(x=1400, y=690)
				time.sleep(1)
				pyautogui.click(x=1180, y=800)
			elif execute(screenshot, 'tb_power3', 100, debug=debug):
				pyautogui.click(x=950, y=950)

		time.sleep(1 / 15)

if __name__ == '__main__':
	fire.Fire(main_loop)