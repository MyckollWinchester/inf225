import requests
from bs4 import BeautifulSoup
import json
from concurrent.futures import ThreadPoolExecutor

class Producto:
    def __init__(self, nombre, precio, enlace, imagen):
        self.nombre = nombre
        self.precio = precio
        self.enlace = enlace
        self.imagen = imagen


productos: list[Producto] = []

def process_url(url):
    global productos
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
    product_name = soup.find("meta", {"property": "og:title"})["content"]
    if product_name.endswith(" | Jumbo.cl"):
        product_name = product_name[:-len(" | Jumbo.cl")]
    product_price = int(soup.find("meta", {"property": "product:price:amount"})["content"])
    product_image_url = soup.find("meta", {"property": "og:image"})["content"]
    productos.append(Producto(product_name, product_price, url, product_image_url))

def jumbo_search(query):
    global productos
    url = f"https://www.jumbo.cl/busqueda?ft={query}"
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
    json_scripts = soup.find_all("script", {"type": "application/ld+json"})
    urls: list[str] = []
    for script in json_scripts:
        try:
            json_data = json.loads(script.string)
            if "@type" in json_data and json_data["@type"] == "ItemList":
                urls = [item["url"] for item in json_data["itemListElement"]]
        except json.JSONDecodeError:
            pass
    if not urls: return None

    with ThreadPoolExecutor() as executor:
        executor.map(process_url, urls)
    productos_tmp = []
    for producto in productos:
        productos_tmp.append({
            "nombre": producto.nombre,
            "precio": producto.precio,
            "enlace": producto.enlace,
            "imagen": producto.imagen
        })
    productos = []
    return productos_tmp

if __name__ == "__main__":
    print("Buscando leche...")
    print(jumbo_search("leche"))
