#Fullbitgui.py =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====
from bitcoinaddress import Wallet
import random
import datetime
import os
import webbrowser
import PySimpleGUI as sg
from json import (load as jsonload, dump as jsondump)
from os import path
import smtplib
gmail_user = 'youremail@gmail.com'
gmail_password = 'yourpassword'
start_time = datetime.datetime.now()

filename ='puzzle.txt'

with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1
with open(filename) as file:
    add = file.read().split()
add = set(add)

start_time = datetime.datetime.now()


SETTINGS_FILE = path.join(path.dirname(__file__), r'settings_file.cfg')
DEFAULT_SETTINGS = {'theme': sg.theme()}
SETTINGS_KEYS_TO_ELEMENT_KEYS = {'theme': '-THEME-'}

def load_settings(settings_file, default_settings):
    try:
        with open(settings_file, 'r') as f:
            settings = jsonload(f)
    except Exception as e:
        sg.popup_quick_message(f'exception {e}', 'No settings file found... will create one for you', keep_on_top=True, background_color='red', text_color='white')
        settings = default_settings
        save_settings(settings_file, settings, None)
    return settings


def save_settings(settings_file, settings, values):
    if values:      
        for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:  
            try:
                settings[key] = values[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]]
            except Exception as e:
                print(f'Problem updating settings from window values. Key = {key}')

    with open(settings_file, 'w') as f:
        jsondump(settings, f)

    sg.popup('Settings saved')

def create_settings_window(settings):
    sg.theme(settings['theme'])

    def TextLabel(text): return sg.Text(text+':', justification='r', size=(15,1))

    layout = [  [sg.Text('Settings', font='Any 15')],
                [TextLabel('Theme'),sg.Combo(sg.theme_list(), size=(20, 20), key='-THEME-')],
                [sg.Button('Save'), sg.Button('Exit')]  ]

    window = sg.Window('Settings', layout, keep_on_top=True, finalize=True)

    for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:
        try:
            window[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]].update(value=settings[key])
        except Exception as e:
            print(f'Problem updating PySimpleGUI window from settings. Key = {key}')

    return window


def create_main_window(settings):
    sg.theme(settings['theme'])

    menu_def = [['&Menu', ['&Settings', 'E&xit']]]

    layout = [[sg.Menu(menu_def)],
              [sg.Text('Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB', size=(40,3), font=('Comic sans ms', 13)),
               sg.Text('Total Addresses Looking for : ', size=(35,1), font=('Comic sans ms', 14)),
               sg.Text(line_count, font=('Comic sans ms', 18)), sg.Text('', size=(10,1))],
               [sg.Button('', key='mizogg', size=(10,1), font=('Helvetica', 10), button_color=(sg.theme_background_color(), sg.theme_background_color()),
                         image_filename='mizogg.png', image_size=(400, 80), image_subsample=1, border_width=0),
               sg.Button('', key='face', size=(10,1), font=('Helvetica', 30), button_color=(sg.theme_background_color(), sg.theme_background_color()),
                         image_filename='MizoggFaceBW.png', image_size=(140, 80), image_subsample=1, border_width=0)],
              [sg.Text('Fullbitgui.py - This program has been running for................ ', size=(48,1), font=('Comic sans ms', 13)),
               sg.Text('', size=(16,1), font=('Comic sans ms', 13), key='_DATE_')],
              [sg.Text('')],
              [sg.Output(size=(96, 14), font=('Comic sans ms', 13), key='out')],
              [sg.Text('Start range in BITs (Puzzle StartNumber) -> ', size=(38,1), font=('Comic sans ms', 13)),
               sg.Input(size=(6,1), key='bitx', background_color='green', text_color='white', font=('Comic sans ms', 13)), sg.Text('', size=(6,1)),
               sg.Text('Stop range Max in BITs (Puzzle StopNumber) -> ', size=(38,1), font=('Comic sans ms', 13)),
               sg.Input(size=(6,1), key='bity', background_color='red', text_color='white', font=('Comic sans ms', 13)), sg.Text('', size=(6,1))],
              [sg.Button('Start/Stop',  font=('Comic sans ms', 12))]]

    return sg.Window('MIZOGG Fullbitgui.py',
                     layout=layout,
                     default_element_size=(10,1))


