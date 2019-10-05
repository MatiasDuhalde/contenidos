class FullDocencia:
    def __init__(self, nombre, mensaje):
        self.nombre = nombre
        self.mensaje_de_apoyo = mensaje

    def asistir_a_catedra(self):  
        print('¡¡Voy a la cátedra!!')
    
    def mostrar_apoyo(self):
        print(f'Vamos, tú puedes, {self.mensaje_de_apoyo}')

class FullTarea:  # La condicion es que FullTarea nunca ejecutará su método
    def __init__(self, nombre, mensaje):
        self.nombre = nombre
    
    def ayudar_en_catedra(self):
        # ¿Y de donde sacará este atributo?
        print(f'{self.mensaje_de_apoyo}!!')

class HibridoTarea(FullTarea, FullDocencia):
    def __init__(self, nombre, mensaje):
        FullTarea.__init__(self, nombre, mensaje)
        FullDocencia.__init__(self,nombre, mensaje)

class HibridoDocencia(FullDocencia, FullTarea):
    def __init__(self, nombre, mensaje):
        FullDocencia.__init__(self,nombre, mensaje)
        FullTarea.__init__(self, nombre, mensaje)
        
# ¿Puedes identificar a estos ayudantes?
ay_1 = HibridoTarea('Antonio Aguilar', 'Ánimo que se puede')
ay_2 = HibridoDocencia('Jorge Negrete', 'Da lo mejor de ti') 
ay_3 = FullTarea('Miguel Aceves Mejía', '¡¡Siempre hay una segunda oportunidad!!')  
ay_4 = FullDocencia('Pedro Infante', 'Un tropezon no es caida') # Parcial

ay_2.asistir_a_catedra()
ay_1.asistir_a_catedra()

ay_2.mostrar_apoyo()
ay_1.mostrar_apoyo()
ay_4.mostrar_apoyo()

# Si lograste hacer funcionar el código, podrás haber notado que éste presenta 
# una restricción en particular para que funcione. 
# ¿Es correcta esta forma de modelar? ¿Es válida esa restricción al modelo? 
# ¿Se puede hacer de manera distinta?

# Funciona para este caso, pero tiene algunos errores. Por ejemplo, los objetos 
# de FullTarea no podrían ocupar el método ayudar_en_catedra, debido a que no 
# poseen el atributo mensaje_de_apoyo. Solo podrían usarlo instancias de clases 
# que hereden tanto de FullTarea como de FullDocencia
# Otra manera de hacer la herencia en el override de __init__ sería ocupar la 
# función super(). Esta es especialmente útil en estructuras de diamante.