#Fullbit.py =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====
from bitcoinaddress import Wallet
import random

filename ='puzzle.txt'

with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1
with open(filename) as file:
    add = file.read().split()
add = set(add)
print('Total Bitcoin Addresses Loaded and Checking : ',str (line_count))
x=int(input("'Start range in BITs 0 or Higher(Puzzle StartNumber) -> "))
a = 2**x
y=int(input("Stop range Max in BITs 256 Max (Puzzle StopNumber) -> "))
b = 2**y
print("Starting search... Please Wait min range: " + str(a))
print("Max range: " + str(b))
print("==========================================================")
print('Total Bitcoin Addresses Loaded and Checking : ',str (line_count))
count=0
total=0

while True:
    count+=1
    total+=5
    ran=random.randrange(a,b)
    HEX = "%064x" % ran
    wallet = Wallet(HEX)
    uaddr = wallet.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr = wallet.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr = wallet.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr = wallet.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr = wallet.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif = wallet.key.__dict__['mainnet'].__dict__['wif']
    wifc = wallet.key.__dict__['mainnet'].__dict__['wifc']
    #print('\nPrivatekey (dec): ', ran,'\nPrivatekey (hex): ', HEX, '\nPrivatekey Uncompressed: ', wif, '\nPrivatekey compressed: ', wifc, '\nPublic Address 1 Uncompressed: ', uaddr, '\nPublic Address 1 Compressed: ', caddr, '\nPublic Address 3 Segwit: ', saddr, '\nPublic Address bc1 P2WPKH: ', bcaddr, '\nPublic Address bc1 P2WSH: ', bc1addr)
    print('Scan : ', count , ' : Total : ', total, ' : HEX : ', HEX, end='\r')
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