def main():
    window, settings = None, load_settings(SETTINGS_FILE, DEFAULT_SETTINGS )
    generator = False
    while True:
        if window is None:
            window = create_main_window(settings)
        event, values = window.Read(timeout=10)
        window.Element('_DATE_').Update(str(datetime.datetime.now()-start_time))
        if event in (None, 'Exit'):
            break
        elif event == 'Start/Stop':
            generator = not generator
            count=0
            total=0

        if generator:
            count+=1
            total+=5
            x=int(values['bitx'])
            y=int(values['bity'])
            ran= random.randrange(2**x,2**y)
            HEX = "%064x" % ran
            wallet = Wallet(HEX)
            uaddr = wallet.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
            caddr = wallet.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
            saddr = wallet.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
            bcaddr = wallet.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] # bc1 P2WPKH:
            bc1addr = wallet.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] # bc1 P2WSH:
            wif = wallet.key.__dict__['mainnet'].__dict__['wif'] # uncompressed WIF
            wifc = wallet.key.__dict__['mainnet'].__dict__['wifc'] # compressed WIF
            print('\nPrivatekey (dec): ', ran,'\nPrivatekey (hex): ', HEX, '\nPrivatekey Uncompressed: ', wif, '\nPrivatekey compressed: ', wifc, '\nPublic Address 1 Uncompressed: ', uaddr, '\nPublic Address 1 Compressed: ', caddr, '\nPublic Address 3 Segwit: ', saddr, '\nPublic Address bc1 P2WPKH: ', bcaddr, '\nPublic Address bc1 P2WSH: ', bc1addr)
            print('Scan : ', count , ' : Total : ', total)
            if caddr in add or uaddr in add or saddr in add or bcaddr in add or bc1addr in add:
                print('\nMatch Found')
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran))
                f.write('\nPrivatekey (hex): ' + HEX)
                f.write('\nPrivatekey Uncompressed: ' + wif)
                f.write('\nPrivatekey compressed: ' + wifc)
                f.write('\nPublic Address 1 Compressed: ' + caddr)
                f.write('\nPublic Address 1 Uncompressed: ' + uaddr)
                f.write('\nPublic Address 3 Segwit: ' + saddr)
                f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr)
                f.write('\nPublic Address bc1 P2WSH: ' + bc1addr)
                f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
                f.close()
                sent_from = gmail_user
                to = ['your@gmail.com']
                subject = ['OMG Super Important Message']
                body = '\nPrivatekey (dec): ' + str(ran) + '\nPrivatekey (hex): ' + HEX + '\nPrivatekey Uncompressed: ' + wif + '\nPrivatekey compressed: ' + wifc + '\nPublic Address 1 Uncompressed: ' + uaddr + '\nPublic Address 1 Compressed: ' + caddr + '\nPublic Address 3 Segwit: ' + saddr + '\nPublic Address bc1 P2WPKH: ' + bcaddr + '\nPublic Address bc1 P2WSH: ' + bc1addr +'\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====\n'
                
                email_text = """\
                    From: %s
                    To: %s
                    Subject: %s

                    %s
                    """ % (sent_from, ", ".join(to), subject, body)

                try:
                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    server.ehlo()
                    server.login(gmail_user, gmail_password)
                    server.sendmail(sent_from, to, email_text)
                    server.close()
                
                    print ('Email sent!')
                except:
                    print('Something went wrong...')
            
        elif event == 'Settings':
            event, values = create_settings_window(settings).read(close=True)
            if event == 'Save':
                window.close()
                window = None
                save_settings(SETTINGS_FILE, settings, values)


        elif event == 'mizogg':
            webbrowser.open_new_tab("https://mizogg.co.uk")
        
        elif event == 'face':
            webbrowser.open_new_tab("https://mizogg.com")

    
    window.Close()
    
main()

