import random
import string
import secrets

def get_random_alphanumeric_string(letters_count, digits_count):
    sample_str = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
    sample_str += ''.join((random.choice(string.digits) for i in range(digits_count)))

    # Convert string to list and shuffle it to mix letters and digits
    sample_list = list(sample_str)
    random.shuffle(sample_list)
    final_string = ''.join(sample_list)
    return final_string


for i in range(0,3):

    print('\nEnter 0 for random Password\nEnter 1 for random Token')

    choice = int(input('\nEnter your choice:'))

    if (choice == 0):

        st = int(input("len of string ? "))
        dg = int(input("len of digit ? "))
        password = get_random_alphanumeric_string(st, dg)

        print("\nRandom password : ", password)
        save = str(input("\nDo you wanna save it ?\n(y/n)\n"))
        if(save == "y"):
            hint = str(input("Type a Hint for your Password : "))
            with open('rand_psw.txt', 'a') as file:
                file.write(hint + " : " + password)
                file.write("\n")
                file.close()
                print(".\n.\n.\n.\n.\nPassword saved!")
            break
        else:
            break

    elif (choice == 1):

        le = int(input("len of token ? "))
        token = secrets.token_hex(le)
        print("\nSecure random Token : ", token)
        save = str(input("\nDo you wanna save it ?\n(y/n)\n"))
        if (save == "y"):
            hint = str(input("Type a hint for your Token : "))
            with open('rand_tkn.txt', 'a') as file:
                file.write(hint + " : " + token)
                file.write("\n")
                file.close()
                print(".\n.\n.\n.\n.\nToken saved!")
            break
        else:
            break
    else:
        print('Invalid choice')
