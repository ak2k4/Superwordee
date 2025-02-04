#Modules Used-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import time
import termcolor
from google_trans_new import google_translator

nc=termcolor.colored('NUMBER CONVERTION','red',attrs=['bold','underline'])
#Color For Number Convertion Sub-Heading-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
do=termcolor.colored('DECIMAL TO OTHER','red',attrs=['bold','underline'])
bo=termcolor.colored('BINARY TO OTHER','red',attrs=['bold','underline'])
oo=termcolor.colored('OCTAL TO OTHER','red',attrs=['bold','underline'])
ho=termcolor.colored('HEXADECIMAL TO OTHER','red',attrs=['bold','underline'])
#Color For Tutorial Sub-Heading----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
t1=termcolor.colored('TUTORIAL OF FEACTURE 1','red',attrs=['bold','underline'])
t2=termcolor.colored('TUTORIAL OF FEACTURE 2','red',attrs=['bold','underline'])
t3=termcolor.colored('TUTORIAL OF FEACTURE 3','red',attrs=['bold','underline'])
t4=termcolor.colored('TUTORIAL OF FEACTURE 4','red',attrs=['bold','underline'])
t5=termcolor.colored('TUTORIAL OF FEACTURE 5','red',attrs=['bold','underline'])
t6=termcolor.colored('TUTORIAL OF FEACTURE 6','red',attrs=['bold','underline'])
t7=termcolor.colored('TUTORIAL OF FEACTURE 7','red',attrs=['bold','underline'])
#Color For Application Name--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
texts=termcolor.colored(" ________________________________________________________________________________________ ",'red',attrs=['bold'])
text0=termcolor.colored("|         _____                          _       __               __          __         |",'red',attrs=['bold'])
text1=termcolor.colored("|        / ___/__  ______  ___  _____   | |     / /___  _________/ /__  ___  / /         |",'red',attrs=['bold'])
text2=termcolor.colored("|        \__ \/ / / / __ \/ _ \/ ___/   | | /| / / __ \/ ___/ __  / _ \/ _ \/ /          |",'red',attrs=['bold'])
text3=termcolor.colored("|       ___/ / /_/ / /_/ /  __/ /       | |/ |/ / /_/ / /  / /_/ /  __/  __/_/           |",'red',attrs=['bold'])
text4=termcolor.colored("|      /____/\__,_/ .___/\___/_/        |__/|__/\____/_/   \__,_/\___/\___(_)            |",'red',attrs=['bold'])
text5=termcolor.colored("|    _      __   /_/      __  ____                 __     _  __           __             |",'red',attrs=['bold'])
text6=termcolor.colored("|   | | /| / /__  _______/ / / __/__  ___ ___ ____/ /    / |/ /_ ____ _  / /  ___ ____   |",'red',attrs=['bold'])
text7=termcolor.colored("|   | |/ |/ / _ \/ __/ _  / _\ \/ _ \/ -_) -_) __/ _ \  /    / // /  ' \/ _ \/ -_) __/   |",'red',attrs=['bold'])
text8=termcolor.colored("|   |__/|__/\___/_/  \_,_/ /___/ .__/\__/\__/\__/_//_/ /_/|_/\_,_/_/_/_/_.__/\__/_/      |",'red',attrs=['bold'])
text9=termcolor.colored("|                             /_/                                                        |",'red',attrs=['bold'])
texte=termcolor.colored("|________________________________________________________________________________________|",'red',attrs=['bold'])
#To Clear Console------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def clear():
    time.sleep(1.5)
    print('\033[H\033[J')
#Color For Main Heading------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Login=termcolor.colored('LOGIN','blue',attrs=['bold','underline'])     
Main_menu=termcolor.colored('MAIN MENU','blue',attrs=['bold','underline'])
start=termcolor.colored('START WINDOW','blue',attrs=['bold','underline'])
tutorial=termcolor.colored('TUTORIAL','blue',attrs=['bold','underline'])
support=termcolor.colored('SUPPORT','blue',attrs=['bold','underline'])
credit=termcolor.colored('CREDITS','blue',attrs=['bold','underline'])

