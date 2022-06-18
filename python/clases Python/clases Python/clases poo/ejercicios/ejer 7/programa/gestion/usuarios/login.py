min_Digitos = 4
max_Digitos = 8

def esEncargado(cargo):
    if cargo == "encargado": return True
    else: return False

def valdiarContraseña(contraseña):
    digitos_Contraseña = 0
    for _ in contraseña:
        digitos_Contraseña += 1
    
    if (min_Digitos < digitos_Contraseña < max_Digitos): return True
    else: return False
        