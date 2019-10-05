class Navegador:
    
    def __init__(self):
        self.actual_url = None
        # Agregar atributos necesarios
        self.url_abajo = []
        self.url_arriba = []
    
    def go_to_url(self, url):
        print("Cargando URL:")
        if self.actual_url is not None:
            self.url_abajo.append(self.actual_url)
            self.url_arriba = []
        self.actual_url = url
        # Realizar acciones necesarias aquí
        # Nota: en un navegador web, si volviste atrás y luego entras
        # a otra página web, ya no puedes volver adelante
    
    def go_back(self):
        # Realizar acciones necesarias aquí
        self.url_arriba.append(self.actual_url)
        self.actual_url = self.url_abajo.pop()
        
    
    def go_forward(self):
        # Realizar acciones necesarias aquí
        self.url_abajo.append(self.actual_url)
        self.actual_url = self.url_arriba.pop()
    
    def __str__(self):
        return "Te encuentras en {}".format(self.actual_url)


if __name__ == "__main__":
    browser = Navegador()
    browser.go_to_url("https://intrawww.ing.puc.cl/")
    print(browser)
    browser.go_to_url("https://mail.google.com/")
    print(browser)
    browser.go_to_url("https://web.telegram.org/")
    print(browser)
    browser.go_back()
    print(browser)
    browser.go_back()
    print(browser)
    browser.go_forward()
    print(browser)
    browser.go_to_url("https://intrawww.ing.puc.cl/")
    print(browser)
    