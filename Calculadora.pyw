from tkinter import * #importar interfaz grafica Tkinter.
from tkinter import messagebox # para cuadros de mensajes
#-------------------VENTANA--------------------------------------------
raiz = Tk() #raiz /root es una variable por convención. crea la ventana.
raiz.title("CALCULADORA COMUN") #titulo de ventana.
raiz.resizable(0,0) #width y height.impide redimensionar la ventana. 0 = false, 1 = true.
raiz.geometry("630x330") #cambia el tamaño, width (ancho) x height (alto)
raiz.config(bg="green") #bg para cambiar el color de fondo.
raiz.iconbitmap("calculator.ico") #localiza el icono,si esta en la misma ubicación,no es necesario la ruta completa.

#-------------------CUADRO--------------------------------------------
miFrame = Frame(raiz, width="630", height="320") #el primer parametro es de donde pertenece.
miFrame.pack(fill="both", expand="True") #redimensiona el frame en ambas direcciones.
miFrame.config(bg="#005A98") #color de fondo del frame
miFrame.config(bd=30) #valor de vorde
miFrame.config(relief="groove") #estilo de vorde
miFrame.config(cursor="hand2") #cambiar tipo de cursor.
#-------------------IMAGEN Y MENSAJE--------------------------------------------
miImagen=PhotoImage(file="Calculator_31.png")
Label(miFrame, image=miImagen, bg="#005A98").grid(row=0, column=0, padx=15,pady=15) #label es una etiqueta.
Label(miFrame, text="Hola soy una\n calculadora simple.", fg="red", bg="#005A98", font=("Monospac821 BT",16)).place(x=120,y=30) #coordenadas para poner el label.
#-------------------INPUT1--------------------------------------------
Label(miFrame, text="Numero 1:", bg="#005A98",font=("Comic Sans MS",12)).grid(row=1,column=0)
borrar1=StringVar() #es una cadena de caracteres
num1=Entry(miFrame, textvariable=borrar1) #textvariable es para asociar a la variable.
num1.grid(row=2, column=0,padx=5,pady=10)
num1.focus()
num1.config(justify="center", bg="#3FFFB9",fg="black", font="Unispace 10")
#-------------------INPUT2--------------------------------------------
Label(miFrame, text="Numero 2:", bg="#005A98",font=("Comic Sans MS",12)).grid(row=3,column=0)
borrar2=StringVar() #es una cadena de caracteres
num2=Entry(miFrame, textvariable = borrar2)
num2.grid(row=4, column=0,padx=5)
num2.config(justify="center", bg="#3FFFB9",fg="black",font="Unispace 10")

#-------------------OPERADORES FUNCIONES--------------------------------------------
# global + variable <- para operar con una varible que este fuera de la funcion.
valor = "0.0"
cambio = 2
def click(x):
    #corresponde al boton SUMA
    global cambio
    if cambio % x == 0:
        #cambia de color el boton a verde.
        suma.configure(bg="#00FF04",fg="black")
        resultado.configure(bg="yellow")
        global valor
        cambio += 1
        try:
            valor = float(num1.get()) + float(num2.get())
        except ValueError:
            valor = "Syntax Error!"
            resultado.configure(bg="red")
    else:
        #cambia al color inicial.
        suma.configure(fg="#3FFFD6", bg="#006B96")
        valor = "0.0"
        cambio += 1
def click2(x):
    #corresponde al boton RESTA
    global cambio
    if cambio % x == 0:
        resta.configure(bg="#00FF04",fg="black")
        resultado.configure(bg="yellow")
        global valor
        cambio += 1
        try:
            valor = float(num1.get()) - float(num2.get())
        except ValueError:
            valor = "Syntax Error!"
            resultado.configure(bg="red")
    else:
        resta.configure(fg="#3FFFD6", bg="#006B96")
        valor = "0.0"
        cambio += 1
def click3(x):
    #corresponde al boton MULTIPLICACIÓN
    global cambio
    if cambio % x == 0:
        MULTIPLICACIÓN.configure(bg="#00FF04",fg="black")
        resultado.configure(bg="yellow")
        global valor
        cambio += 1
        try:
            valor = "{0:.1f}".format(float(num1.get()) * float(num2.get()))
        except ValueError:
            valor = "Syntax Error!"
            resultado.configure(bg="red")
    else:
        MULTIPLICACIÓN.configure(fg="#3FFFD6", bg="#006B96")
        valor = "0.0"
        cambio += 1