#Language Detector-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def back_detect():
    back = str(input('To go back or to retry type Back and Retry respectively: '))
    if (back=='back') or (back=='BACK') or (back=='Back'):
        print('________________________________________________________________________________________')
        clear()
        print()
        main()
    elif (back=='retry') or (back=='RETRY') or (back=='Retry'):
        print('________________________________________________________________________________________')
        clear()
        print()
        text_detect()
    else:
        print('Error....!')
        print('Please input the given word')
        back_detect()

def text_detect():
    print('________________________________________________________________________________________')
    print('                                   ',td,'                                   ')
    print()
    try:
        word = str(input('Enter the sentence you wanted to detect:'))
        trans = google_translator()
        out = trans.detect(word)
        out[1]=out[1].capitalize()
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('Language of the sentence:',out[1])
        print('Please remember the output before you procced further')
        back_detect()
    except:
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Failed!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('Error....!')
        print('Connection Error')
        back_detect()
    print('________________________________________________________________________________________')
    
#Number Convertion-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def back_dec():
    back = str(input('To go back or to retry type Back and Retry respectively: '))
    if (back=='back') or (back=='BACK') or (back=='Back'):
        print('________________________________________________________________________________________')
        clear()
        print()
        num()
    elif (back=='retry') or (back=='RETRY') or (back=='Retry'):
        print('________________________________________________________________________________________')
        clear()
        print()
        dec_n()
    else:
        print('Error....!')
        print('Please input the given word')
        back_dec()

def back_bin():
    back = str(input('To go back or to retry type Back and Retry respectively: '))
    if (back=='back') or (back=='BACK') or (back=='Back'):
        print('________________________________________________________________________________________')
        clear()
        print()
        num()
    elif (back=='retry') or (back=='RETRY') or (back=='Retry'):
        print('________________________________________________________________________________________')
        clear()
        print()
        bin_n()
    else:
        print('Error....!')
        print('Please input the given word')
        back_bin()

def back_oct():
    back = str(input('To go back or to retry type Back and Retry respectively: '))
    if (back=='back') or (back=='BACK') or (back=='Back'):
        print('________________________________________________________________________________________')
        clear()
        print()
        num()
    elif (back=='retry') or (back=='RETRY') or (back=='Retry'):
        print('________________________________________________________________________________________')
        clear()
        print()
        oct_n()
    else:
        print('Error....!')
        print('Please input the given word')
        back_oct()
        
def back_hex():
    back = str(input('To go back or to retry type Back and Retry respectively: '))
    if (back=='back') or (back=='BACK') or (back=='Back'):
        print('________________________________________________________________________________________')
        clear()
        print()
        num()
    elif (back=='retry') or (back=='RETRY') or (back=='Retry'):
        print('________________________________________________________________________________________')
        clear()
        print()
        hex_n()
    else:
        print('Error....!')
        print('Please input the given word')
        back_hex()

def dec_n():
    print()
    print('________________________________________________________________________________________')
    print('                                   ',do,'                                    ')
    print()
    num=input('Enter the Decimal number which you wanted to convert:')
    if num.isdecimal():
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        bn=bin(int(num))
        print('The Binary of',num,'is:',bn.replace('0b',''))
        on=oct(int(num))
        print('The Octal of',num,'is:',on.replace('0o',''))
        hn=hex(int(num))
        hn=hn.upper()
        print('The Hexadecimal of',num,'is:',hn.replace('0X',''))
        print()
        back_dec()
    else:
        print('Error....!')
        print('Please input a Deciaml number')
        print('________________________________________________________________________________________')
        clear()
        dec_n()

