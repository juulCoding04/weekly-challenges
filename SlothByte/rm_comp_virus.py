def remove_virus(files):
    list_files = files[10:].split(', ')
    print(list_files)
    protected = ['notvirus', 'antivirus']

    for f in list_files:
        if ('virus' in f or 'malware' in f) and (protected[0] not in f and protected[1] not in f):
            print("virus found")

if __name__ == "__main__":
    remove_virus("PC Files: spotifysetup.exe, virus.exe, dog.jpg")
    remove_virus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe ")
    remove_virus("PC Files: notvirus.exe, funnycat.gif")
    remove_virus("PC Files: virus.exe")