def click4(x):
    #corresponde al boton DIVISIÓN
    global cambio
    if cambio % x == 0:
        DIVISIÓN.configure(bg="#00FF04",fg="black")
        resultado.configure(bg="yellow")
        global valor
        cambio += 1
        try:
            valor = "{0:.3f}".format(float(num1.get()) / float(num2.get()))
        except ValueError:
            valor = "Syntax Error!"
            resultado.configure(bg="red")
        except ZeroDivisionError:
            valor = "Infinito"
    else:
        DIVISIÓN.configure(fg="#3FFFD6", bg="#006B96")
        valor = "0.0"
        cambio += 1
#-------------------BOTONES DE OPERADORES--------------------------------------------
#TITULO QUE NO VARIA -->
Label(miFrame, text="        Operación:",bg="#005A98",font=("Comic Sans MS",12)).grid(row=1,column=2,columnspan=2)
#BOTON DE SUMA -->
suma = Button(miFrame, text="SUMA", fg="#3FFFD6", bg="#006B96",command= lambda: click(2))
suma.grid(row=2, column=1,padx=5)
#BOTON DE RESTA -->
resta = Button(miFrame, text="RESTA", fg="#3FFFD6", bg="#006B96",command= lambda: click2(2))
resta.grid(row=2, column=2,padx=5)
#BOTON DE MULTIPLICACIÓN -->
MULTIPLICACIÓN = Button(miFrame, text="MULTIPLICACIÓN", fg="#3FFFD6", bg="#006B96",command= lambda: click3(2))
MULTIPLICACIÓN.grid(row=2, column=3,padx=5)
#BOTON DE DIVISIÓN -->
DIVISIÓN = Button(miFrame, text="DIVISIÓN", fg="#3FFFD6", bg="#006B96",command= lambda: click4(2))
DIVISIÓN.grid(row=2, column=4,padx=5)

#-------------------RESULTADO FINAL--------------------------------------------
def result():
    #asigna resultado final segun operador al Label "resultado"
    resultado.configure(text=valor)
    if valor == "Syntax Error!":
        messagebox.showerror("Syntax Error!", "INGRESASTE UN VALOR INVALIDO! ")
#BOTON DE IGUAL =
igual = Button(miFrame, text="=",fg="#3FFFD6", bg="#006B96",font="Arial 14",command=result)
igual.grid(row=4, column=1)
#TEXTO QUE NO VARIA.
Label(miFrame, text="        Resultado:",bg="#005A98",font=("Comic Sans MS",12)).grid(row=3,column=2,columnspan=2)
#MUESTRA POR PANTALLA EL RESULTADO FINAL.
resultado= Label(miFrame, text="0.0",bg="YELLOW",font=("Comic Sans MS",14))
#resultado.config(justify="left")
resultado.grid(row=4,column=2,columnspan=3)
#-------------------BOTON PARA REINICIAR--------------------------------------------
def clean():
    #me permite borrar tanto los valores ingresados como el resultado.
    resultado.configure(text="0.0")
    resultado.configure(bg="yellow")
    borrar1.set("")
    borrar2.set("")
    num1.focus()
imgR=PhotoImage(file="Refresh.png")
reiniciar = Button(miFrame, image=imgR,fg="#3FFFD6", bg="#006B96", command=clean)
reiniciar.grid(row=4,column=2)

#-------------------BOTON PARA FINALIZAR PROGRAMA--------------------------------------------
salir = Button(miFrame,text="SALIR",fg="#3FFFD6", bg="#006B96",command=quit)
salir.grid(row=4, column=4)
#-------------------FIRMAS--------------------------------------------
firma = Label(miFrame, text="by Luis Peralta | V1.0", bg="#005A98",fg="#FAFDFF")
firma.place(x=455,y=250)
firma2 = Label(miFrame, text="Informatorio", bg="#005A98",fg="#FAFDFF")
firma2.place(x=490,y=0)

raiz.mainloop() #es como un bucle infinito, para que pueda ejecutarse la ventana.siempre a lo ultimo.
