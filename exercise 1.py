dictionary={"Abnegation":"Renouncing a belief or doctrine",
            "Beguile":"influence someone in a deceptive way",
            "Cajole":"persuade by flattery or coaxing",
            "Disparate":"of a distinct kind",
            "Demagogue":"a political leader who uses rhetoric to appeal to prejudices and desires of ordinary citizens",
            }
ch = "yes"
while(ch=="yes"):
   print("Enter the word to know the meaning of the word")
   word=input()
   print("meaning of ",word," is ",dictionary[word])
   print("do you want to know more meanings?")
   ch=input()