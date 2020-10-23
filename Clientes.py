class Clients():
def validarDNI(dni):
    try:
        dig_ext='XYZ'
        reemp_dig_ext = {'X': '0', 'Y': '1, 'Z': '2'}
        numeros = '1234567890'
        dni = dni.upper()
        if len(dni)==9:
            dig_control= dni[8]
            dni = [0:8]
            if dni[0] in dig_ext:
                dni= dni.replace(dni[0], reemp_dig_ext[dni[0]])
            return len(dni == len(ln for n in dni if n in numeros])) and tabla[int(dni) % 23] == dig_control
        return false
    except:
    print('Error en el módulo de validación del DNI')
    return None