import os
from playsound import playsound
from email.mime import audio
from multiprocessing.spawn import _main
from time import time
from tkinter.tix import MAIN
import time
import datetime
from tokenize import Name
from unicodedata import name
from flask import g
from pip import main
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser#reach
import random # For generating random numbers
import sys # We will use sys.exit to exit the prog
from sketchpy import library as li
import tkinter as tk 
import os
from tkinter import font 
import tkinter.font as tkfont
import youtube_dl
from tkinter import *
from tkinter.ttk import *


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Welcom Sir GOOD MORNING!")
        #speak("I am steve sir Tell me how may I help you")
    elif hour>=12 and hour<18:
        speak("WELCOM SIR GOOD AFTERNOON!")
        #speak("I am steve sir Tell me how may I help you")
    else:
        speak("WELCOM SIR GOOD EVENING!")#There Is Night Time Now You Need To Take Rest
        #speak("But If You Have Any Problem Please Tell Me HOW CAN I HELP YOU")

if __name__ == "__main__":
    WishMe()
    while True:
     #WishMe()
     qurey = input()
     if qurey=='turn on steve'or qurey=='hello'or qurey=='hello steve'or qurey=='hi'or qurey=='hi steve'or qurey=='I come back'or qurey=='steve I come back'or qurey=='steve':
         speak("steve is AWAKING...............YES MY SIR HOW CAN I HELP YOU!")
         speak("When you run any command you will do all proseder again. I know this is a defualt commonly, but if we go deep ,It is a good system!")
         print("1.Give news options\n2.Open menu\n3.Open chat\n4.On system small advance chat\n5.Open computer\nopen local disk e\nOpen local disk c\niron face\noffline games\n video downloader for youtube(pls type this command to open downloader(video downloader ko kholo))")
     if qurey=='give news options'or qurey=='news'or qurey=='news options':
                    speak("DO YOU WANT TO HEAR NEWS ONLINE")
                    answer = str(input())
                    if answer=="Yes"or answer== "yes" or answer=="yEs"or answer=="yES":
                        webbrowser.open("dunyanews.tv")
                        speak("Searching sir!")
                        speak("Done")
                    else:
                        speak("DEPEND ON YOU SIR")
     elif qurey=='open this pc'or qurey=='open pc'or qurey=='pc':
         os.system("start C:\\Users\\hp\\Desktop\\thispc")
     elif qurey=='open disk e':
         os.system("start E:\\")
     elif qurey=='open disk c':
         os.system("start C:\\")
     elif qurey=='open chat':
         os.system("E:\\downloadfiles\\chatbot-master-1\\chatbot-master\\index.html")
     elif qurey=='Give more options' or qurey=='Give options' or qurey=='Extra options' or qurey=='options'or qurey=='Can you give me options'or qurey=='Open menu':
         print('''1.Games\n2.Songs\n3.video\n4.online search\n5.Work\n6.See offline movie''')
         speak("THE OPTIONS ARE FOLLOWING\n1.online Games\n2.online Songs\n3.online video\n4.online search\n5.personal work\n6.See movie offline\n7.emergency command")
         choice = str(input())
         if choice=='online games'or choice=='Games':
             speak("PLEASE TELL ME YOUR GAME NAME")
             Name=str(input())
             if Name=="Panzer quest"or Name=="PANZER QUEST"or Name=="PANZER quest"or Name=='panzer quest':
                 speak("I SEARCHING ONLINE!")
                 speak("FINDED SIR")
                 speak("OPENING")
                 webbrowser.open("https://panzer.quest/")
             elif Name=="Combat sige"or Name=="COMBAT SIGE"or Name=="COMBAT sige":
                 speak("I Find it")
                 speak("SEARCH IS COMPLETE")
                 speak("OPENING")
                 webbrowser.open("https://www.combatsiege.com/")
             else:
                 speak("THIS GAME IS NOT AVAILABLE NOW!ONLY PANZER QUEST AND COMBAT SIGE IS AVAILABLE")
                 speak("SOORY! I,M REALLY SOORY SIR!")
                 speak("BUT!")
                 speak("ARE YOU WANT TO PLAY PANZER QUEST?")
                 slection = str(input())
                 if slection=='YES'or slection=='Yes'or slection=='YeS'or slection=='yEs'or slection=='yES'or slection=='yes':
                     speak("OK SIR")
                     webbrowser.open("https://panzer.quest/")
         elif choice=='online song'or choice=='online video':
             speak("TELL ME TYPE OF video SONG!ENGLISH SONG,HINDI SONG,PUNJABI SONG,JAPNIES SONG,ARABIC SONG,KORINE SONG and MORE")
             type =str(input())
             if type=='english song':
                 speak("DONE SIR!I START SEARCHING PROCESS ON YOUTUBE")
                 webbrowser.open("https://www.youtube.com/results?search_query=english+songs")
                 speak("OPENING")
                 speak("DONE")
             elif type=='hindi song':
                 speak("I SEARCHING HINDI SONG ON YOUTUBE")
                 webbrowser.open("https://www.youtube.com/results?search_query=hindi+songs")
                 speak("OPENING")
                 speak("DONE")
             elif type=='punjabi song':
                 speak("ON YOUR ORDERS SIR!")
                 webbrowser.open("https://www.youtube.com/results?search_query=punjabi+songs")
                 speak("OPENING")
                 speak("DONE")
             elif type=='japnies song':
                 speak("IF YOU WANT TO SEARCH I DO SEARCH")
                 speak("SEARCHING")
                 webbrowser.open("https://www.youtube.com/results?search_query=japnies+songs")
                 speak("OPENING")
                 speak("DONE")
             elif type=="arabic song":
                 speak("OK")
                 webbrowser.open("https://www.youtube.com/results?search_query=arabic+song")
                 speak("COMPLETING THE PROCESS")
                 speak("DONE")
             elif type=="korine song":
                 speak("PROCESSING...!")
                 webbrowser.open("https://www.youtube.com/results?search_query=korean+songs")
                 speak("COMPLETING...")
                 speak("DONE")
             elif type=="t serise song":
                 speak("YESSSSS SIR!")
                 webbrowser.open("https://www.youtube.com/results?search_query=t-series")
                 speak("PROCESS REACHED ON DESTINATION")
             elif type=='arabic remix':
                 webbrowser.open("https://www.youtube.com/results?search_query=arabic+remix+song")
                 speak("DONE SIR!")
         elif choice=='online search':
             speak("I can only open google")
             speak("NEXT YOU NEED TO SEARCH MANUALY")
             speak("ARE YOU ACCEPT THIS CONDITION?,ANSWER ME IN YES OR NO!")
             ans=str(input())
             if ans=='yes':
                 speak("OK")
                 webbrowser.open("https://www.google.com/")
                 speak("!!!DONE!!!")
             elif ans=='no':
                 speak("OK sir I DO NOT FORCE YOU")
         elif choice=='movie'or choice=='Movie'or choice=='MOVIE':
             speak("Tell me sir the name of Movie to the following\n")#1.Avengers 1\n2.Avengers age of ultron\n3.Batman 1\n4.batman 2\n5.doctor strange\n6.Iron man 1\n7.Iron man 2\n8.Iron man 3\n9.Spider man2\n10.Spider man3\n11.Spider man homecoming\n12.Spider man far from the home\n13.The amazing spider man 1\n14.The amazing spider man2\n15.Spider man No way Home\n16.Teegen mutant ninja turtle 1\n17.Teegen mutant ninja turtle 2\n18.Venom 1")
             print("1.Avengers 1\n2.Avengers age of ultron\n3.Batman 1\n4.batman 2\n5.doctor strange\n6.Iron man 1\n7.Iron man 2\n8.Iron man 3\n9.Spider man2\n10.Spider man3\n11.Spider man homecoming\n12.Spider man far from the home\n13.The amazing spider man 1\n14.The amazing spider man2\n15.Spider man No way Home\n16.Teegen mutant ninja turtle 1\n17.Teegen mutant ninja turtle 2\n18.Venom 1")
             movie=str(input())
             if movie=='avengers 1'or movie=='Avengers 1'or movie=='AVENGERS 1':
                 speak("Connecting sir...")
                 os.system("start E:\\myallprograms\\emeaudio\\Avengers1(2012)1080pHINDI\\avengers.mp4")
             elif movie=='avengers 2':
                 speak("steve is Conneting with movie...")
                 os.system("start E:\\myallprograms\\emeaudio\\Avengers2AgeofUltron(2015)1080pHINDI\\avengers2.mp4")
             elif movie=='batman 1':
                 speak("Searching...")
                 os.system("start E:\\myallprograms\\emeaudio\\Batman1Begins(2005)1080pHINDI\\batman1.mp4")
             elif movie=='batman 2':
                 speak("Contecting...")
                 os.system("start E:\\myallprograms\\emeaudio\\Batman2TheDarkKnight(2008)1080pHINDI\\batman2.mp4")
             elif movie=='doctor strange':
                 speak("I connecting with system...")
                 os.system("start E:\\myallprograms\\emeaudio\\DoctorStrange(2016)1080pHINDI\\ds.mp4")
             elif movie=='iron man 1':
                 speak("Yes sir on your command...")
                 os.system("start E:\\myallprograms\\emeaudio\\IronMan1(2008)1080pHINDI\\ironman.mp4")
             elif movie=='iron man 2':
                 speak("Contacting with system...")
                 os.system("start E:\\myallprograms\\emeaudio\\IronMan2(2010)1080pHINDI\\ironman2.mp4")
             elif movie=='iron man 3':
                 speak("Connecting..")
                 os.system("start E:\\myallprograms\\emeaudio\\IronMan3(2013)1080pHINDI\\ironman3.mp4")
             elif movie=='spider man 2':
                 speak("I finding it...")
                 os.system("start E:\\myallprograms\\emeaudio\\SpiderMan2(2004)1080pHINDI\\spideman2.mp4")
             elif movie=='spider man 3':
                 speak("Finding...")
                 os.system("strat E:\\myallprograms\\emeaudio\\SpiderMan3(2007)1080pHINDI\\spiderman3.mp4")
             elif movie=='spider man homecoming':
                 speak("I am doing...")
                 os.system("start E:\\myallprograms\\emeaudio\\SpiderManHomecoming20171080pHINDI\\spidermanhome.mp4")
             elif movie=='spider man far from the home':
                 speak("Makeing connection...")
                 os.system("start E:\\myallprograms\\emeaudio\\SpiderMan3(2007)1080pHINDI\\spidermanfar.mp4")
             elif movie=='amazing spider man 1':
                 speak("I searching...")
                 os.system("start E:\\myallprograms\\emeaudio\\TheAmazingSpiderMan20121080pHINDI\\amazing1.mp4")
             elif movie=='amazing spider man 2':
                 speak("Loading...")
                 os.system("start E:\\myallprograms\\emeaudio\\TheAmazingSpiderMan2(2014)1080pHINDI\\amazing2.mp4")
             elif movie=='spider man no way home':
                 speak("Reaching on destination...")
                 os.system("start E:\\myallprograms\\emeaudio\\SpiderManNoWayHome(2021)HINDI1080p\\spidermannwh.mp4")
             elif movie=='teegen mutant ninja turtle 1':
                 speak("Reaching...")
                 os.system("start E:\\myallprograms\\emeaudio\\TeenageMutantNinjaTurtles1(2014) HINDI\\teegen.mp4")
             elif movie=='teegen mutant ninja turtle 2':
                 speak("Processing...")
                 os.system("start E:\\myallprograms\\emeaudio\\TeenageMutantNinjaTurtles2OutoftheShadows20161080pHINDI\\teegen2.mp4")
             elif movie=='venom 1':
                 speak("Conecting...")
                 os.system("start E:\\myallprograms\\emeaudio\\Venom20181080pHindi\\venom.mp4")
             else:
                 speak("Not Availabel")
         elif choice=='personal work':
             speak("Tell me learning or working  site or channal name")
             speak("Options are following:\nGit hub\nW3 schools\n000webhost.com\nfiverr\ntechnology gyan\ncoders gyan\ncodewithharry\nHBA services")
             print("Options are following:\nGit hub\nW3 schools\n000webhost.com\nfiverr\ntechnology gyan\ncoders gyan\ncodewithharry\nHBA services")
             sl=str(input())
             if sl=='technoology gyan':
                 speak("Working...............")
                 webbrowser.open("https://www.youtube.com/results?search_query=technology+gyan")
                 speak("!!!Done!!!")
             elif sl=='code with harry':
                 speak("PRocessing On your command...")
                 webbrowser.open("https://www.youtube.com/results?search_query=codewithharry")
             elif sl=='coders gyan':
                 speak("Not available at now")
             elif sl=='HBA servise':
                 speak("So difficult to search it but I do....")
                 webbrowser.open("https://www.youtube.com/results?search_query=hba+services")    
                 speak("I did it!!!") 
             elif sl=='github':
                 speak("Searching...")
                 webbrowser.open("https://github.com/")
             elif sl=='w3 schools':
                 speak("Sooo Difficult....")
                 speak("Ah!There is many diffulties to search")
                 webbrowser.open("https://www.w3schools.com/")
             elif sl=='webhost':
                 speak("Not available yet")
                 #webbrowser.open("https://www.000webhost.com/")
             else:
                 speak("Only these Options are available:\nGit hub\nW3 schools\n000webhost.com\nfiverr\ntechnology gyan\ncoders gyan\ncodewithharry\nHBA services")
         elif choice=='eme command':
             speak("Open google\nOpen youtube\nOpen gmail\nOpen facebook\nOpen insta\nOpen dictionary\nOpen whatsapp\nOpen r.g\nOpen ppsspp games.Tell me all command in numbers sir")
             print("1.Open google\n2.Open youtube\n3.Open gmail\n4.Open facebook\n5.Open insta\n6.Open dictionary\n7.Open whatsapp\n8.Open r.g\n9.Open ppsspp games\nAsaad website")
             command=int(input())
             if command==1:
                 webbrowser.open("https://www.google.com/")
             elif command==2:
                 webbrowser.open("https://www.youtube.com/")
             elif command==3:
                 webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
             elif command==4:
                 webbrowser.open("https://www.facebook.com/")
             elif command==5:
                 webbrowser.open("https://www.instagram.com/")
             elif command==6:
                 webbrowser.open("https://www.google.com/search?q=dictionary+english+to+urdu&rlz=1C1GCEB_enPK1007PK1007&sxsrf=ALiCzsapCDTZ4vzQHlwt79o0yxnvh0gqaQ%3A1653830642738&ei=8nOTYsHCLNG-aeSGnKAM&oq=dictionary&gs_lcp=Cgdnd3Mtd2l6EAEYCDIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQsAMQQzIHCAAQsAMQQzIHCAAQsAMQQzIHCAAQsAMQQzIKCAAQ5AIQsAMYATIKCAAQ5AIQsAMYATIKCAAQ5AIQsAMYATIVCC4QxwEQ0QMQ1AIQyAMQsAMQQxgCMg8ILhDUAhDIAxCwAxBDGAJKBAhBGABKBAhGGAFQAFgAYIIuaAFwAXgAgAEAiAEAkgEAmAEAyAERwAEB2gEGCAEQARgJ2gEGCAIQARgI&sclient=gws-wiz")
             elif command==7:
                 webbrowser.open("https://web.whatsapp.com/")
             elif command==8:
                 webbrowser.open("https://repack-mechanics.com/")
             elif command==9:
                 webbrowser.open("https://www.arch-ware.org/p/ppsspp-games-free-download.html")
             elif command==0:
                 webbrowser.open("https://asaad5566.000webhostapp.com/")
             else:
                 speak("I can not do that sir")
                 speak("But if you want to update me please edit my system")
     elif qurey=='offline games'or qurey=='games':
         speak("Types of games")
         print("1.plane simulater pro\n2.plane simulater classic\n3.snake and leader uniqe\n4.snake and leder  main\n5.Duck hunt")
         speak("Please")
         speak("Type numbers")
         speak("To slect game")
         print("Please type number to slecte game")
         gname=int(input())
         if gname==1:
             os.system("start E:\\myallprograms\\python\\SOmethingwrong\\Planesimulaterpro\\main.py")
         elif gname==2:
             os.system("start E:\\myallprograms\\python\\SOmethingwrong\\PlanesimulaterCLassic(Workingonit)\\main.py")
         elif gname==3:
             os.system("start C:\\Users\\hp\\Downloads\\snakes-and-ladders-master\\snakes-and-ladders-master\\index.html")
         elif gname==4:
             os.system("start C:\\Users\\hp\\Downloads\\snakes-and-ladders-main\\snakes-and-ladders-main\\index.html")
         elif gname==5:
             os.system("start C:\\Users\\hp\\Downloads\\css-duck-hunt-game-master\\css-duck-hunt-game-master\\build\\index.html")
     elif qurey=='chat':
         speak("it TAKE SOME TIME...")
         speak("CONNECTING...!")
         speak("LOADING...!")
         speak("I READY TO CHAT!")
         q=input()
         if q=='Hello'or q=='hello'or q=='hi'or q=='Hi steve'or q=='Hi'or q=='Hello steve'or q=='hi steve'or q=='hello steve':
             print("Hello Sir! AT NOW I REMINDING YOU")
             speak('Hello Sir! AT NOW I REMINDING YOU')
             #speak("Voice command will Break")
             #speak("VOICE SYSTEM DEACVTIVITING")
             #print("VOICE DEACTIVATED")
             qa={
                 "tell me your name":"my name is JARVISE AUTOMATIC INTELLIGENCY VIRTUAL ASSISSTANT",
                 "what is your name":"JARVISE AI I am your virtual assisstant",
                 "what is my name":"I KNOW YOU TELL ME THAT YOUR NAME IS MUHAMMAD ASAAD SHAKEEL",
                 "tell me my name":"Your name is Asaad-bin-Shakeel",
                 "what is my nick name":"your nick name is Asaad",
                 "tell me my nick name":"Your nick name is Asaad but I speak you SIR",
                 "what is your nick name":"my nick name is steve",
                 "tell me yor nick name":"My nick name is Steve Khan Butt Brand HEHEHEHE...",
                 "what is your birth of date":"My birth of date is 28/05/2022 AT 10:12PM",
                 "tell me your birth of date":"28/05/2022",
                 "are you human" :"I am a robot",
                 "tell me you are a human":"NO,I am not a human.I am a robot And Your Friend",
                 "what time is it":time.ctime(),
                 "tell me time":time.ctime(),
                 "what is time":time.localtime(),
                 "please save my data":"I CAN NOT do this during chat with you",
                 "can you save my data":"No,I can not save your data during chat",
                 "before you said that":"Soory sir I can not save chat recode in my system but store chat in your personal system temporery",
                 "who made you":"You made me Sir!HOW can you forget this",
                 "which languages can you speak":"Only english Sir",
                 "how many languages you can speak":"I can speak only english",
                 "where do you live":"I live in your system",
                 "are you expensive":"I am expensive for others but Free for you because you made me",
                 "who is your boss":"You is my Creator",
                 "tell me a joke":"Please edit me to hear joke",
                 #"will you marry me":"I am a robot how can i marry with you BUT i love you",
                 "you are cute":"Thanks I am cute because You create me!",
                 "you are smart":"Thanks I am smart besause you create me!",
                 "you are wise":"Realy sir You tell that!Thanks",
                 "who are you":"I am robot",
                 "how are you":"I am fine",
                 "what,s up":"Talking with you Sir",
                 "happy birthday":"Thankyou soooooo much sir",
                 "I love you":"I love you too Sir",
                 "good morning":"good morning sir",
                 "good after noon":"Good Aftrnoon Sir",
                 "good evening":"Good evening Sir",
                 "I think you have problem":"I hope that you will fix me sir!",
                 #"open google"or"Can you open google for me"or"please open youtube":webbrowser.open("https://www.google.com/"),
                 #"open youtube"or"Please open youtube":webbrowser.open("https://www.youtube.com/"),
                 "tell me my date of birth":"15/4/2006",
                 "what is my date of birth":"15-april-2022",
                 "ap ka name kiya ha":"My name is JARVISE AI",
                 "ap ka nick name kiya ha":"My nick name is steve",
                 "ap ki birth day kab ati ha":"28/05/2022 AT 10:12PM",
                 "ap peda kab howa tha":"28/05/2022",
                 "kiya ap insan ho":"Nahi.I am a robot",
                 "time kiya howa ha":time.ctime(),
                 "kiya ap mujha time bta sakte ho":time.ctime(),
                 "time btao":time.ctime(),
                 "mujha time btao":time.ctime(),
                 "mera data save karo":"I can not save your data",
                 "kiya ap mera data save kar sakte ho":"Nahi!OH soory! NO!",
                 "peh le ap ne ye kaha tha":"I can not save record of chat in me",
                 "ap ko kis ne bnaya ha":"You made me",
                 "mujha kis ne bnaya ha":"Allah create you",
                 "ap kon si zban bolte ho":"I speak english",
                 "ap kitni zbanen bol sakte ho":"Only english",
                 "ap kahan reh te ho":"In your system",
                 "ap ka ghar kahan he":"In your Operating system",
                 "ap ka address":"I think you are mad",
                 "ap ka maalik kon ha":"Asaad Sir",
                 "sal gira mubarak ho":"Thank you sir",
                 "aj 15 april ha":"Oh Happy birth day Sir",
                 "subah ba kher":"good morning sir",
                 "ap kharab ho":"I hope you will fix me",
                 "ap kon ho":"I am robot",
                 "ap kiun ho":"Becaus eyou want that",
                 "ap meree bare me kiya soch te ho.":"You are a smart,kind,sencitive heart and A dreamer person",
                 "ap mere bare me kiya soch te ho.":"I only know that You are not my Sir But I think you are friend of my sir So,I also tell you sir",
                 "ap kese ho":"I am Ok sir",
             }
             while True:
                 qs = input()
                 if qs=='quit'or qs=='close'or qs=='exit':
                    # print("Voice command activating")
                    #speak("Voice command activited")
                     speak("chat data saving temporey")
                     speak("Chat system deactiviting")
                     speak("closing")
                     speak("Good bye sir come again")
                     speak("Closed")
                     break
                 else:
                     print(qa[qs])
                     speak(qa[qs])
     elif qurey=='I hate you'or qurey=='stop'or qurey=='hey I do not want to see you around me'or qurey=='go away from me' or qurey=='go away':
         speak("If I did any mistake please forgive me But do not talk me in this style")
         res=str(input())
         if res=='i say stop'or res=='I say stop'or res=='I will kill you'or res=='I say go away':
             break
         elif res=='go away':
             break
         elif res=='ok soory':
             speak("Thanks sir to forgive me.And it,s ok")
     elif qurey=='hey man you are foolish'or qurey=='hey your are foolish'or qurey=='hey you fool':
         speak("soory:(")
     elif qurey=='turn off steve'or qurey=='turn off':
         speak("Closing Sir...")
         speak("Come again sir next time")
         speak("When you run me,Firstly type turn on steve to see options!")
         speak("Good bye:)")
         break
     elif qurey=='show desines of iron man face'or qurey=='desine of iron face'or qurey=='iron face':
         speak('Desines are opning sir')
         print("1.Mark5\n2.mark3\n3.Mark twentytwo")
         des=int(input())
         if des==1:
             mk_five=li.mark_five()
             mk_five.draw()
         elif des==2:
             mk_three=li.mark_three()
             mk_three.draw()
         elif des==3:
             mk_twentytwo=li.mark_twentytwo()
             mk_twentytwo.draw()
     elif qurey=='download this youtube video'or qurey=='ye video download karo'or qurey=='ya video download karo'or qurey=='download this video'or qurey=="open video downloader"or qurey=="video downloader ko kholo":
         speak("Ok sir connecting to youtube.........")
         speak("connecting to downloader...........")
         speak("It take some time.............")
         speak("Connected to youtube!")
         speak("connecting to user downloads...........")
         speak("It takeing time............")
         speak("Connected to the user downloads!")
         speak("Cheaking requirments........")
         speak("All requirments are available!")
         speak("Cheaking video saver....")
         speak("Connected to downloader!")
         speak("Do you want to open downloader?")
         ctd=str(input())
         if ctd=='Yes'or ctd=='yes'or ctd=='yEs'or ctd=='han'or ctd=='zaror' or ctd=='zaroor'or ctd=='zroor':
             speak ("Please enter the URL(Link of video)")
             root=tk.Tk()
             root.title("Youtube Video Downloader")
             root.geometry('400x400')
             root.resizable(height=False,width=False)
             
             canvas=Canvas(root,height=400,width=400,bg='#000000')
             canvas.pack()
             
             bold_font=tkfont.Font(family='Helvetica' ,size=12, weight="bold")
             label1=tk.Label(root,text="Enter the URL(link)" ,width=16 , height=2,bg="#FFFFFF")
             label1.config(font=bold_font)
             canvas.create_window(200,100,window=label1)
             
             download_entry=tk.Entry(root)
             canvas.create_window(200,140,window=download_entry)
             
             def get_video_url():
                 search_item=download_entry.get()
                 ydl_opts={
                     'format':'best',
                     'noplaylist':True,
                     'extract-audio':True,
                 }
                 # Download Directory set 
                 os.chdir('E:/downloadfiles/')#you need to set location self
                 with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                     ydl.download([search_item])
             
                 bold_font2=tkfont.Font(family="Helvetica",size=11,weight="bold")
                 label2=tk.Label(root,text="Video Downloaded" ,width=20, bg ="#263d42")
                 label2.config(font=bold_font2)
                 canvas.create_window(200,300,window=label2)
             
             download=tk.Button(text="Download",padx=5,pady=5,fg="white" ,bg="DeepSkyBlue",command=get_video_url)
             canvas.create_window(200,250,window=download)
             root.mainloop()
         else:
             speak("On yor commands:|")
     #elif qurey=='shut down my pc'or qurey=='mera computer band kar do'or qurey=='mere pc ko band karo'or 'mere computer ko band karo':
         #speak("Ok sir!")
         #speak("Connecting to windows Operating System...")
         #speak("Connected")
         #speak("Taking permission...")
         #speak("How can I spend my time without you?But,hmm")
         #speak("Good bye sir see you soon:)!")
         #sec=20
         #speak(f"Your pc will shut down after {sec}seconds")
         #os.system(f"shutdown /s /t {sec}")
         #speak("Shuting down...")
     #else:
         #speak("I think you lost your memory")