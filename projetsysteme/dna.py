from random import randint
class DNA():

    # this metaclass is here to implement getters
    #  and setters for these static variables

    
    dna_chain= ""
    rna_chain = ""
    protein_chain = ""
    dna_complement = ""
    gc_rate = 0
    codon_frequency=0
    protein_mass = 0


    
    # generate DNA Sequence from length
    @classmethod    
    def generate_dna(cls,length: int):
        ADN = ''
        for i in range(0,length):
            ADN+='ACGT'[randint(0,3)]
        cls.dna_chain = ADN
    
    @classmethod
    def translate_to_rna(cls):
        cls.rna_chain = cls.dna_chain.replace("T", "U")
    
    @classmethod
    def rna_to_prot(cls):
        from .rna_to_acid import RNA_to_acido_dic
        rna = cls.rna_chain
        index = 0
        l = []
        while index <= len(rna)-1:
            if(len(rna[index:index+3]) == 3):
                l.append(RNA_to_acido_dic[rna[index:index+3]])
            
            index += 3
        prot=''
        # print(l)
        for ele in l:  
            prot += ele+' ' 
        cls.protein_chain = prot
    
    @classmethod
    def get_dna_complement(cls):
        adn = cls.dna_chain
        dna_comp=''
        conversion_dict = {
            'A':'T',
            'T':'A',
            'C':'G',
            'G':'C'
        }
        for x in adn:
            dna_comp += conversion_dict[x]

        cls.dna_complement = dna_comp
    
    @classmethod
    def taux_gc(cls):
        adn = cls.dna_chain
        gc= int((adn.count("C")+adn.count("G")) / len(adn) * 100)
        cls.gc_rate=gc
    
    @classmethod
    def taux_codons(cls):
        if cls.rna_chain == "":
            cls.translate_to_rna()
        from .rna_to_acid import RNA_to_acido_dic
        rna = cls.rna_chain
        freq = 0
        for index in range(0,len(rna),3):
            if index+3 < len(rna) and RNA_to_acido_dic[rna[index:index+3]] != "---":
                freq= freq+1
        cls.codon_frequency = freq
    
    @classmethod
    def masse(cls):
        from .acid_mass import amino_acid_abr, mass_amino_acid
        prot = cls.protein_chain.replace(' ','')
        if (len(prot)>0):
            index = 0
            l = []
            while index <= len(prot)-1:
                if(len(prot[index:index+3]) == 3):

                    l.append(amino_acid_abr[prot[index:index+3]])
                
                index += 3
            prot_abr = ""
            for ele in l:  
                prot_abr += ele
            mass = 0
            for x in prot_abr:
                mass+=mass_amino_acid[x]
            cls.protein_mass = mass
            # print(cls.MASSE)
        # else:
        #     cls.show_popup("vous devez creer le Proteine")

    
        
# DNA.generate_dna(31)
# DNA.taux_codons()
# DNA.rna_to_prot()
# print(DNA.protein_chain)
# print(DNA.codon_frequency)
