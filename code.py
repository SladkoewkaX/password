def encrypt(data, shift):
    encrypted = " "
    for i in range(len(data)):
        char = data[i]
        if (char.isupper()):
            encrypted += chr((ord(char) + shift - 65) % 26 + 65)
        elif (char.islower()):
                encrypted += chr((ord(char) + shift - 97) % 26 + 97) 
        elif (char.isdigit()):
            number = (int(char) + shift) % 10
            encrypted = str(number)
        else:
            encrypted += char
    return encrypted    

def decrypt(data, shift):
    decrypted = ""
    for i in range(len(data)):
        char = data[i]
        if (char.isupper()):
            decrypted += chr((ord(char) - shift - 65) % 26 + 65)
        elif (char.islower()):
                decrypted += chr((ord(char) - shift - 97) % 26 + 97) 
        elif (char.isdigit()):
            number = (int(char) - shift) % 10
            decrypted = str(number)
        else:
            decrypted += char
    return decrypted     

menu = ""
while menu != '1' or menu != '2':
    menu = input('Would you like to save a new password or view your old ones?'
                '\n1. Input new password'
                '\n2. View passwords'
                '\n3. Exit: ')

    if menu == '1':
        softwareName = input("enter the name of the software you are using: ")
        username = input('enter your username for this software: ')
        password = input('enter your password for this software: ')
        shift = 5
        file = open('SecurePasswordData.txt', 'a')
        file.write(encrypt(softwareName, shift)+ ";|" + encrypt(username, shift)+ ';|' + encrypt(password, shift)+ '\n')
        file.close()
    if menu == '2':
        file = open('SecurePasswordData.txt', 'r')
        print('Software\t\tUsername\t\tPassword')
        for i in file:
            shift = 5
            data = i.split(';|')
            print(decrypt(data[0], shift)+ "\t\t" +decrypt(data[1], shift)+ "\t\t" + decrypt(data[2], shift))
    if menu == '3':
        exit()