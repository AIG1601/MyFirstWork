class Salud():
    def diagnostico(self):
        self.nombre = (input("ingrese su nombre: "))
        self.apellido = (input("ingrese su apellido: "))
        self.pais = (input("ingrese su pais o lugar en el que reside: "))
        self.genero = (input("ingrese su sexo: "))
                     
        while True:
            try :
                self.edad = int(input("ingrese su edad: "))
                break
            except:
                print("solo puedes ingresar numeros..."+"\n")
        if self.edad >= 18 :
            print("eres un adulto")
        elif self.edad >= 60:
            print("eres un anciano")
        else :
            print("eres un niño")
            
        while True:
            try:
                self.fecha = int(input("ingrese su fecha de nacimiento: "))
                break
            except:
                print("solo puedes ingresar numeros..." + "\n")  

                
paises = []        
estadisticas = 0
paciente = []
recuperados = []
descartados = []
fallecidos = []
confirmados = []
contador = 0
opc = 0
opcd = 0
respuesta = 0

while opc != 5 :
    print("")
    print("-----------BIENVENIDO-----------")
    print("1.- resgistrate si sospechas")
    print("2.- cantidad de casos en general")
    print("3.- datos de las personas registradas")
    print("4.-cambiar estatus")
    print("5.- salir" + "\n")
    opc = int(input('opcion:'))
    print("")

    if opc == 1 :
        persona = Salud()
        persona.diagnostico()
        paciente.append(persona)

        opcd = 0
        print("es hora de que me diga si usted ha presintado los siguientes sintomas: ")
        print("")
        print("1.-si")
        print("2.- no")
        print("")
        print("-fiebre")
        print("-tos")
        print("-dolor muscular")
        print("-dolor o incomodidad en la garganta")
        print("-dolor de cabeza")
        print("-dificultad para respirar")
        print("")
        opcd = int(input("opcion: "))
        print("")

        if opcd == 1:
            contador = contador +1
            print("tienes coronavirus")
            sospechositos = Salud()
            paciente.append(sospechositos)
            
        elif opcd == 2 :
            print("es solo una gripe")
            gripe = Salud()
            paciente.append(gripe)
        
    if opc == 2 :
        x = 0
        print("")
        print("-------REGISTRADOS-------")
        print("cantidad de casos en general")
        print("1.- ver pais")
        print("2.- ver por genero")
        print("3.- ver por edad")
        x = int(input("opcion: "))
        print("")

        if x == 1 :
            numero= Salud()
            #culo.diagnostico()
            paises.append(numero)
        if estado = "sospechosito":
            confimadito = salud()
            confirmadito.append(confirmadito)

        if x == 2:
            letra = salud()
            #zorra.diagnostico()
            genero. append(letra)
            #for i in genero:
                #print(i.genero)
            

    if opc == 3:
        print("-----------DATOS DE LOS REGISTRADOS-----------")
        for i in paciente :
            print( i.nombre,i.apellido,i.pais,i.genero,i.edad,i.fecha )


    if opc == 4:
        print("")
        
            
        
        
            
            

        
        

    

    

        
    
        
        
