# -*- coding: utf-8 -*-
from twx.botapi import *
import ipgetter

#leggo da file l'ultimo messagio a cui ero arrivato

dati = open("up.txt","r")
raw = dati.read()
offset = raw.split("\n")[0]
tokien = raw.split("\n")[1]
dati.close()

#inizializza il bot
bot = TelegramBot(tokien)
bot.update_bot_info().wait()
print (bot.username)

if (int(offset) != 0):
    print ("offset iniziale: ", offset)
else:
    offset = 1

while True:
    updates = bot.get_updates(offset).wait()
    for update in updates:
        print ("Nuovo update: ", update.update_id, "Da: ", update.message.sender.username, "\n")
        offset = int(offset) + 1
        if (update.message.text != None): #and update.update_id >= offset):
            dati = open("up.txt", "w")
            dati.seek(0)
            dati.write(str(offset))
            dati.close()
            print ("Non ancora processato: ", update.update_id , update.message.text, "\n")
            message = update.message.text.split()
            #print (message)
            for m in message:
                if (m.lower() == "/ip"):
                    ip = ipgetter.myip()
                    print ("Rispondo a ", update.message.sender.username, "con l'ip  \n")
                    bot.send_message(update.message.chat.id, "Here is the ip: " + ip)
                else:
                    print("Comando sconosciuto")
                    bot.send_message(update.message.chat.id, "/ip is all I can do for you now")
