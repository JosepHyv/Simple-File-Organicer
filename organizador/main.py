import os 
import shutil
import pathlib


nombre = "ArchivosOrganizados/"

def getHome():
	return str(os.path.expanduser("~")) + "/"

def updateContenedor(padre, lista, destino):
	directions = {}
	usuario = getHome()
	dircompleta = usuario + destino + padre + "/"
	fileList = []
	if os.path.isdir(dircompleta):
		fileList = os.listdir(dircompleta)
	else:
		print("El directorio no existe ", usuario + nombre, " Creando ")
		os.mkdir(dircompleta)
	for extension in lista:
		if not os.path.isdir(dircompleta + extension[1::]):
			os.mkdir(dircompleta + extension[1::] )
		fileList.append(extension[1::])
	print("DEBUG\n", *fileList, sep=" <-> ")
	for dirs in fileList:
		directions[dirs] = dircompleta + dirs +  "/"
	return directions

def lastname(line):
	aux = ""
	line = line[::-1]
	for char in line:
		if char != '/':
			aux += char
		else: break
	aux = aux[::-1]
	#print(aux)
	return aux

def getExtension(file):
	if ".tar.gz" in file:
		return str(".tar gz")	
	return str(pathlib.Path(file).suffix)

def move(dirArchivo, dirDestino):
	if os.path.isfile(dirArchivo) and os.path.isdir(dirDestino):
		print("Moviendo "  + lastname(dirArchivo) + " A " + dirDestino)
		shutil.move(dirArchivo, dirDestino)
	else:
		print("Hay un problema con las direcciones")
		exit()
	pass

def main():
	dirs = input()
	print(dirs, lastname(dirs))

	lista = os.listdir(dirs)
	extensiones = []
	archivos = []
	for files in lista:
		#print(dirs + "/" + files ) 
		if os.path.isfile(dirs + "/" + files):
			extensiones.append(getExtension(files))
			archivos.append(dirs + "/" + files)
	direcciones = updateContenedor(lastname(dirs), extensiones, nombre)
#	print(direcciones)
#	print(*archivos, sep="\n")
	for file in archivos:
	#	print(file, getExtension(file), direcciones[getExtension(file)[1::]] )
		move(file, direcciones[getExtension(file)[1::]])
	## creando  carpeta contenedora 

if __name__ == "__main__":
	main()
	# Vanessa Rodriguez Medina
	# mi amada niña 
