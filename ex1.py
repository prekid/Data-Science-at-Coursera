print ('ovaj program sabira brojeve od 1 do 10')
pb = input ('unesite prvi broj: ')
db = input ('unesite drugi broj: ')
try:
    ipb = int(pb)
    idb = int(db)
except:
    print ("Greska, niste uneli brojeve")
    quit ()
if ipb>=0 and ipb<=10:
    if idb>=0 and idb<=10:
        zb = ipb + idb
        print ('zbir je:', zb)
    else:
        print ('drugi broj nije u granicama, pretesko mi je da izracunam')
        quit()
else:
    print ('prvi broj nije u granicama, pretesko mi je da izracunam')
