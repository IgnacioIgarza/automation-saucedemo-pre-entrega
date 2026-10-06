import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_loginExitoso():
    # Configurar el controlador del navegador (en este caso, Chrome)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Espera implícita de hasta 10 segundos
    wait = WebDriverWait(driver, 10)  # Espera explícita de hasta 10 segundos
    
    try:
        # Abrir la página de inicio de sesión
        driver.get("https://www.saucedemo.com/")
        
        # Encontrar los elementos de usuario, contraseña y botón de inicio de sesión
        usuario = wait.until(EC.presence_of_element_located((By.ID, "user-name"))) #lo seleccionamos esperando que sea visible
        #usuario = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        boton_login = wait.until(EC.element_to_be_clickable((By.ID, "login-button"))) #lo seleccionamos esperando que sea clickeable
        #boton_login = driver.find_element(By.ID, "login-button")
        
        # Ingresar las credenciales y hacer clic en el botón de inicio de sesión
        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")
        boton_login.click()
        
        # Validar que el inicio de sesión fue exitoso verificando la URL actual
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
        
        # Validar que el logo de la aplicación esté presente (doble verificación)
        logo = driver.find_element(By.CLASS_NAME, "app_logo")
        assert logo.text == "Swag Labs"
        titulo = driver.find_element(By.CLASS_NAME, "title")
        assert titulo.text == "Products"
        
    except Exception as e:
        print(f"Error durante la prueba de inicio de sesión exitoso: {e}")
        
    finally:
        # Cerrar el navegador
        driver.quit()
    
def test_loginFallido():
    # Configurar el controlador del navegador (en este caso, Chrome)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Espera implícita de hasta 10 segundos
    
    try:
        # Abrir la página de inicio de sesión
        driver.get("https://www.saucedemo.com/")
        
        # Encontrar los elementos de usuario, contraseña y botón de inicio de sesión
        usuario = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        boton_login = driver.find_element(By.ID, "login-button")
        
        # Ingresar credenciales incorrectas y hacer clic en el botón de inicio de sesión
        usuario.send_keys("usuario_incorrecto")
        password.send_keys("contraseña_incorrecta")
        boton_login.click()
        
        # Validar que el inicio de sesión falló verificando la presencia del mensaje de error
        mensaje_error = driver.find_element(By.CLASS_NAME, "error-message-container")
        assert mensaje_error.is_displayed()
    
    except Exception as e:
        print(f"Error durante la prueba de inicio de sesión fallido: {e}")
        
    finally:
        # Cerrar el navegador
        driver.quit()

def test_loginVacio():
    # Configurar el controlador del navegador (en este caso, Chrome)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Espera implícita de hasta 10 segundos

    try:
        # Abrir la página de inicio de sesión
        driver.get("https://www.saucedemo.com/")
        
        # Encontrar los elementos de usuario, contraseña y botón de inicio de sesión
        usuario = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        boton_login = driver.find_element(By.ID, "login-button")
        
        # Dejar los campos vacíos y hacer clic en el botón de inicio de sesión
        usuario.send_keys("")
        password.send_keys("")
        boton_login.click()
        
        # Validar que el inicio de sesión falló verificando la presencia del mensaje de error
        mensaje_error = driver.find_element(By.CLASS_NAME, "error-message-container")
        assert mensaje_error.is_displayed()
    
    except Exception as e:
        print(f"Error durante la prueba de inicio de sesión vacío: {e}")
        
    finally:
        # Cerrar el navegador
        driver.quit()
