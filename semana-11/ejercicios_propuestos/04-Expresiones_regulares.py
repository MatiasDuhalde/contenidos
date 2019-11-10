import re

def traducir_pata(cancion):
    # Aqui deberás hacer los cambios correspondientes
    substitutions = {
        "BUM" : "O",
        "pata": "././",
        "tss" : "x/" ,
        ";-;" : "|"
    }
    for sub_ in substitutions:
        cancion = re.sub(sub_, substitutions[sub_] + " ", cancion)
    return cancion

print(traducir_pata("BUMpatapatapatatss;-;BUMBUMpatatsspatatss;-;BUMpataBUMpataBUM;-;BUMtsstssBUMpata"))