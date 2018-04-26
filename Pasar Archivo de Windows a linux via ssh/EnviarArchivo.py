from subprocess import check_output
host= ""+str(raw_input("Introduzca direccion del servidor \n"))
user=str( raw_input("Introduzca usuario\n"))
passs= str(raw_input("Introduzca contrasenna usuario\n"))
origen=str( raw_input("Introduca archivo a enviar (ruta)\n"))
destino= str(raw_input("Introduzca ruta destino\n"))
comando="pscp -pw "+passs+" "+origen+" "+user+"@"+host+":"+destino
check_output(comando, shell=True).decode()
#pscp -pw password D:\test.txt user@192.168.33.10:/etc/var/test/test.txt
