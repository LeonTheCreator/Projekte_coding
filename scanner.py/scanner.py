import argparse
import subprocess
import socket
 
def scan(ip, port) -> bool:
    # AF_INET = IPv4
    # SOCK_STREAM = TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Ohne diesen Timeout würde der Scan ewig dauern, wenn der Port nicht antwortet.
    # Damit sagen wir, nach 2 Sekunden soll der Scan abgebrochen werden, falls keine Antwort kommt.
    sock.settimeout(2)
 
    result = sock.connect_ex((ip, port))
        
    if result == 0:
        print(f"Port {port} ist offen.")
        return True
    else:
        print(f"Port {port} ist geschlossen.")
        return False
 
def ping(ip: str) -> bool:
    command = ["ping", "-n", "1", ip] # Das hier ist ein Array (Liste in Python)
    result = subprocess.run(command,capture_output=True,text=True)
 
    if result.returncode == 0:
        print(f"{ip} ist erreichbar.")
        return True
    else:
        print(f"{ip} ist nicht erreichbar.")
        return False
 
def info(ip, port):
    print("Dies ist eine Informationsmethode.")
    print(f"Das Angriffziel ist {ip}:{port}")
 
def main():
    parser = argparse.ArgumentParser(description="Ein einfaches Scanner-Programm.")
    parser.add_argument("-t","--target", help="Die Ziel-IP-Adresse für den Scan.", required=True)
    parser.add_argument("-p","--ports", type=int, nargs="+",help="Die Portnummer für den Scan.", required=True)
 
    args = parser.parse_args()
 
    result = ping(args.target)
    print(len(args.ports)) # args.ports...] Abfrage, ob die Länge >1
    anfangswert = args.ports[0]
    letzeWert = args.ports[1]

    #Hier muss die Schleife rein, wenn port.arg >1 ist

    if result == True:
        # Wenn der Host erreichbar ist (True) wird dieser Code ausgeführt.
        for i in range(letzeWert-anfangswert):
            scan(args.target, anfangswert + i)
            print(f"i: {i}")
    else:
        # Wenn der Host nicht erreichbar ist (False) wird dieser Code ausgeführt.
        exit(1)
            
 
if __name__ == "__main__":
    main()