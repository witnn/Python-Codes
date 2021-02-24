# Simple Sezar type encrypter
# Author : Barış Kıvanç

def Menu():
    print("=" * 30)
    print("Simple Encrypter")
    print("=" * 30)

    def secim():
        print("1 - Encrypt \n2 - Decrypt \n" + ("-" * 16))
        choice = str(input("What do you want? = "))
        if choice == "1":
            init = str(input("\n"+"Enter the message = "))
            try :
                level = int(input("Enter encrypt key number(1,2..) = "))
            except ValueError:
                print("Encrypt key number must be integer!\nRebooting...")
                secim()
            finally:
                print("\n" + "Encrypted message = " + crypt(init, level) + "\n")
                secim()

        elif choice == "2":
            init = str(input("\n"+"Enter the encrypted message = "))

            try :
                level = int(input("Enter encrypt key number (the first number on message)= "))
            except ValueError:
                print("Encrypt key number must be integer!\nRebooting...")
                Menu()
            finally:
                print("\n"+"Decrypted message = " + decrypt(init, level)+ "\n")
                Menu()
        else:
            print("Wrong choice!")
            secim()
    secim()

def crypt(param, key):
    x = list(param)
    for i in range(len(x)):
        x[i] = chr(ord(x[i]) + key)
    cryptedPassword = end=""+"{}".format(key)
    for i in x:
        cryptedPassword += i
    return cryptedPassword

def decrypt(param, key):
    x = list(param)
    for i in range(len(x)):
        x[i] = chr(ord(x[i]) - key)
    decryptedPassword = ""
    for i in x:
        decryptedPassword += i
    return decryptedPassword

Menu()
