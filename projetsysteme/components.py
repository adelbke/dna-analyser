from PyQt5.QtWidgets import QFormLayout, QInputDialog, QLabel, QMainWindow, QHBoxLayout, QMessageBox, QTextEdit, QVBoxLayout, QWidget, QToolBar, QPushButton
# from PyQt5.QtCore import Qt

from .dna import DNA

class AbstractWindow(QMainWindow):
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__()
        # self.setMinimumWidth(1500)
    
    def setupMainLayout(self,sidebarLayout, mainLayout):
        layout = QHBoxLayout()
        left = QWidget()
        left.setLayout(sidebarLayout)

        right = QWidget()
        right.setLayout(mainLayout)
        
        layout.addWidget(left)
        layout.addWidget(right)

        layout.setStretch(0, 0)
        layout.setStretch(1, 7)

        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.centralwidget.setLayout(layout)

    def setMenuItems(self):
        self.menu_fichier = self.menuBar().addMenu("Fichier")
        self.menu_edit = self.menuBar().addMenu("Edit")    
    

class SidebarLayout(QVBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.setupButtons()
        
        
        self.btn_creer_adn.clicked.connect(self.action_creer_adn)
    
    def action_creer_adn(self):
        n,result = QInputDialog.getInt(QWidget(), "Input Dialog", "Entrer la longueur:",0,0)
        if result:
            if n>0:
                N=n
                DNA.generate_dna(N)
                print(self.parentWidget().window().mainLayout.output_ADN.setText(DNA.dna_chain))
            else:
                msg = QMessageBox()
                msg.setWindowTitle("create dna")
                msg.setText("Vous devez donner un nombre positif")
                msg.setIcon(QMessageBox.Critical)
                x=msg.exec_()
    
    def setupButtons(self):
        # setup buttons list
        self.buttons = [
            ('Créer ADN','creer_adn'),
            ('ADN vers ARN','adn_vers_arn'),
            ('ARN vers Proteine','arn_vers_proteine'),
            ('Comp INV ADN','comp_inv_adn'),
            ('taux GC ADN','taux_gc_adn'),
            ('fréq codons ADN','freq_codons_adn'),
            ('Mutation','mutation'),
            ('Chercher Motif ADN','chercher_motif_adn'),
            ('ADN Consensus + profil','adn_consensus_profil'),
            ('Masse Proteïque','masse_proteique'),
            ('Epissage d\'ADN','epissage_adn'),
        ]
        # create and assign buttons
        for btn in self.buttons:
            setattr(self,'btn_' + btn[1],QPushButton(btn[0]))
            self.addWidget(getattr(self,'btn_' + btn[1]))
        self.addStretch()

    

class MainLayout(QFormLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        
        elements = [
            ('ADN','dna_chain'),
            ('ARN','rna_chain'),
            ('Proteine','protein_chain'),
            ('Comp Inv','dna_complement')
        ]
        for element in elements:
            label = QLabel(element[0])
            textEdit = QTextEdit()
            textEdit.setReadOnly(True)

            setattr(self,'label_'+element[0], label)
            setattr(self,'output_'+element[0],textEdit)
            self.addRow(getattr(self,'label_'+element[0]),getattr(self,'output_'+element[0]))




class QPrimaryButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.setStyleSheet("background-color: indigo;color:white;font-weight:bold;")

