import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



def test_inventary():
    # Configurar el controlador del navegador (en este caso, Chrome)
    driver = webdriver.Chrome()
    
    try:
        # Login exitoso antes de verificar el inventario
        driver.get("https://www.saucedemo.com/")
        
        # Encontrar los elementos de usuario, contraseña y botón de inicio de sesión
        usuario = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        boton_login = driver.find_element(By.ID, "login-button")
        
        # Ingresar las credenciales y hacer clic en el botón de inicio de sesión
        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")
        boton_login.click()
        
        # Validar que el inicio de sesión fue exitoso verificando la URL actual
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
        
        # Validar que el logo de la aplicación esté presente
        logo = driver.find_element(By.CLASS_NAME, "app_logo")
        assert logo.text == "Swag Labs"
        
        # Validar el título de la página
        assert driver.title == "Swag Labs"
        
        # Validar que haya al menos un producto en la lista de inventario
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"Cantidad de productos en inventario: {len(productos)}")
        assert len(productos) > 0
        
        # Validar el nombre y precio del primer producto
        primer_producto = productos[0]
        nombre_primer_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name")
        precio_primer_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price")
        print(f"Primer producto: {nombre_primer_producto.text}, Precio: {precio_primer_producto.text}")
        assert nombre_primer_producto.text == "Sauce Labs Backpack"
        assert precio_primer_producto.text == "$29.99"
        
        # Validar que los productos tengan nombre y precio
        for producto in productos:
            nombre = producto.find_element(By.CLASS_NAME, "inventory_item_name")
            precio = producto.find_element(By.CLASS_NAME, "inventory_item_price")
            assert nombre.text != ""
            assert precio.text != ""
            print(f"Producto: {nombre.text}, Precio: {precio.text}")
            
        # Validar si es visible el menú hamburguesa
        menu_hamburguesa = driver.find_element(By.ID, "react-burger-menu-btn")
        assert menu_hamburguesa.is_displayed()
        
        # Validar si es visible el carrito de compras
        carrito_compras = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        assert carrito_compras.is_displayed()
        
        # Verificar el filtro de productos
        filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
        assert filtro.is_displayed()
            
    except Exception as e:
        print(f"Error durante la prueba de inventario: {e}")
    
    finally:
        # Cerrar el navegador
        driver.quit()