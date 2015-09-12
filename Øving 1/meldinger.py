def main():
    tid = ["23:59","0:00","0:03","0.09","0:09","0.09"]
    navn = ["Mr. Y", "Mdm. Evil", "Dr. Horrible","Mr.Y","Mr.Y","Dr. Horrible"]
    meldinger = ["Har du mottatt pakken?", "Ja. Pakken er mottatt", "All you need is love!", "Dr. Horrible, Dr. Horrible , calling Dr. Horrible .","Dr. Horrible, Dr. Horrible wake up now." ,"Up now!"]
    
    #Skriver ut alle meldinger
    for i in range(0, len(meldinger)):
        logg(tid[i], navn[i], meldinger[i])

def logg(tid,navn, melding):
    print("Klokken " + tid + " sendte " + navn + " følgende melding: " + melding)
    
main()