import pyautogui
import cv2
import numpy as np

pyautogui.sleep(3)

for i in range(999):  

    # Tira o print da tela inteira
    screenshot = pyautogui.screenshot()

    # Salva o print em um arquivo
    screenshot.save('screenshot.png')

    # Mostra uma mensagem de confirmação
    print("Print tirado com sucesso e salvo como 'screenshot.png'")

    # Carregar a imagem
    image_to_find = cv2.imread('C:\Projeto Autoclick TFT\img\Malza.png')

    # Converter a imagem para escala de cinza
    gray_image_to_find = cv2.cvtColor(image_to_find, cv2.COLOR_BGR2GRAY)

    # Tirar um screenshot da tela inteira
    screenshot = pyautogui.screenshot()

    # Converter a screenshot para um array numpy
    screenshot_np = np.array(screenshot)

    # Converter a screenshot para escala de cinza
    gray_screenshot = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)

    # Procurar a imagem na screenshot
    result = cv2.matchTemplate(gray_screenshot, gray_image_to_find, cv2.TM_CCOEFF_NORMED)

    # Definir um limite de confiança para detecção
    threshold = 0.8
    loc = np.where(result >= threshold)

    # Definir um limite de confiança para detecção
    threshold = 0.8
    loc = np.where(result >= threshold)

    # Encontrar as coordenadas das correspondências
    coordinates = []
    for pt in zip(*loc[::-1]):
        coordinates.append(pt)

    # Exibir as coordenadas encontradas
    if coordinates:
        print("Coordenadas das correspondências encontradas:")
        for coord in coordinates:
            print(f"X: {coord[0]}, Y: {coord[1]}")

        # Clicar no centro das coordenadas encontradas (opcional)
        for coord in coordinates:
            center_x = coord[0] + gray_image_to_find.shape[1] // 2
            center_y = coord[1] + gray_image_to_find.shape[0] // 2
            pyautogui.mouseDown(center_x, center_y, button='left')
            pyautogui.mouseUp(center_x, center_y, button='left')
    else:
        print("Nenhuma correspondência encontrada.")

    ############################################################################################################################################################################################

    # Tira o print da tela inteira
    screenshot = pyautogui.screenshot()

    # Salva o print em um arquivo
    screenshot.save('screenshot.png')

    # Mostra uma mensagem de confirmação
    print("Print tirado com sucesso e salvo como 'screenshot.png'")

    # Carregar a imagem
    image_to_find = cv2.imread('C:\Projeto Autoclick TFT\img\Cho.png')

    # Converter a imagem para escala de cinza
    gray_image_to_find = cv2.cvtColor(image_to_find, cv2.COLOR_BGR2GRAY)

    # Tirar um screenshot da tela inteira
    screenshot = pyautogui.screenshot()

    # Converter a screenshot para um array numpy
    screenshot_np = np.array(screenshot)

    # Converter a screenshot para escala de cinza
    gray_screenshot = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)

    # Procurar a imagem na screenshot
    result = cv2.matchTemplate(gray_screenshot, gray_image_to_find, cv2.TM_CCOEFF_NORMED)

    # Definir um limite de confiança para detecção
    threshold = 0.8
    loc = np.where(result >= threshold)

    # Definir um limite de confiança para detecção
    threshold = 0.8
    loc = np.where(result >= threshold)

    # Encontrar as coordenadas das correspondências
    coordinates = []
    for pt in zip(*loc[::-1]):
        coordinates.append(pt)

    # Exibir as coordenadas encontradas
    if coordinates:
        print("Coordenadas das correspondências encontradas:")
        for coord in coordinates:
            print(f"X: {coord[0]}, Y: {coord[1]}")

        # Clicar no centro das coordenadas encontradas (opcional)
        for coord in coordinates:
            center_x = coord[0] + gray_image_to_find.shape[1] // 2
            center_y = coord[1] + gray_image_to_find.shape[0] // 2
            pyautogui.mouseDown(center_x, center_y, button='left')
            pyautogui.mouseUp(center_x, center_y, button='left')
    else:
        print("Nenhuma correspondência encontrada.")

    ############################################################################################################################################################################################

     # Tira o print da tela inteira
    screenshot = pyautogui.screenshot()

    # Salva o print em um arquivo
    screenshot.save('screenshot.png')

    # Mostra uma mensagem de confirmação
    print("Print tirado com sucesso e salvo como 'screenshot.png'")

    # Carregar a imagem
    image_to_find = cv2.imread('C:\Projeto Autoclick TFT\img\Kassa.png')

    # Converter a imagem para escala de cinza
    gray_image_to_find = cv2.cvtColor(image_to_find, cv2.COLOR_BGR2GRAY)

    # Tirar um screenshot da tela inteira
    screenshot = pyautogui.screenshot()

    # Converter a screenshot para um array numpy
    screenshot_np = np.array(screenshot)

    # Converter a screenshot para escala de cinza
    gray_screenshot = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)

    # Procurar a imagem na screenshot
    result = cv2.matchTemplate(gray_screenshot, gray_image_to_find, cv2.TM_CCOEFF_NORMED)

    # Definir um limite de confiança para detecção
    threshold = 0.8
    loc = np.where(result >= threshold)

    # Definir um limite de confiança para detecção
    threshold = 0.8
    loc = np.where(result >= threshold)

    # Encontrar as coordenadas das correspondências
    coordinates = []
    for pt in zip(*loc[::-1]):
        coordinates.append(pt)

    # Exibir as coordenadas encontradas
    if coordinates:
        print("Coordenadas das correspondências encontradas:")
        for coord in coordinates:
            print(f"X: {coord[0]}, Y: {coord[1]}")

        # Clicar no centro das coordenadas encontradas (opcional)
        for coord in coordinates:
            center_x = coord[0] + gray_image_to_find.shape[1] // 2
            center_y = coord[1] + gray_image_to_find.shape[0] // 2
            pyautogui.mouseDown(center_x, center_y, button='left')
            pyautogui.mouseUp(center_x, center_y, button='left')
    else:
        print("Nenhuma correspondência encontrada.")

    ############################################################################################################################################################################################

    # Tira o print da tela inteira
    screenshot = pyautogui.screenshot()

    # Salva o print em um arquivo
    screenshot.save('screenshot.png')

    # Mostra uma mensagem de confirmação
    print("Print tirado com sucesso e salvo como 'screenshot.png'")

    # Carregar a imagem
    image_to_find = cv2.imread('C:\Projeto Autoclick TFT\img\Rek.png')

    # Converter a imagem para escala de cinza
    gray_image_to_find = cv2.cvtColor(image_to_find, cv2.COLOR_BGR2GRAY)

    # Tirar um screenshot da tela inteira
    screenshot = pyautogui.screenshot()

    # Converter a screenshot para um array numpy
    screenshot_np = np.array(screenshot)

    # Converter a screenshot para escala de cinza
    gray_screenshot = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)

    # Procurar a imagem na screenshot
    result = cv2.matchTemplate(gray_screenshot, gray_image_to_find, cv2.TM_CCOEFF_NORMED)

    # Definir um limite de confiança para detecção
    threshold = 0.8
    loc = np.where(result >= threshold)

    # Definir um limite de confiança para detecção
    threshold = 0.8
    loc = np.where(result >= threshold)

    # Encontrar as coordenadas das correspondências
    coordinates = []
    for pt in zip(*loc[::-1]):
        coordinates.append(pt)

    # Exibir as coordenadas encontradas
    if coordinates:
        print("Coordenadas das correspondências encontradas:")
        for coord in coordinates:
            print(f"X: {coord[0]}, Y: {coord[1]}")

        # Clicar no centro das coordenadas encontradas (opcional)
        for coord in coordinates:
            center_x = coord[0] + gray_image_to_find.shape[1] // 2
            center_y = coord[1] + gray_image_to_find.shape[0] // 2
            pyautogui.mouseDown(center_x, center_y, button='left')
            pyautogui.mouseUp(center_x, center_y, button='left')
    else:
        print("Nenhuma correspondência encontrada.")

    ############################################################################################################################################################################################

     # Tira o print da tela inteira
    screenshot = pyautogui.screenshot()

    # Salva o print em um arquivo
    screenshot.save('screenshot.png')

    # Mostra uma mensagem de confirmação
    print("Print tirado com sucesso e salvo como 'screenshot.png'")

    # Carregar a imagem
    image_to_find = cv2.imread('C:\Projeto Autoclick TFT\img\Velk.png')

    # Converter a imagem para escala de cinza
    gray_image_to_find = cv2.cvtColor(image_to_find, cv2.COLOR_BGR2GRAY)

    # Tirar um screenshot da tela inteira
    screenshot = pyautogui.screenshot()

    # Converter a screenshot para um array numpy
    screenshot_np = np.array(screenshot)

    # Converter a screenshot para escala de cinza
    gray_screenshot = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)

    # Procurar a imagem na screenshot
    result = cv2.matchTemplate(gray_screenshot, gray_image_to_find, cv2.TM_CCOEFF_NORMED)

    # Definir um limite de confiança para detecção
    threshold = 0.8
    loc = np.where(result >= threshold)

    # Definir um limite de confiança para detecção
    threshold = 0.8
    loc = np.where(result >= threshold)

    # Encontrar as coordenadas das correspondências
    coordinates = []
    for pt in zip(*loc[::-1]):
        coordinates.append(pt)

    # Exibir as coordenadas encontradas
    if coordinates:
        print("Coordenadas das correspondências encontradas:")
        for coord in coordinates:
            print(f"X: {coord[0]}, Y: {coord[1]}")

        # Clicar no centro das coordenadas encontradas (opcional)
        for coord in coordinates:
            center_x = coord[0] + gray_image_to_find.shape[1] // 2
            center_y = coord[1] + gray_image_to_find.shape[0] // 2
            pyautogui.mouseDown(center_x, center_y, button='left')
            pyautogui.mouseUp(center_x, center_y, button='left')
    else:
        print("Nenhuma correspondência encontrada.")

    ############################################################################################################################################################################################

    # Tira o print da tela inteira
    screenshot = pyautogui.screenshot()

    # Salva o print em um arquivo
    screenshot.save('screenshot.png')

    # Mostra uma mensagem de confirmação
    print("Print tirado com sucesso e salvo como 'screenshot.png'")

    # Carregar a imagem
    image_to_find = cv2.imread('C:\Projeto Autoclick TFT\img\kaysa.png')

    # Converter a imagem para escala de cinza
    gray_image_to_find = cv2.cvtColor(image_to_find, cv2.COLOR_BGR2GRAY)

    # Tirar um screenshot da tela inteira
    screenshot = pyautogui.screenshot()

    # Converter a screenshot para um array numpy
    screenshot_np = np.array(screenshot)

    # Converter a screenshot para escala de cinza
    gray_screenshot = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)

    # Procurar a imagem na screenshot
    result = cv2.matchTemplate(gray_screenshot, gray_image_to_find, cv2.TM_CCOEFF_NORMED)

    # Definir um limite de confiança para detecção
    threshold = 0.8
    loc = np.where(result >= threshold)

    # Definir um limite de confiança para detecção
    threshold = 0.8
    loc = np.where(result >= threshold)

    # Encontrar as coordenadas das correspondências
    coordinates = []
    for pt in zip(*loc[::-1]):
        coordinates.append(pt)

    # Exibir as coordenadas encontradas
    if coordinates:
        print("Coordenadas das correspondências encontradas:")
        for coord in coordinates:
            print(f"X: {coord[0]}, Y: {coord[1]}")

        # Clicar no centro das coordenadas encontradas (opcional)
        for coord in coordinates:
            center_x = coord[0] + gray_image_to_find.shape[1] // 2
            center_y = coord[1] + gray_image_to_find.shape[0] // 2
            pyautogui.mouseDown(center_x, center_y, button='left')
            pyautogui.mouseUp(center_x, center_y, button='left')
    else:
        print("Nenhuma correspondência encontrada.")

    ############################################################################################################################################################################################

     # Tira o print da tela inteira
    screenshot = pyautogui.screenshot()

    # Salva o print em um arquivo
    screenshot.save('screenshot.png')

    # Mostra uma mensagem de confirmação
    print("Print tirado com sucesso e salvo como 'screenshot.png'")

    # Carregar a imagem
    image_to_find = cv2.imread('C:\Projeto Autoclick TFT\img\Bel.png')

    # Converter a imagem para escala de cinza
    gray_image_to_find = cv2.cvtColor(image_to_find, cv2.COLOR_BGR2GRAY)

    # Tirar um screenshot da tela inteira
    screenshot = pyautogui.screenshot()

    # Converter a screenshot para um array numpy
    screenshot_np = np.array(screenshot)

    # Converter a screenshot para escala de cinza
    gray_screenshot = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)

    # Procurar a imagem na screenshot
    result = cv2.matchTemplate(gray_screenshot, gray_image_to_find, cv2.TM_CCOEFF_NORMED)

    # Definir um limite de confiança para detecção
    threshold = 0.8
    loc = np.where(result >= threshold)

    # Definir um limite de confiança para detecção
    threshold = 0.8
    loc = np.where(result >= threshold)

    # Encontrar as coordenadas das correspondências
    coordinates = []
    for pt in zip(*loc[::-1]):
        coordinates.append(pt)

    # Exibir as coordenadas encontradas
    if coordinates:
        print("Coordenadas das correspondências encontradas:")
        for coord in coordinates:
            print(f"X: {coord[0]}, Y: {coord[1]}")

        # Clicar no centro das coordenadas encontradas (opcional)
        for coord in coordinates:
            center_x = coord[0] + gray_image_to_find.shape[1] // 2
            center_y = coord[1] + gray_image_to_find.shape[0] // 2
            pyautogui.mouseDown(center_x, center_y, button='left')
            pyautogui.mouseUp(center_x, center_y, button='left')
    else:
        print("Nenhuma correspondência encontrada.")