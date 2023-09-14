def minutos_segundos(minutos):
    formulas =minutos * 60
    return f"El resultado es {formulas}"

def horas_minutos(horas):
    formula =  horas * 60
    return f"El resultado es {formula}"

if __name__ == '__main__':
  minutos = 2
  horas = 2
  print(minutos_segundos(minutos))
  print(horas_minutos(horas))