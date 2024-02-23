import socket
import sys

HOST = '192.168.20.65'
PORT = 5555
counter = 0  # compteur de connexions actives

# 1) création du socket :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2) liaison du socket à une adresse précise :
try:
    mySocket.bind((HOST, PORT))
except socket.error as e:
    print("La liaison du socket à l'adresse choisie a échoué.")
    sys.exit()

while True:
    # 3) Attente de la requête de connexion d'un client :
    print("Serveur prêt, en attente de requêtes ...")
    mySocket.listen(2)

    # 4) Etablissement de la connexion :
    connexion, adresse = mySocket.accept()
    counter += 1
    print("Client connecté, adresse IP %s, port %s" % (adresse[0], adresse[1]))

    # 5) Dialogue avec le client :
    msgServeur = "Vous êtes connecté au serveur Marcel. Envoyez vos messages."
    connexion.send(msgServeur.encode("utf-8"))
    msgClient = connexion.recv(1024).decode("utf-8")
    while True:
        print("C>", msgClient)
        if msgClient.upper() == "FIN" or not msgClient:
            break
        msgServeur = input("S> ")
        connexion.send(msgServeur.encode("utf-8"))
        msgClient = connexion.recv(1024).decode("utf-8")

    # 6) Fermeture de la connexion :
    connexion.send("fin".encode("utf-8"))
    print("Connexion interrompue.")
    connexion.close()

    ch = input("<R>ecommencer <T>erminer ? ")
    if ch.upper() == 'T':
        break
