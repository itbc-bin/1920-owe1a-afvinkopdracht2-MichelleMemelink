genoom_drosophila_melanogaster = """AACTGTCTGGTAATACTAGAGCATATACGTCAAAAACGCGCTAATTTAAAAGTCGGTGGCTTGCAAAGAA
ATAGCTTAATAAATTATGGAGGATTTTGAGAAAATTGAGAAGATTGGCGAGGGCACATATGGCGTGGTGT
ATAAGGGTCGCAACCGCCTGACGGGCCAAATTGTGGCAATGAAGAAAATCCGCTTGGAGTCCGACGACGA
AGGCGTTCCATCAACCGCGATCAGGTAAAATGCCGCGGCTTGGACGCCCAAGCCTCAAAATGTTTCATGT
TCTTTCGCGACTTTTCCATTCAAATGGCTTATATGCTTAATTGAAAGTATGTTCCTTGACATCTTATGGG
TTGGTTTGAAGATTTTGCAATATTGTTTTTAATTTATACTGTGGAAGTCTAGCATAATTATGTTACGGCT
TATGTTCATCATACATATGTGTGTGTATGTACAATCCTATATGCGTACTTATGCTCATGTGTACATCATC
ATACTTTCTATTTATGTTTATTAATTGGAAGCCTGCGAATACTTTCTGGTTCAACTGATAGACCAATAAC
TAAAATACTTTAATCACATGTTTTTTCTATAATGTAGTAATATTTAATATCCATTACAGAGAAATTTCGT
TGCTTAAGGAGTTGAAACATGAAAACATTGTCTGTTTGGAGGATGTTTTGATGGAGGAGAACCGCATATA
CTTGATCTTTGAATTCCTATCGATGGACCTCAAGAAATACATGGATTCGCTGCCAGTTGATAAGCACATG
GAGAGTGAATTGGTCCGTAGCTATTTGTACCAAATAACTAGCGCCATTCTTTTCTGCCATCGTCGGCGAG
TACTTCACCGTGATCTTAAGCCGCAGAACTTACTAATCGACAAGAGTGGCCTCATAAAAGTCGCCGACTT
TGGACTTGGCCGATCCTTTGGCATTCCGGTGCGCATTTATACGCACGAGATTGTTACCTTGTGGTACAGA
GCGCCGGAGGTGCTACTGGGTTCACCCCGGTATTCCTGTCCCGTCGATATCTGGTCCATTGGATGCATAT
TCGCGGAGATGGCAACGAGAAAGCCGCTATTCCAGGGTGACTCGGAAATTGACCAGTTGTTTAGAATGTT
TAGGTAACCACAGGTAATTTACTTTCTATTCCCTGTGATACTCACACTCATTGATTGCAGAATTCTGAAA
ACACCTACCGAAGACATTTGGCCGGGCGTTACTTCGCTACCCGACTATAAGAACACGTTCCCCTGCTGGT
CCACGAACCAATTGACCAATCAGTTAAAGAATCTCGATGCGAATGGTATTGATCTCATACAAAAGATGTT
AATCTACGATCCAGTTCATCGCATTTCCGCCAAGGACATTTTGGAGCATCCCTATTTCAATGGTTTTCAA
TCGGGCTTAGTTCGAAATTAACGTTCGGTATTCTCGTTTGACTTTAACTAAGAATTTTAAAACAAGAGAT
CTTGGTATCTAATCTAAAGCAAAATAGCCGTAAATAAAACTAAGGGTGTAAAAC"""

#legnte bereken zonder enters.
lengte_genoom_drosophila_melanogaster = len(genoom_drosophila_melanogaster.replace("\n",""))
print ("lengte_genoom_drosophila_melanogaster:", (lengte_genoom_drosophila_melanogaster))

#aantal en CG
aantal_c =genoom_drosophila_melanogaster.count("C")
aantal_g =genoom_drosophila_melanogaster.count("G")

print ("Aantal_C:",aantal_c)
print ("Aantal_g:",aantal_g)

aantal_GC =(aantal_c+aantal_g)/(lengte_genoom_drosophila_melanogaster)*100
print ("Aantal_GC%:",aantal_GC, "%")





