import sys, random
import time
print(" Network and security Assignment")
print(" Name: Rogina Michelle Talaat Sidhome  "+" ID: 2019-02401")



class CaesarCipher:
    
    def encrypt(string,key):
        r = ""
        for char in string:
            if char == " ": 
                r += " "
                continue
            if ord(char) > 96 :
                r += chr((ord(char) + key - 97) % 26 + 97)
            else:
                r += chr((ord(char)+ key - 65) % 26 +65)
            
        return r
    
   
    @staticmethod
    def decrypt(string,key):
        r = ""
        for char in string:
            if char == " ":
                r += " "
                continue
            if ord(char) > 96 :
                r += chr((ord(char) - key - 97) % 26 + 97)
            else:
                r += chr((ord(char) - key -65) % 65 +65)
            
        return r


if __name__ == "__main__": 
   inp = input("Choose 1 for Ceaser cipher or 2 for Monoalphabetic")
   if inp == "1":
    String=input("Enter plain text")
    #String = " plain text"
    key = 3
    encrypted = CaesarCipher.encrypt(String,key)
    decrypted = CaesarCipher.decrypt(encrypted,key)
    print("Plain Text : ", String)
    print("Encrypted : ", encrypted)
    print("Decrypted : ", decrypted)





   if inp == "2":
      print("MONOALPHABETIC CIPHER")
      u = input("Choose 1 for Encryption  or 2 for Decryption")
      if u =='1':
    
       print("Encryption")
       print("Enter the plain text only alphabets and spaces) :")

       while True :
        plain_text = input().strip()
        plain_text = plain_text.replace(" ", "")
        if plain_text.isalpha() :
            break
        else :
            print("Please try again should contain only alphabets")
            print("Enter the plain text :")

      print("Enter the key capital alphabets with all unique letters and length should be 26 long :")
      while True :
        key = input().strip()
        if len(set(key)) == 26 and key.isupper() :
            break
        else :
            print("please try again Key must be in capital alphabets with all unique letters and length should be 26 :")
            print("Enter a valid key:")

      

      for j in range(10) :
        cipher_text = []
        for i in plain_text.upper() :
            cipher_text.append(key[ord(i) - ord('A')])
        

      print("Cipher-text is :", end = ' ')
      print("".join(cipher_text))
      

      if u =='2':
       print("Decryption")
       print("Enter the cipher text only capital alphabets without any spaces :")

       while True :
        cipher_text = input().strip()
        if cipher_text.isalpha() and cipher_text.isupper() :
            break
        else :
            print("Please try again should contain only capital alphabets without any spaces :")
            print("Enter the cipher-text :")

       print("Enter the key- capital alphabets with all unique letters and length should be 26 :")
       while True :
        key = input().strip()
        if len(set(key)) == 26 and key.isupper() :
            break
        else :
            print("Please try again in capital alphabets with all unique letters and length should be 26 :")
            print("Enter a valid key:")
        break
       

       for j in range(10) :
       
        plain_text = []
        for i in cipher_text :
            plain_text.append(chr(ord('A') + key.index(i)))
       
       print("Plain-text is :", end = ' ')
       print("".join(plain_text))
       if u=='3':
        print("Enter 1 or 2 only :")
   if inp=='3' :
      print("Enter 1 or 2 only :")




