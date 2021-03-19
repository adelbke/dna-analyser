# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from main import dna_complement
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QInputDialog, QLineEdit ,QPushButton
from random import randint


RNA_to_acido_dic = {'UUU': 'Phe',
                    'UCU': 'Ser',
                    'UAU': 'Tyr',
                    'UGU': 'Cys',
                    'UUC': 'Phe',
                    'UCC': 'Ser',
                    'UAC': 'Tyr',
                    'UGC': 'Cys',
                    'UUA': 'Leu',
                    'UCA': 'Ser',
                    'UAA': '---',
                    'UGA': '---',
                    'UUG': 'Leu',
                    'UCG': 'Ser',
                    'UAG': '---',
                    'UGG': 'Trp',
                    'CUU': 'Leu',
                    'CCU': 'Pro',
                    'CAU': 'His',
                    'CGU': 'Arg',
                    'CUC': 'Leu',
                    'CCC': 'Pro',
                    'CAC': 'His',
                    'CGC': 'Arg',
                    'CUA': 'Leu',
                    'CCA': 'Pro',
                    'CAA': 'Gln',
                    'CGA': 'Arg',
                    'CUG': 'Leu',
                    'CCG': 'Pro',
                    'CAG': 'Gln',
                    'CGG': 'Arg',
                    'AUU': 'Ile',
                    'ACU': 'Thr',
                    'AAU': 'Asn',
                    'AGU': 'Ser',
                    'AUC': 'Ile',
                    'ACC': 'Thr',
                    'AAC': 'Asn',
                    'AGC': 'Ser',
                    'AUA': 'Ile',
                    'ACA': 'Thr',
                    'AAA': 'Lys',
                    'AGA': 'Arg',
                    'AUG': 'Met',
                    'ACG': 'Thr',
                    'AAG': 'Lys',
                    'AGG': 'Arg',
                    'GUU': 'Val',
                    'GCU': 'Ala',
                    'GAU': 'Asp',
                    'GGU': 'Gly',
                    'GUC': 'Val',
                    'GCC': 'Ala',
                    'GAC': 'Asp',
                    'GGC': 'Gly',
                    'GUA': 'Val',
                    'GCA': 'Ala',
                    'GAA': 'Glu',
                    'GGA': 'Gly',
                    'GUG': 'Val',
                    'GCG': 'Ala',
                    'GAG': 'Glu',
                    'GGG': 'Gly'}
mass_amino_acid =  {'A': 71.03711,
                    'C': 103.00919,
                    'D': 115.02694,
                    'E': 129.04259,
                    'F': 147.06841,
                    'G': 57.02146,
                    'H': 137.05891,
                    'I': 113.08406,
                    'K': 128.09496,
                    'L': 113.04049,
                    'M': 131.04049,
                    'N': 114.04293,
                    'P': 97.05276,
                    'Q': 128.05858,
                    'R': 156.10111,
                    'S': 87.03203,
                    'T': 101.04768,
                    'V': 99.06841,
                    'W': 186.07931,
                    'Y': 163.06333,
                    'Z': 0}
amino_acid_abr =   {'Ala': 'A',
                    'Cys': 'C',
                    'Asp': 'D',
                    'Glu': 'E',
                    'Phe': 'F',
                    'Gly': 'G',
                    'His': 'H',
                    'Ile': 'I',
                    'Lys': 'K',
                    'Leu': 'L',
                    'Met': 'M',
                    'Asn': 'N',
                    'Pro': 'P',
                    'Gln': 'Q',
                    'Arg': 'R',
                    'Ser': 'S',
                    'Thr': 'T',
                    'Val': 'V',
                    'Trp': 'W',
                    'Tyr': 'Y',
                    '---': 'Z'}

