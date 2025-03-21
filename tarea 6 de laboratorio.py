def cajero():
    s = 3000
    intento = 0

    while True:
        print(f"\nSaldo actual: Q{s}")
        monto = int(input("Ingrese monto a retirar (0 para salir): "))

        if monto == 0:
            print("Gracias por preferirinos.")
            break
        elif monto > s:
            intento += 1
            if intento >= 3:
                print("Ha excedido el número de intentos.")
                break
            print(f"Saldo insuficiente.: {3 - intento}")
        else:
            s -= monto
            print(f"Retiro exitoso. saldo actual: Q{s}")
            if s == 0:
                print("Saldo agotado. comuniquese con su banco.")
                break

cajero()
