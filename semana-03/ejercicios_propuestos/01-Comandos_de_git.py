class Repositorio:
    
    def __init__(self, archivos=[]):
        # Los archivos subidos al repositorio remoto (e.g. servidor github)
        self.archivos_remotos = archivos
        # Archivos a los que se les hizo un commit
        self.archivos_locales = set()
        #puedes agregar más atributos si lo estimas necesario ;)
        # Archivos a los que se les hizo un add
        self.staging = set()
        
    def git_add(self, archivos):
        #debes completar aquí
        if type(archivos) == str:
            archivos = [archivos]
        self.staging.update(archivos)
        
    def git_commit(self, comentario):
        print(comentario)
        #debes completar aquí
        self.archivos_locales.update(self.staging)
        self.staging.clear()
    
    def git_push(self):
        self.archivos_remotos.extend(self.archivos_locales)
        self.archivos_locales.clear()
        
    
if __name__ == "__main__":
    mi_repo = Repositorio(["main.py", "windows.py", "user.txt"])
    mi_repo.git_add('README.md')
    mi_repo.git_commit('Agregado el README :D')
    mi_repo.git_push()
    mi_repo.git_add(["data.json", "client.py", "user.txt"])
    mi_repo.git_commit("subiendo datos")
    mi_repo.git_push()
    