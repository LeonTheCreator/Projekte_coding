import socket
#bib für den Socket, damit ich die Verbindung erstellen kann

hostip = input("Bitte eine IP-Adresse einfügen: ") 
portnrAnfang = int(input("Bitte die  Startportnummer einfügen: "))
portnrEnde = int(input("Bitte die Endportnummer einfügen: "))
#Anfang und Ende gewählt, weil es vorher nur eine Portnummer war


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket erfolgreich erstellt")
except socket.error as err:
    print(f"Socket creation failed with error {err}")
#Erstellung des Sockets


for port in range(portnrAnfang, portnrEnde + 1):
#die Range-Funktion geht vom Anfangswert los und endet vor dem Endwert, deswegen noch das +1, damit der Endwert inkludiert wird

    ausgabe_connection = s.connect_ex((hostip, port))
#Ausgabe ist nur "0" für connected oder "1" für nicht
#deswegen kann ich bei If-Verzweigung nur einen Wert nehmen

    if ausgabe_connection == 0:
        print(f"The Socket has succesfully connected on port {port}")


        banner = s.recv(1024)
        print(banner)
        s.close()

    else:
        print(f"The socket did NOT connect on port {port}")
#f vor dem String lässt mich variable im Text ausgeben

s.close()


