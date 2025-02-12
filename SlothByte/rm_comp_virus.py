def remove_virus(files):
    list_files = files[10:].split(', ')
    protected = ['notvirus', 'antivirus']

    for i, f in enumerate(list_files):
        if ('virus' in f or 'malware' in f) and (protected[0] not in f and protected[1] not in f):
            list_files[i] = 0;

    new_list = [i for i in list_files if i != 0]

    if (len(new_list) != 0):
        res = ', '.join(new_list)
        print("PC Files: " + res)
    else:
        print("PC Files: Empty")

if __name__ == "__main__":
    remove_virus("PC Files: spotifysetup.exe, virus.exe, dog.jpg")
    remove_virus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe ")
    remove_virus("PC Files: notvirus.exe, funnycat.gif")
    remove_virus("PC Files: virus.exe")