def bin_n():
    print()
    print('________________________________________________________________________________________')
    print('                                   ',bo,'                                    ')
    print()
    num=input('Enter the Binary number which you wanted to convert:')
    t='01'
    count=0
    for i in num:
        if i not in t:
            count=count+1
            break
        else:
            pass
    if count>0:
        print('Error....!')
        print('Please input a Binary number')
        print('________________________________________________________________________________________')
        clear()
        bin_n()
    else:
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('The Decimal of',num,'is:',int(num,2))
        on=oct(int(num,2))
        print('The Octal of',num,'is:',on.replace('0o',''))
        hn=hex(int(num,2))
        hn=hn.upper()
        print('The Hexadecimal of',num,'is:',hn.replace('0X',''))
        print()
        back_bin()

def oct_n():
    print()
    print('________________________________________________________________________________________')
    print('                                   ',oo,'                                    ')
    print()
    num=input('Enter the Octal number which you wanted to convert:')
    t='01234567'
    count=0
    for i in num:
        if i not in t:
            count=count+1
            break
        else:
            pass
    if count>0:
        print('Error....!')
        print('Please input a Octal number')
        print('________________________________________________________________________________________')
        clear()
        oct_n()
    else:
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('The Decimal of',num,'is:',int(num,8))
        bn=bin(int(num,8))
        print('The Binary of',num,'is:',bn.replace('0b',''))
        hn=hex(int(num,8))
        hn=hn.upper()
        print('The Hexadecimal of',num,'is:',hn.replace('0X',''))
        print()
        back_oct()
     
def hex_n():
    print()
    print('________________________________________________________________________________________')
    print('                                   ',ho,'                                    ')
    print()
    num=input('Enter the Hexadecimal number which you wanted to convert:')
    t='0123456789abcdefABCDEF'
    count=0
    for i in num:
        if i not in t:
            count=count+1
            break
        else:
            pass
    if count>0:
        print('Error....!')
        print('Please input a Hexadecimal number')
        print('________________________________________________________________________________________')
        clear()
        hex_n()
    else:
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('The Decimal of',num,'is:',int(num,16))
        bn=bin(int(num,16))
        print('The Binary of',num,'is:',bn.replace('0b',''))
        on=oct(int(num,16))
        print('The Octal of',num,'is:',on.replace('0o',''))
        print()
        back_hex()

