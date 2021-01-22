
dimInterno = float(input("Digite o Diametro Interno: "))
dimexterno = float(input("Digite o Diametro Externo: "))
largura = float(input("Digite a Largura: "))

tempinterno = float(dimInterno*dimInterno)
tempexterno = float(dimexterno*dimexterno)
tempcalc = float(tempexterno-tempinterno) 

tempcalc1 = float(tempcalc * 0.00000785 * 3.1437708364187786)/4

peso = float(tempcalc1 * largura)

print("A densidade do rolo é:",float(round(tempcalc1,2)))
print("O peso do rolo é de:",int(peso),"Kg")
