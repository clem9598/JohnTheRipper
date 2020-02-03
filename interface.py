from tkinter import *
from tkinter import filedialog
from generation import *

class Interface(Frame) :
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=480, height=360, **kwargs)
        self.nb_clic = 0
        self.filename=""

        Frame0 = Frame(fenetre)
        Frame0.pack(side=TOP,padx=5,pady=5)
        Frame1 = Frame(fenetre)
        Frame1.pack(side=TOP,padx=5,pady=10)

        Frame2 = Frame(fenetre)
        Frame2.pack(padx=15, pady=5,side=LEFT)

        Frame3 = Frame(fenetre)
        Frame3.pack(padx=5, pady=5,side=BOTTOM)



        # Personnalisation de la fenêtre

        fenetre.title("John the Ripper")
        fenetre.geometry("600x400")
        fenetre.minsize(480, 360)
        label_title = Label(fenetre, text="JOHN THE RIPPER")
        print()

        # création de widgets 'Label' et 'Entry' :
        self.titre = Label(Frame0, text='JOHN THE REAPER')
        self.titre.pack(side="top")
        self.login = Label(Frame1, text="Login : ")
        self.login.pack(side="left")

        self.entrylogin = Entry(Frame1)
        self.entrylogin.pack(side="left", padx=6)

        self.entrymdp = Entry(Frame1)
        self.entrymdp.pack(side="right")

        self.mdp = Label(Frame1, text="Password : ")
        self.mdp.pack(side="right", padx=5)


        # Mise en page à l'aide de la méthode 'grid' :
        #txt1.grid(row =1, padx =5, pady = 10)
        #txt2.grid(row =1, column =2, padx =10, pady =2)

        #entr1.grid(row =1, column =1, padx =1, pady =2)
        #entr2.grid(row =1, column =3, padx =10, pady =2)

        self.choix_button = IntVar()
        button1 = Radiobutton(Frame2, text="Lettre devant Nom + date de naissance", variable=self.choix_button, value = 1)
        button2 = Radiobutton(Frame2, text="Mot de passe dérivé d'un animal", variable=self.choix_button, value = 2)
        button3 = Radiobutton(Frame2, text="Classique", variable=self.choix_button, value = 3)
        button4 = Radiobutton(Frame2, text="Animal + chiffres", variable=self.choix_button, value = 4)
        button5 = Radiobutton(Frame2, text="Voyelle inversé avec nombre + Majuscule", variable=self.choix_button, value = 5)
        button6 = Radiobutton(Frame2, text="Nom d'animal à l'envers dédoublé", variable=self.choix_button, value = 6)
        button7 = Radiobutton(Frame2, text="2 animaux concaténés", variable=self.choix_button, value = 7)


        button1.pack(padx =2, pady =5, anchor="w")
        button2.pack(padx =2, pady =5, anchor="w")
        button3.pack(padx =2, pady =5, anchor="w")
        button4.pack(padx =2, pady =5, anchor="w")
        button5.pack(padx =2, pady =5, anchor="w")
        button6.pack(padx =2, pady =5, anchor="w")
        button7.pack(padx =2, pady =5, anchor="w")


        self.crack = Button(Frame2, text = 'CRACK', command=self.search)
        self.crack.pack()


        self.result = Label(Frame2, text="Résultat : ")
        self.result.pack(anchor="w", padx=15, pady=5)
        self.res = Label(Frame2, text="")
        self.res.pack(anchor="e")

    def search(self):

        g = generation(self.entrylogin.get(),self.entrymdp.get())

        a=self.choix_button.get()
        rep=0

        if a==0:
            print("Choisissez une option")
        elif a==1:
            rep=g.choix1()
        elif a==2:
            rep=g.choix2()
        elif a==3:
            rep=g.choix3()
        elif a==4:
            rep=g.choix4()
        elif a==5:
            rep=g.choix5()
        elif a==6:
            rep=g.choix6()
        elif a==7:
            rep=g.choix7()
        elif a==9:
            if g.choix1()!=0:
                rep=g.choix1()
            elif g.choix2()!=0:
                rep=g.choix2()
            elif g.choix3()!=0:
                rep=g.choix3()
            elif g.choix4()!=0:
                rep=g.choix4()
            elif g.choix5()!=0:
                rep=g.choix5()
            elif g.choix6()!=0:
                rep=g.choix6()
            elif g.choix7()!=0:
                rep=g.choix7()

        if rep==0:
            self.res["text"] = "Décryptage impossible"
        else:
            self.res["text"]=rep

    def selectFile(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("text files", "*.txt"), ("all files", "*.*")))
