'''
Created on Dec 9, 2012

@author: gustavokons
'''
from operator import itemgetter
import gdata.spreadsheet.service

class Pessoa(object):
    nome = None
    email = None
    telefone = None

    def __init__(self,nome,email,telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        
    def contaLetras(self):
        palavra = self.nome.lower()
        quants = {}
        for i in range(len(palavra)):
            if(quants.has_key(palavra[i])):
                quants[palavra[i]] += 1
            else:
                quants[palavra[i]] = 1

        q = sorted(quants.items(), key=itemgetter(1) , reverse=True)
        print "PALAVRA " + palavra.upper() + ":"
        for i in range(len(q)):
            print "letra "+q[i][0] + " = " + str(q[i][1]) + " ( " + str(round(q[i][1] / float(len(palavra))*100,2)) + " % ) "
    
    def inserirRegistroDocs(self):
        spreadsheet_key = '0Agk10_lnG2CxdDdzelBrZVNsQ3JIUFFEcFNTcV9wV1E'
        worksheet_id = 'od6'
        spr_client = gdata.spreadsheet.service.SpreadsheetsService()
        spr_client.email = 'gustavokons1@gmail.com'
        spr_client.password = 'morcego2006'
        spr_client.source = 'Pessoas'
        spr_client.ProgrammaticLogin()
        dados = {}
        dados['nome'] = self.nome
        dados['telefone'] = self.telefone
        dados['email'] = self.email
        entry = spr_client.InsertRow(dados, spreadsheet_key, worksheet_id)
    
    def gerarVCard(self):
        file = open(self.email+".vcf","w")
        file.write("BEGIN:VCARD\nVERSION:2.1\nN:"+self.nome+"\nEMAIL:"+self.email+
        "\nTEL;TYPE=HOME,VOICE:"+self.telefone+"\nEND:VCARD")
        file.close()   