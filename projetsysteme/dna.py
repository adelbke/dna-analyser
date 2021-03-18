
from random import randint
class DNA():

    # this metaclass is here to implement getters
    #  and setters for these static variables

    
    _dna_chain= ""
    _rna_chain = ""
    _protein_chain = ""
    _dna_complement = ""
    _gc_rate = 0


    
    # generate DNA Sequence from length
    @classmethod    
    def generate_dna(cls,length: int):
        ADN = ''
        for i in range(0,length):
            ADN+='ACGT'[randint(0,3)]
        cls.dna_chain = ADN
        return cls.dna_chain
    
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
    
        
# DNA.generate_dna(15)
# DNA.translate_to_rna()
# print(DNA.rna_chain)