class Ui_MainWindow(object):

    N=0
    GC=0
    MASSE=0
    DNA=''
    RNA=''
    PROT=''
    PROT_abr=''
    DNA_COMP=''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(12)

        self.dna_label = QtWidgets.QLabel(self.centralwidget)
        self.dna_label.setGeometry(QtCore.QRect(210, 10, 70, 41))
        self.dna_label.setObjectName("dna_label")
        self.dna_label.setFont(font)

        self.rna_label = QtWidgets.QLabel(self.centralwidget)
        self.rna_label.setGeometry(QtCore.QRect(210, 65, 70, 41))
        self.rna_label.setObjectName("rna_label")
        self.rna_label.setFont(font)

        self.prot_label = QtWidgets.QLabel(self.centralwidget)
        self.prot_label.setGeometry(QtCore.QRect(210, 120, 70, 41))
        self.prot_label.setObjectName("prot_label")
        self.prot_label.setFont(font)

        self.dna_comp_label = QtWidgets.QLabel(self.centralwidget)
        self.dna_comp_label.setGeometry(QtCore.QRect(210, 180, 70, 41))
        self.dna_comp_label.setObjectName("dna_comp_label")
        self.dna_comp_label.setFont(font)

        self.gc_label = QtWidgets.QLabel(self.centralwidget)
        self.gc_label.setGeometry(QtCore.QRect(210, 240, 500, 41))
        self.gc_label.setObjectName("gc_label")
        self.gc_label.setFont(font)

        self.masse_label = QtWidgets.QLabel(self.centralwidget)
        self.masse_label.setGeometry(QtCore.QRect(210, 290, 500, 41))
        self.masse_label.setObjectName("masse_label")
        self.masse_label.setFont(font)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(280, 10, 450, 41))
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setEnabled(False)
        self.textEdit_2.setGeometry(QtCore.QRect(280, 60, 450, 41))
        self.textEdit_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setReadOnly(True)

        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setEnabled(False)
        self.textEdit_3.setGeometry(QtCore.QRect(280, 120, 450, 41))
        self.textEdit_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_3.setReadOnly(True)

        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setEnabled(False)
        self.textEdit_4.setGeometry(QtCore.QRect(280, 180, 450, 41))
        self.textEdit_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_4.setReadOnly(True)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 190, 650))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.bt_dna = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_dna.setObjectName("bt_dna")
        self.bt_dna.setFont(font)
        self.verticalLayout.addWidget(self.bt_dna)

        self.bt_dna_to_rna = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_dna_to_rna.setObjectName("bt_dna_to_rna")
        self.bt_dna_to_rna.setFont(font)
        self.verticalLayout.addWidget(self.bt_dna_to_rna)

        self.bt_rna_to_prot = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_rna_to_prot.setObjectName("bt_rna_to_prot")
        self.bt_rna_to_prot.setFont(font)
        self.verticalLayout.addWidget(self.bt_rna_to_prot)

        self.bt_comp_inv_adn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_comp_inv_adn.setObjectName("bt_comp_inv_adn")
        self.bt_comp_inv_adn.setFont(font)
        self.verticalLayout.addWidget(self.bt_comp_inv_adn)

        self.bt_taux_gc_adn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_taux_gc_adn.setObjectName("bt_taux_gc_adn")
        self.bt_taux_gc_adn.setFont(font)
        self.verticalLayout.addWidget(self.bt_taux_gc_adn)

        self.bt_freq_codons_adn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_freq_codons_adn.setObjectName("bt_freq_codons_adn")
        self.bt_freq_codons_adn.setFont(font)
        self.verticalLayout.addWidget(self.bt_freq_codons_adn)

        self.bt_mutation = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_mutation.setObjectName("bt_mutation")
        self.bt_mutation.setFont(font)
        self.verticalLayout.addWidget(self.bt_mutation)

        self.bt_motif_adn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_motif_adn.setObjectName("bt_motif_adn")
        self.bt_motif_adn.setFont(font)
        self.verticalLayout.addWidget(self.bt_motif_adn)

        self.bt_adn_cons_profil = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_adn_cons_profil.setObjectName("bt_adn_cons_profil")
        self.bt_adn_cons_profil.setFont(font)
        self.verticalLayout.addWidget(self.bt_adn_cons_profil)

        self.bt_masse_prot = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_masse_prot.setObjectName("bt_masse_prot")
        self.bt_masse_prot.setFont(font)
        self.verticalLayout.addWidget(self.bt_masse_prot)

        self.bt_epis_arn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_epis_arn.setObjectName("bt_epis_arn")
        self.bt_epis_arn.setFont(font)
        self.verticalLayout.addWidget(self.bt_epis_arn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 575, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport_fasta_file = QtWidgets.QAction(MainWindow)
        self.actionImport_fasta_file.setObjectName("actionImport_fasta_file")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionCopier = QtWidgets.QAction(MainWindow)
        self.actionCopier.setObjectName("actionCopier")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionImport_fasta_file)
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionCopier)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.dna_label.setText(_translate("MainWindow", "ADN"))
        self.rna_label.setText(_translate("MainWindow", "ARN"))
        self.prot_label.setText(_translate("MainWindow", "Protein"))
        self.dna_comp_label.setText(_translate("MainWindow", "Comp inv"))
        self.gc_label.setText(_translate("MainWindow",""))
        self.masse_label.setText(_translate("MainWindow",""))

        self.bt_dna.clicked.connect(self.show_dialog)
        self.bt_dna.setText(_translate("MainWindow", "Créer ADN"))

        self.bt_dna_to_rna.clicked.connect(lambda: self.translate_to_rna(self.DNA))
        self.bt_dna_to_rna.setText(_translate("MainWindow", "ADN vers ARN"))

        self.bt_rna_to_prot.clicked.connect(lambda: self.rna_to_prot(self.RNA))
        self.bt_rna_to_prot.setText(_translate("MainWindow", "ARN vers PROTEIN"))

        self.bt_comp_inv_adn.clicked.connect(lambda: self.dna_complement(self.DNA))
        self.bt_comp_inv_adn.setText(_translate("MainWindow", "COMP INV ADN"))

        self.bt_taux_gc_adn.clicked.connect(lambda: self.gc_taux(self.DNA))
        self.bt_taux_gc_adn.setText(_translate("MainWindow", "Taux GC ADN"))

        self.bt_freq_codons_adn.setText(_translate("MainWindow", "Fréq codons ADN"))
        self.bt_mutation.setText(_translate("MainWindow", "Mutation"))
        self.bt_motif_adn.setText(_translate("MainWindow", "Chercher motif ADN"))
        self.bt_adn_cons_profil.setText(_translate("MainWindow", "ADN consensus + profil"))

        self.bt_masse_prot.clicked.connect(lambda: self.masse(self.PROT))
        self.bt_masse_prot.setText(_translate("MainWindow", "Masse protéique"))

        self.bt_epis_arn.setText(_translate("MainWindow", "Epissage d\'ARN"))

        self.textEdit.setLineWrapColumnOrWidth(214748)
        self.textEdit.setLineWrapMode(self.textEdit.FixedPixelWidth)
        self.textEdit_2.setLineWrapColumnOrWidth(214748)
        self.textEdit_2.setLineWrapMode(self.textEdit.FixedPixelWidth)
        self.textEdit_3.setLineWrapColumnOrWidth(214748)
        self.textEdit_3.setLineWrapMode(self.textEdit.FixedPixelWidth)
        self.textEdit_4.setLineWrapColumnOrWidth(214748)
        self.textEdit_4.setLineWrapMode(self.textEdit.FixedPixelWidth)

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Editer"))
        self.actionImport_fasta_file.setText(_translate("MainWindow", "Import fasta file"))
        self.actionImport_fasta_file.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCopier.setText(_translate("MainWindow", "Copier"))
        self.actionCopier.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))

    def create_dna(self,n):
        self.DNA=''
        for i in range(1,n+1):
            self.DNA+='ACGT'[randint(0,3)]
        self.textEdit.setText(self.DNA)
        self.textEdit.setEnabled(True)
        print(self.DNA)    
    
    def show_popup(self,str):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(str)
        msg.setIcon(QMessageBox.Critical)
        x=msg.exec_()

    def show_dialog(self):
        n , result = QInputDialog.getInt(self.centralwidget, "Input Dialog", "Entrer la longueur:",min=1)
        if result:
            if n>0:
                self.N=n
                self.create_dna(n)
                print(self.DNA)
                print(self.N)
            else:
                self.show_popup("Vous devez donner un nombre positif")

    def translate_to_rna(self, dna_chain):
        self.RNA = self.textEdit.toPlainText()
        # self.RNA=dna_chain
        if (len(self.RNA)==0):
            self.show_popup("vous devez creer la chaine adn")
        else:
            self.RNA = self.RNA.replace("T", "U")
            self.RNA=self.RNA
            self.textEdit_2.setText(self.RNA)
            self.textEdit_2.setEnabled(True)
            print(self.RNA)
    
    def rna_to_prot(self,rna):
        self.RNA = self.textEdit_2.toPlainText()
        if (len(self.RNA)==0):
            self.show_popup("vous devez creer la chaine arn")
        else:
            index = 0
            l = []
            while index <= len(self.RNA)-1:
                if(len(self.RNA[index:index+3]) == 3):
                    l.append(RNA_to_acido_dic[self.RNA[index:index+3]])
                
                index += 3
            prot=''
            print(l)
            for ele in l:  
                prot += ele+' ' 
            for ele in l:  
                self.PROT += ele
            self.textEdit_3.setText(prot)
            self.textEdit_3.setEnabled(True)
            print(self.PROT)

    def dna_complement(self, adn):
        self.DNA = self.textEdit.toPlainText()
        if (len(self.DNA)==0):
            self.show_popup("vous devez creer la chaine ADN")
        else:
            for i in range(len(self.DNA)):
                if self.DNA[i] == 'A':
                    self.DNA_COMP += 'T'
                elif self.DNA[i] == 'T':
                    self.DNA_COMP += 'A'
                elif self.DNA[i] == 'C':
                    self.DNA_COMP += 'G'
                elif self.DNA[i] == 'G':
                    self.DNA_COMP += 'C'
            self.DNA_COMP=self.DNA_COMP[::-1]
            self.textEdit_4.setText(self.DNA_COMP)
            self.textEdit_4.setEnabled(True)
            print(self.DNA_COMP)
        
    def gc_taux(self,adn):
        self.DNA = self.textEdit.toPlainText()
        if (len(self.DNA)==0):
            self.show_popup("vous devez creer la chaine ADN")
        else:
            gc= int((self.DNA.count("C")+self.DNA.count("G")) / len(self.DNA) * 100)
            self.gc_label.setText("le taux de GC est: "+str(gc)+"%")
            self.GC=gc
            print(self.GC)

    def masse(self,prot):
        if (len(self.PROT)>0):
            index = 0
            l = []
            while index <= len(self.PROT)-1:
                if(len(self.PROT[index:index+3]) == 3):
                    l.append(amino_acid_abr[self.PROT[index:index+3]])
                
                index += 3
            print(l)
            for ele in l:  
                    self.PROT_abr += ele
            print(self.PROT_abr)
            for x in self.PROT_abr:
                self.MASSE+=mass_amino_acid[x]
            self.masse_label.setText("La masse proteique est : "+str(self.MASSE))
            print(self.MASSE)
        else:
            self.show_popup("vous devez creer le Proteine")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
