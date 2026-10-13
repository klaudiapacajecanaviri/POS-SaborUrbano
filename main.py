#cambio de prueba1
monto_total_diario = 0.0
caja_abierta = True  

while caja_abierta:
    print ("MENÚ:")
    print ("1. Registrar venta")
    print ("2. ver total acumulado")
    print ("3. cerrar caja y salir")
    opcion = int(input("ingrese opción: "))    

    if (opcion == 1):

        print ("===REGISTRO VENTA===")
        sub_total = 0
        registro_venta = True

        while registro_venta:
            entrada = input("Ingrese Precio: ")


            if (entrada == "0" or entrada == "fin"):
                registro_venta = False 
            else:
                precio = float(entrada)
                sub_total = sub_total+precio
        print("BOLETA")
        print("Subtotal cliente: ", sub_total)
        Monto_Iva= sub_total *0.19
        Total_definitivo = Monto_Iva+sub_total
        print ("Monto IVA: ", Monto_Iva)
        print ("Total cliente: ",Total_definitivo)
        print ("1. Efectivo")
        print ("2. Tarjeta")
        metodo_pago = int(input("Seleccione el metodo de pago: "))

        if (metodo_pago == 1):
            descuento = Total_definitivo * 0.05
            Total_definitivo = Total_definitivo - descuento 
             
        if (Total_definitivo > 15000):
                print ("Venta Alta")
        else:
            print ("Venta Habitual")
            monto_total_diario = monto_total_diario + Total_definitivo

        print ("precio total: ", Total_definitivo)
        print ("Monto total diario: ", monto_total_diario)


    elif (opcion == 2):

        print ("===VER TOTAL ACUMULADO===")
        print ("monto total diario hasta el momento es de: ", monto_total_diario)

    else:
        print ("===CERRAR CAJA Y SALIR===")
        print ("monto total diario: ", monto_total_diario )
        print ("Gracias por usar nuestro sistema, adios")
        caja_abierta = False
        monto_total_diario = 0
        monto_total_diario = 0
