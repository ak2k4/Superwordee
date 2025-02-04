import os
from gtts import gTTS
from google_trans_new import google_translator

def f1():
    f1b=input('Enter Back to go back:')
    if f1b=='back' or f1b=='BACK' or f1b=='Back':
        tutorial()
    else:
        print('Error....!')
        print('Please input the given word')
        f1()

def back_trans():
    back = str(input('To go back or to retry type Back and Retry respectively: '))
    if back=='back' or back=='BACK' or back=='Back':
        main()
    elif back=='retry' or back=='RETRY' or back=='Retry':
        text_trans()
    else:
        print('Error....!')
        print('Please input the given word')
        back_trans()
        
def back_speech():
    back = str(input('To go back or to retry type Back and Retry respectively: '))
    if back=='back' or back=='BACK' or back=='Back':
        main()
    elif back=='retry' or back=='RETRY' or back=='Retry':
        text_speech()
    else:
        print('Error....!')
        print('Please input the given word')
        back_speech() 
        
def back_detect():
    back = str(input('To go back or to retry type Back and Retry respectively: '))
    if back=='back' or back=='BACK' or back=='Back':
        main()
    elif back=='retry' or back=='RETRY' or back=='Retry':
        text_detect()
    else:
        print('Error....!')
        print('Please input the given word')
        back_detect()

def text_trans():
    print('_______________________________________________________')
    print('                    Text Translator                    ')
    print()
    word = str(input('Enter the sentence you wanted to convert:'))
    lang= str(input('Enter the language in which you wanted to translate:'))
    lang()
    trans = google_translator()
    out = trans.translate(word,lang_tgt=short_lang)
    print('loading.......')
    print('Translated sentence:',out)
    back_trans()
    print('_______________________________________________________')
    
def text_speech():
    print('_______________________________________________________')
    print('               Text to Speech Converter                ')
    print()
    word = str(input('Enter the sentence you wanted to convert:'))
    sound = gTTS(text=word,slow=False)
    sound.save('text_to_audio.mp3')
    print('loading.......')
    os.system('text_to_audio.mp3')
    back_speech()
    print('_______________________________________________________')
    
def text_detect():
    print('_______________________________________________________')
    print('                   Language Detector                   ')
    print()
    word = str(input('Enter the sentence you wanted to detect:'))
    trans = google_translator()
    out = trans.detect(word)
    out[1]=out[1].capitalize()
    print('loading.......')
    print('Language of the sentence:',out[1])
    back_detect()
    print('_______________________________________________________')
    
def main():
    print('_______________________________________________________')
    print('                      Start Window                     ')
    print()
    print('1.Text Translator')
    print('2.Text to Speech converter')
    print('3.Language Detector')
    print()
    print('To go back to Main Menu type Back')
    sub=input('Enter any of the one number to open it: ')
    print('loading.......')
    print('_______________________________________________________')
    if sub==1:
        text_trans()
    elif sub==2:
        text_speech()
    elif sub==3:
        text_detect()
    elif sub=='back' or sub=='BACK' or sub=='Back':
        main_menu()
    else:
        print('_______________________________________________________')
        print('Error....!')
        print('Please input the given number/word')
        print('Other feature coming soon!')
        print('_______________________________________________________')
        main()

def name():
    name=input('Enter your name:')
    gender=input('Enter your gender:')
    if gender=='m' or gender=='M' or gender=='male' or gender=='MALE' or gender=='Male':
        g_ans='Mr.'
    elif gender=='f' or gender=='F' or gender=='female' or gender=='FEMALE' or gender=='Female':
        g_ans='Ms/Mrs.'
    main_menu()
      
def main_menu():
    print('_______________________________________________________')
    print('                       Main Menu                       ')
    print()
    print('Welcome',g_ans,name,'to the program')
    print('1.Start')
    print('2.Tutorial')
    print('3.Supported Languages')
    print('4.Credits')
    num=int(input('Enter any of the one number to open it: '))
    if num==1:
        main()
    elif num==2:
        tutorial()
    elif num==3:
        slang()
    elif num==4:
        credit()
    else:
        print('_______________________________________________________')
        print('Error....!')
        print('Please input the given number')
        print('Other feature coming soon!')
        print('_______________________________________________________')
        main_menu()

def tutorial():
    print('_______________________________________________________')
    print('                       Tutorial                        ')
    print('Welome,',g_ans,name,'to the program')
    print('This program will provide the following feature:')
    print('1.Text Translator')
    print('2.Text into Speech')
    print('3.Language Dectector')
    print('To run this features type the number followed by the Start in Main Menu')
    print('Note:You should be connected to the internet to run the program')
    print()
    print('To know more about any of the feature type the number followed by them below')
    print('To go Back to the Main Menu type Back below')
    ans=input('Enter your answer here')
    print('_______________________________________________________')
    if ans==1:
        print('_______________________________________________________')
        print('                  Tutorial of feacture 1               ')
        print('As the name suggest this feature will help you to translate text into diffrent languages')
        print('To translale the text follow the step below:')
        print('Step 1:Type your text which you wanted to translate')
        print('Step 2:Type the language in which you wanted to translate into')
        print('Step 3:Wait for a small while and you will get the required output')
        print()
        f1()
        print('_______________________________________________________')
    elif ans==2:
        print('_______________________________________________________')
        print('                  Tutorial of feacture 2               ')
        print('As the name suggest this feature will help you to convert the text into speech/audio')
        print('To translale the text follow the step below:')
        print('Step 1:Type your text which you wanted to convert')
        print('Step 3:Wait for a small while and you will get the required output')
        print()
        f1()
        print('_______________________________________________________')
    elif ans==3:
        print('_______________________________________________________')
        print('                  Tutorial of feacture 3               ')
        print('As the name suggest this feature will help you to detect the language of your text ')
        print('To translale the text follow the step below:')
        print('Step 1:Type your text which you wanted to convert')
        print('Step 3:Wait for a small while and you will get the required output')
        print()
        f1()
        print('_______________________________________________________')
    elif ans=='back' or ans=='BACK' or ans=='Back':
        main_menu()
    else:
        print('_______________________________________________________')
        print('Error....!')
        print('Please input the given number/word')
        print('Other feature coming soon!')
        print('_______________________________________________________')
        tutorial()
   
    