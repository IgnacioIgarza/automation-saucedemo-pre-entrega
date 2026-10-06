import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_cart():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Espera implícita de hasta 10 segundos
    wait = WebDriverWait(driver, 10)  # Espera explícita de hasta 10 segundos
    
    try:
        # Abrir la página
        driver.get("https://www.saucedemo.com/")
        
        # Login exitoso
        usuario = wait.until(EC.presence_of_element_located((By.ID, "user-name"))) # seleccionamos esperando que sea visible
        password = driver.find_element(By.ID, "password")
        boton_login = wait.until(EC.element_to_be_clickable((By.ID, "login-button"))) # seleccionamos esperando que sea clickeable
        
        # Ingresar usuario y contraseña y hacer clic en el botón de inicio de sesión
        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")
        boton_login.click()
        
        # Agregar un producto al carrito
        boton_agregar = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
        boton_agregar.click()
        
        # Validar que el carrito tenga 1 producto
        carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert carrito.text == "1"
    
    except Exception as e:
        print(f"Error durante la prueba del carrito: {e}")
    
    finally:
        # Cerrar el navegador
        driver.quit()
    