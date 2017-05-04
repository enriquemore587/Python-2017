import matplotlib
def createDic(nom,edad,calif):
    dic={
        "nombre": nom,
        "edad" : edad,
        "calificacion" : calif
    }
    return dic

def graficaX2(ejex):
    ejey = []
    for i in ejex:
        ejey.append(i **2)
    dic2={
        "eje x": ejex,
        "eje y": ejey
    }
    return dic2

