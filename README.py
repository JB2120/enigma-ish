#enigma remake-ish
'''
 _____      _                         ______                     _        
|  ___|    (_)                        | ___ \                   | |       
| |__ _ __  _  __ _ _ __ ___   __ _   | |_/ /___ _ __ ___   __ _| | _____ 
|  __| '_ \| |/ _` | '_ ` _ \ / _` |  |    // _ \ '_ ` _ \ / _` | |/ / _ \
| |__| | | | | (_| | | | | | | (_| |  | |\ \  __/ | | | | | (_| |   <  __/
\____/_| |_|_|\__, |_| |_| |_|\__,_|  \_| \_\___|_| |_| |_|\__,_|_|\_\___|
               __/ |                                                      
              |___/                                                       

'''

#======================================================================================================================================================================
#importing pyperclip

import pyperclip

#======================================================================================================================================================================
#creating 'drums' and drum sets

purple   ='>\%9SJlix|+Ljtuq7)V?PQ\'T;]EH^z~bC-3o!$5k g4([#=AFnOD.d`wY1f2_NXm"@ZG&B:0}M<vh6acpK/rI8,W*eRys{U'
blue     ='O<03)b*e}I6D{Cyx\'uKd=]@G/Jiqa(MYpTQL41m7BXs^8kE`U_v!N[?l&\~.9V2og;F+f:Sn>zt"Pw%cR,$A -r|h5ZjWH#'
maroon   ='vOqY!3%-6R+f9Zh}N24ED<S8^Vm/AU$jx[zW"u_yMT`l?e0na:w@]LC;1gJ5)KB*Gt\Q.XIHd&~P (>ri\'7p=cF,ksb#|o{'
red      ='_%a*JHyDw$Ge=pxSKTIO~V`<#F@PbsUZ3W?jA&^R42d97Clc|-m"{nfLi\'8Q\[Y1g}>q+h!uzXEMoB6])t,;vN (r5:0k/.'
green    ='x3])[7wWm NQ\+|rEC!:*94hngXVI,&tij<y2sbkfLTa.?p#q0@R~^ZuB`_(SFAOJGYDc\'d}8>%=-P{6/$zHUKe1"Ml5o;v'
yellow   =' GDfa>}_xSrT;*tJjnFp9UKdlw\[Mm4qRhyN@)(cB]\'<$!3AW&E5Z1gL7zVoC.2Qb,eHiO=8v|X/+YP#%^?"-{~6u0I:ks`'
drums    = {'p':purple,'b':blue,'m':maroon,'r':red,'g':green,'y':yellow}
drum_ini = 'pbmrgy'

#======================================================================================================================================================================
#checks to see the settings are valid

def setcheck(setting):
    rtn = True
    for char in setting:
        if not char in 'pbmrgy':
            rtn = False
    return (rtn)
        
        
#======================================================================================================================================================================
#gather the settings of the day

setting = input('enter today\'s drum settings:  ')
while len(setting)!= 10 or not setcheck(setting):
    setting = input('enter today\'s drum settings(only initials of drum should be 10 characters long):  ')

#======================================================================================================================================================================
#gather message settings

key = input('enter the message key:  ')
while len(setting)!= 10 :
    setting = input('enter the message key(should be 10 characters long):  ')

#======================================================================================================================================================================
#convert settings to drum order


do = []
for drum in setting:
    do.append(drums[drum])
    

#======================================================================================================================================================================
#definfing rotation functions

def rotate(num,stri):
    num = int(num % len(stri))
    chars = stri[int(len(stri)-(num)): int(len(stri))]
    stri = stri[0:int(len(stri)-(num))]
    stri = chars + stri
    return stri

#rotate until function

def rot_to(char,stri):
    while str(stri[0]) != str(char):
        stri = rotate(1,stri)
    return (stri)

#======================================================================================================================================================================
#aligning drums


n = 0
for drum in do:
    do[n] = rot_to(key[n],drum)
    n += 1

#======================================================================================================================================================================
#deciding mode and gathering message

e_d = input('do you want to encrypt or decrypt a message?: ')
while not e_d.lower() in ['encrypt','decrypt']:
    e_d = input('do you want to encrypt or decrypt a message?(type either\'encrypt\' or \'decrypt\'): ')

message = input('input message to ' + e_d + ' : ')

#======================================================================================================================================================================
#rotating the drums to the finished position if decrypting

rot_num = len(message)
n = 0
if e_d == 'decrypt':
    for drum in do:
        do[n] = rotate(rot_num,drum)
        n+=1
        rot_num = int((rot_num +1) / len(drum))

#======================================================================================================================================================================
#making reverser function
def reverse(msg):
    translated = ''
    i = len(msg) - 1
    while i >= 0:
        translated = translated + msg[i]
        i = i - 1
    return translated

#======================================================================================================================================================================
#forward 'drum-run' encryption

def encrypt_char(char,do):
    return do[9][do[8].find((do[7][(do[6].find(do[5][(do[4].find(do[3][(do[2].find(do[1][do[0].find(char)]))]))]))]))]

#backward 'drum-run' decryption
def decrypt_char(char,do):
    return do[0][do[1].find((do[2][(do[3].find(do[4][(do[5].find(do[6][(do[7].find(do[8][do[9].find(char)]))]))]))]))]

#======================================================================================================================================================================
#making forward rotation sequence


def encrypt_msg (msg,do,key):
    cypher_txt = ''
    for char in msg:
        n = 0
        cypher_txt = cypher_txt + str(encrypt_char(char,do))
        do[n] = rotate(1,do[n])
        for drum in do:
            if do[n][0] == key[n]:
                do[n+1] = rotate (1,do[n+1])
                n += 1
            else:
                break
    return cypher_txt

#======================================================================================================================================================================
#making backward rotation sequence

def decrypt_msg (msg,do,key):
    cypher_txt = ''
    msg = reverse(msg)
    for char in msg:
        n = 0
        do[n] = rotate(-1,do[n])
        cypher_txt = cypher_txt + str(decrypt_char(char,do))
        
        for drum in do:
            if do[n][0] == key[n]:
                do[n+1] = rotate (-1,do[n+1])
                n += 1
            else:
                break
    return reverse(cypher_txt)

#======================================================================================================================================================================
#running encryption/ decryption

if e_d == 'encrypt':
    print(encrypt_msg (message,do,key))
    pyperclip.copy(encrypt_msg (message,do,key))
else:
    print(decrypt_msg (message,do,key))
    pyperclip.copy(decrypt_msg (message,do,key))

#======================================================================================================================================================================
#making sure the tab doesn't close

import os
os.system("pause")

#======================================================================================================================================================================
