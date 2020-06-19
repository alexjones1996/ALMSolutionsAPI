from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from httplib2 import Http
from oauth2client import file, client, tools



from django.shortcuts import render, redirect
#from .models.fornecedores import t_fornecedor
#from .models.clientes import t_cliente
#from .models.eventos import t_evento
#from .forms.forms import fornecedorForm, clienteForm, eventoForm



SCOPES = ['https://www.googleapis.com/auth/calendar']
'''
titulo = input('digite o titulo do evento: ')
dataInicio = input('Digite a data: ')
dataFim = input('Digite a data: ')
participantes = input('Digite e-mail de participantes: ')

def criarEvento(titulo, dataInicio, dataFim, participantes):
    try:
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None


    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)

    GCAL = build('calendar', 'v3', http=creds.authorize(Http()))




    EVENT = {
        'summary': titulo,
        'start':{'timeZone': 'America/Sao_Paulo',
            'dateTime': dataInicio},
        'end':{'timeZone': 'America/Sao_Paulo',
            'dateTime': dataFim},
        'attendees': [
            {'email': participantes},
        ]
    }
    

    evento = GCAL.events().insert(calendarId='primary',
            sendNotifications=False, body=EVENT).execute()


if __name__ == '__main__':
    criarEvento(titulo, dataInicio, dataFim, participantes)
'''


store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)

GCAL = build('calendar', 'v3', http=creds.authorize(Http()))





EVENT = {
    'summary': 'Aniversario3',
    'start':{'timeZone': 'America/Sao_Paulo',
        'date': '2020-06-19'},
    'end':{'timeZone': 'America/Sao_Paulo',
        'date': '2020-06-20'},
    'attendees': [
        {'email': 'alexjones19961996@gmail.com'},
    ]
}


#EVENT_ID=eventos.Events.list(calendarId).items[0].id
EVENT_ID = '2ogrrl4vbl57200ep45u5emgb8'
evento = GCAL.events().patch(calendarId='primary', eventId= EVENT_ID,
        sendNotifications=False, body=EVENT).execute()


print('Evento Modificado')





#if __name__ == '__main__':
#    atualizaevento()

    