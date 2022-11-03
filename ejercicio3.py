from gettext import find


op=1
texto=""
cont=0
cv=0
while op!=11:
    print("===MENU===")
    print("[1] ingresar cadena:")
    print("[2] buscar cadena:")
    print("[3] reemplazar cadena:")
    print("[4] capitaliza el primer caracter e la cadena")
    print("[5] convierta la cadena en miniscula.")
    print("[6] convierta la cadena en mayuscula")
    print("[7] elimina los espacio en blanco de la cadena")
    print("[8] alinear la izquierda")
    print("[9] alinear a la derecha")
    print("[10] alinear al centro")
    print("[11] salir")
    op = int(input("opcion[1-11]:"))
    if op == 1:
        texto = input("ingresar frase:") 
    if op == 2:
        cad = input("buscar:")
        ubi= texto.find(cad)
        if ubi>=0:
            print("ingresar la palabra a buscar :",ubi)
        else:
            print("palabra no existe en la frase")
    if op==3:
        cad_ant =input("ingresar la palabra a buscar:")
        cad_nu =input("ingresar la palabra a reemplazar:")
        texto.replace(cad_ant, cad_nu)
        print(texto.replace(cad_ant, cad_nu))
    if op==4:
        print(texto.capitalize())
    if op==5:
        print(texto.lower())
    if op==6:
        print(texto.upper())
    if op==7:
        print(texto.strip())
    if op==8:
        print('{:^100}'.format(texto))
    if op==9:
        print('{:>100}'.format(texto))
    if op==10:
        print('{:100}'.format(texto))
        
        