def num():
    print()
    print('________________________________________________________________________________________')
    print('                                  ',nc,'                                    ')
    print()
    print('1.',termcolor.colored('Decimal to other','magenta',attrs=['bold']))
    print('2.',termcolor.colored('Binary to other','magenta',attrs=['bold']))
    print('3.',termcolor.colored('Octal to other','magenta',attrs=['bold']))
    print('4.',termcolor.colored('Hexadecimal to other','magenta',attrs=['bold']))
    print()
    print('To go back to Start type Back')
    ans=input('Enter your Answer:')
    if (ans=='1'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print()
        dec_n()
    elif (ans=='2'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print()
        bin_n()
    elif (ans=='3'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print()
        oct_n()
    elif (ans=='4'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print()
        hex_n()
    elif (ans=='back') or (ans=='BACK') or (ans=='Back'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print()
        main()
    else:
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Failed!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('Error....!')
        print('Please input the given word/number')
        print('________________________________________________________________________________________')
        clear()
        print()
        num()

#Start-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    print('________________________________________________________________________________________')
    print('                                     ',start,'                                      ')
    print()
    print('1.',termcolor.colored('Text Translator','magenta',attrs=['bold']))
    print('2.',termcolor.colored('Speech Translator','magenta',attrs=['bold']))
    print('3.',termcolor.colored('Text to Speech','magenta',attrs=['bold']))
    print('4.',termcolor.colored('Speech to Text','magenta',attrs=['bold']))
    print('5.',termcolor.colored('Text Detector','magenta',attrs=['bold']))
    print('6.',termcolor.colored('Speech Detector','magenta',attrs=['bold']))
    print('7.',termcolor.colored('Number Convertion','magenta',attrs=['bold']))
    print()
    print('To go back to Main Menu type Back')
    sub=input('Enter any of the one number to open it: ')
    print()
    if (sub=='1'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print()
        text_trans()
    elif (sub=='2'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print()
        speech_trans()
    elif (sub=='3'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print()
        text_speech()
    elif (sub=='4'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print()
        speech_text()
    elif (sub=='5'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print()
        text_detect()
    elif (sub=='6'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print()
        speech_detect()
    elif (sub=='7'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print()
        num()
    elif (sub=='back') or (sub=='BACK') or (sub=='Back'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print()
        main_menu()
    else:
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Failed!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('Error....!')
        print('Please input the given number/word')
        print('Other feature coming soon!')
        print('________________________________________________________________________________________')
        print()
        clear()
        print()
        main()
 
#Tutorial--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def tb1():
    tb=input('Type Back to go back:')
    if (tb=='back') or (tb=='BACK') or (tb=='Back'):
        print('________________________________________________________________________________________')
        clear()
        tutorialw()
    else:
        print('Error....!')
        print('Please input the given word')
        print('________________________________________________________________________________________')
        clear()
        print()
        print('________________________________________________________________________________________')
        print('                                 ',t1,'                                ')
        print()
        print('As the name suggests this feature will help you to translate text into diffrent languages')
        print('To translale the text follow the step below:')
        print('Step 1:Type your text which you wanted to translate')
        print('Step 2:Type the language in which you wanted to translate into')
        print('Step 3:Wait for a some time and you will get the required output')
        print('Note:To know the supported languages go to the Support tab in the Main Menu')
        print()
        tb1()

def tb2():
    tb=input('Type Back to go back:')
    if (tb=='back') or (tb=='BACK') or (tb=='Back'):
        print('________________________________________________________________________________________')
        clear()
        tutorialw()
    else:
        print('Error....!')
        print('Please input the given word')
        print('________________________________________________________________________________________')
        clear()
        print()
        print('________________________________________________________________________________________')
        print('                                 ',t2,'                                ')
        print()
        print('As the name suggests this feature will help you to translate speech to desied language')
        print('To translale the speech follow the step below:')
        print('Step 1:Enter the language in which you want to tanslate')
        print('Step 2:Type Fast or Slow to determine the speed of the translated speech')
        print('Step 3:Speak desied')
        print('Step 4:Wait for a small while and you will get the required output')
        print('Note:To know the supported languages go to the Support tab in the Main Menu')
        print()
        tb2()

def tb3():
    tb=input('Type Back to go back:')
    if (tb=='back') or (tb=='BACK') or (tb=='Back'):
        print('________________________________________________________________________________________')
        clear()
        tutorialw()
    else:
        print('Error....!')
        print('Please input the given word')
        print('________________________________________________________________________________________')
        clear()
        print()
        print('________________________________________________________________________________________')
        print('                                 ',t3,'                                ')
        print()
        print('As the name suggests this feature will help you to convert the text into speech/audio')
        print('To convert the text to audio follow the step below:')
        print('Step 1:Type your text which you wanted to convert')
        print('Step 2:Wait for a small while and you will get the required output')
        print()
        tb3()

def tb4():
    tb=input('Type Back to go back:')
    if (tb=='back') or (tb=='BACK') or (tb=='Back'):
        print('________________________________________________________________________________________')
        clear()
        tutorialw()
    else:
        print('Error....!')
        print('Please input the given word')
        print('________________________________________________________________________________________')
        clear()
        print()
        print('________________________________________________________________________________________')
        print('                                 ',t4,'                                ')
        print()
        print('As the name suggests this feature will help you to convert speech to text')
        print('To convert the speech to text follow the step below:')
        print('Step 1:Speak desied')
        print('Step 2:Wait for a small while and you will get the required output')
        print()
        tb4()

def tb5():
    tb=input('Type Back to go back:')
    if (tb=='back') or (tb=='BACK') or (tb=='Back'):
        print('________________________________________________________________________________________')
        clear()
        tutorialw()
    else:
        print('Error....!')
        print('Please input the given word')
        print('________________________________________________________________________________________')
        clear()
        print()
        print('________________________________________________________________________________________')
        print('                                 ',t5,'                                ')
        print()
        print('As the name suggests this feature will help you to detect the language of your text ')
        print('To detect the language follow the step below:')
        print('Step 1:Type your text which you wanted to detect')
        print('Step 2:Wait for a small while and you will get the required output')
        print()
        tb5()

def tb6():
    tb=input('Type Back to go back:')
    if (tb=='back') or (tb=='BACK') or (tb=='Back'):
        print('________________________________________________________________________________________')
        clear()
        tutorialw()
    else:
        print('Error....!')
        print('Please input the given word')
        print('________________________________________________________________________________________')
        clear()
        print()
        print('________________________________________________________________________________________')
        print('                                 ',t6,'                                ')
        print()
        print('As the name suggests this feature will help you to detect the language of your speech ')
        print('To detect the language follow the step below:')
        print('Step 1:Speak desied')
        print('Step 2:Wait for a small while and you will get the required output')
        print()
        tb6()

def tb7():
    tb=input('Type Back to go back:')
    if (tb=='back') or (tb=='BACK') or (tb=='Back'):
        print('________________________________________________________________________________________')
        clear()
        tutorialw()
    else:
        print('Error....!')
        print('Please input the given word')
        print('________________________________________________________________________________________')
        clear()
        print()
        print('________________________________________________________________________________________')
        print('                                 ',t7,'                                ')
        print()
        print('As the name suggests this feature will help you to convert number into differnt types ')
        print('To convert the language follow the step below:')
        print('Step 1:Select the type in which you wanted to convert your number ')
        print('Step 2:Type your number')
        print('Step 3:Wait for a small while and you will get the required output')
        print()
        tb7()

def tutorialw():
    print('________________________________________________________________________________________')
    print('                                      ',tutorial,'                                         ')
    print()
    print('Welome',g_ans,name,'to The Super Wordee!')
    print('This program will provide the following feature:')
    print('1.',termcolor.colored('Text Translator','magenta',attrs=['bold']))
    print('2.',termcolor.colored('Speech Translator','magenta',attrs=['bold']))
    print('3.',termcolor.colored('Text to Speech','magenta',attrs=['bold']))
    print('4.',termcolor.colored('Speech to Text','magenta',attrs=['bold']))
    print('5.',termcolor.colored('Text Detector','magenta',attrs=['bold']))
    print('6.',termcolor.colored('Speech Detector','magenta',attrs=['bold']))
    print('7.',termcolor.colored('Number Convertion','magenta',attrs=['bold']))
    print()
    print('To see this features type the number followed by the Start in Main Menu')
    print('Note:You should be connected to the internet to run the program')
    print()
    print('To know more about any of the feature type the number followed by them below')
    print('To go Back to the Main Menu type Back below')
    ans=input('Enter your answer here:')
    print()
    if (ans=='1'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print('________________________________________________________________________________________')
        print('                                 ',t1,'                                ')
        print()
        print('As the name suggests this feature will help you to translate text into diffrent languages')
        print('To translale the text follow the step below:')
        print('Step 1:Type your text which you wanted to translate')
        print('Step 2:Type the language in which you wanted to translate into')
        print('Step 3:Wait for a some time and you will get the required output')
        print('Note:To know the supported language go to the Support tab in the Main Menu')
        print()
        tb1()
    elif (ans=='2'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print('________________________________________________________________________________________')
        print('                                 ',t2,'                                ')
        print()
        print('As the name suggests this feature will help you to translate speech to desied language')
        print('To translale the speech follow the step below:')
        print('Step 1:Enter the language in which you want to tanslate')
        print('Step 2:Type Fast or Slow to determine the speed of the translated speech')
        print('Step 3:Speak desied')
        print('Step 4:Wait for a small while and you will get the required output')
        print('Note:To know the supported languages go to the Support tab in the Main Menu')
        print()
        tb2()
    elif (ans=='3'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print('________________________________________________________________________________________')
        print('                                 ',t3,'                                ')
        print()
        print('As the name suggests this feature will help you to convert the text into speech/audio')
        print('To convert the text to audio follow the step below:')
        print('Step 1:Type your text which you wanted to convert')
        print('Step 2:Wait for a small while and you will get the required output')
        print()
        tb3()
    elif (ans=='4'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print()
        print('________________________________________________________________________________________')
        print('                                 ',t4,'                                ')
        print()
        print('As the name suggests this feature will help you to convert speech to text')
        print('To convert the speech to text follow the step below:')
        print('Step 1:Speak desied')
        print('Step 2:Wait for a small while and you will get the required output')
        print()
        tb4()
    elif (ans=='5'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print()
        print('________________________________________________________________________________________')
        print('                                 ',t5,'                                ')
        print()
        print('As the name suggests this feature will help you to detect the language of your text ')
        print('To detect the language follow the step below:')
        print('Step 1:Type your text which you wanted to detect')
        print('Step 2:Wait for a small while and you will get the required output')
        print()
        tb5()
    elif (ans=='6'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print()
        print('________________________________________________________________________________________')
        print('                                 ',t6,'                                ')
        print()
        print('As the name suggests this feature will help you to detect the language of your speech ')
        print('To detect the language follow the step below:')
        print('Step 1:Speak desied')
        print('Step 2:Wait for a small while and you will get the required output')
        print()
        tb6()
    elif (ans=='7'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print()
        print('________________________________________________________________________________________')
        print('                                 ',t7,'                                ')
        print()
        print('As the name suggests this feature will help you to convert number into differnt types ')
        print('To convert the language follow the step below:')
        print('Step 1:Select the type in which you wanted to convert your number ')
        print('Step 2:Type your number')
        print('Step 3:Wait for a small while and you will get the required output')
        print()
        tb7()
    elif (ans=='back') or (ans=='BACK') or (ans=='Back'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        main_menu()
    else:
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Failed!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('Error....!')
        print('Please input the given number/word')
        print('Other feature coming soon!')
        print('________________________________________________________________________________________')
        clear()
        tutorialw()

#Support---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def back_support():
    ans=input('Type Back to go back to Support:')
    if ans=='back' or ans=='Back' or ans=='BACK':
        clear()
        print()
        slang()
    else:
        print('Error....!')
        print('Please input the given word')
        back_support()

def list_lang():
    file=open('slang.txt','r')
    reader=file.read()
    print(reader)
    back_support()

def list_accent():
    file=open('list_accent.txt','r')
    reader=file.read()
    print(reader)
    back_support()

def slang():
    print('________________________________________________________________________________________')
    print('                                       ',support,'                                         ')
    print()
    print('1.',termcolor.colored('Supported Languages','magenta',attrs=['bold']))
    print('2.',termcolor.colored('Supported Accents','magenta',attrs=['bold']))
    print()
    print('To go back to Main Menu type Back')
    sub=input('Enter any of the one number to open it:')
    print()
    if (sub=='1'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print()
        list_lang()
    elif (sub=='2'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print()
        list_accent()
    elif (sub=='back') or (sub=='BACK') or (sub=='Back'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print()
        main_menu()
    else:
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Falied!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('Error....!')
        print('Please input the given number/word')
        print('Other feature coming soon!')
        print('________________________________________________________________________________________')
        print()
        clear()
        print()
        slang()

#Credits---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def back_credit():
    back = str(input('To go back or to retry type Back and Retry respectively: '))
    if (back=='back') or (back=='BACK') or (back=='Back'):
        print('_________________________________________________________________________________________')
        clear()
        main_menu()
    elif (back=='retry') or (back=='RETRY') or (back=='Retry'):
        print('_________________________________________________________________________________________')
        clear()
        creditw()
    else:
        print('Error....!')
        print('Please input the given word')
        print('_________________________________________________________________________________________')
        clear()
        creditw()
        back_credit()

def creditw():
    print('_________________________________________________________________________________________')
    print('                                        ',credit,'                                        ')
    print()
    print(termcolor.colored('Created by:','magenta',attrs=['bold']),'Akshat M.Gupta and Atharv Kaushik')
    print(termcolor.colored('Class:','magenta',attrs=['bold']),'XII-Science')
    print(termcolor.colored('Subject:','magenta',attrs=['bold']),'Computer Science(083)')
    print(termcolor.colored('School:','magenta',attrs=['bold']),'The Aditya Birla Public School,Kesrol,Bharuch')
    print(termcolor.colored('Suppervisor:','magenta',attrs=['bold']),'Mrs.Rucha Patel')
    print()
    print(texts)
    print(text0)
    print(text1)
    print(text2)
    print(text3)
    print(text4)
    print(text5)
    print(text6)
    print(text7)
    print(text8)
    print(text9)
    print(texte)
    print()
    back_credit()

#Quit------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Quitw():
    print('________________________________________________________________________________________')
    print('                                        ',Quitl,'                                           ')
    print()
    print('Are you sure to Quit? type Yes or No:')
    Quit=input('Enter your answer here:')
    print()
    if Quit=='yes' or Quit=='Yes' or Quit=='YES'or Quit=='y' or Quit=='Y':
        print('________________________________________________________________________________________')
        clear()
        print()
        print('________________________________________________________________________________________')
        print()
        print()
        print('                          ',thank,'                            ')    
        print()
        print()
        print('________________________________________________________________________________________')
    elif Quit=='no' or Quit=='No' or Quit=='NO'or Quit=='n' or Quit=='N':
        clear()
        print()
        main_menu()
    else:
        print('Error....!')
        print('Please input the given word')
        clear()
        print()
        Quitw()
        print('________________________________________________________________________________________')

#Main Menu-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
current_date= time.strftime('%A %m %B,%Y')
def main_menu():
    print('________________________________________________________________________________________')
    print('                                      ',Main_menu,'                                      ')    
    print()
    print('                                                             ',current_date)
    print('Welcome',g_ans,name,'to The Super Wordee!')
    print('1.',termcolor.colored('Start','magenta',attrs=['bold']))
    print('2.',termcolor.colored('Tutorial','magenta',attrs=['bold']))
    print('3.',termcolor.colored('Support','magenta',attrs=['bold']))
    print('4.',termcolor.colored('Credits','magenta',attrs=['bold']))
    print('5.',termcolor.colored('Quit','magenta',attrs=['bold']))
    num=input('Enter any of the one number to open it: ')
    if (num=='1'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print()
        main()
    elif (num=='2'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print()
        tutorialw()
    elif (num=='3'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print()
        slang()
    elif (num=='4'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print()
        creditw()
    elif (num=='5'):
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('________________________________________________________________________________________')
        clear()
        print()
        Quitw()
    else:
        spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Failed!']
        for a in spin:
            print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
            time.sleep(0.18)
        print()
        print('Error....!')
        print('Please input the given number')
        print('Other feature coming soon!')
        print('________________________________________________________________________________________')
        clear()
        print()
        main_menu()

#Login-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print('_________________________________________________________________________________________')
print('                                        ',Login,'                                         ')
print()
print(texts)
print(text0)
print(text1)
print(text2)
print(text3)
print(text4)
print(text5)
print(text6)
print(text7)
print(text8)
print(text9)
print(texte)
print()
print('Welcome!')
name=input('Enter your name:')
if name=='' or name==None:
    name='User'
else:
    name=name
gender=input('Enter your gender:')
if gender=='m' or gender=='M' or gender=='male' or gender=='MALE' or gender=='Male':
    g_ans='Mr.'
elif gender=='f' or gender=='F' or gender=='female' or gender=='FEMALE' or gender=='Female':
    g_ans='Ms/Mrs.'
else:
    g_ans=''
name=name.capitalize()
spin=['Loading........','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','|','/','-','\\','Success!']
for a in spin:
    print('\b'+termcolor.colored(a,'green',attrs=['bold']),end='')
    time.sleep(0.18)
print()
print('_________________________________________________________________________________________')
clear()
print()
main_menu()
