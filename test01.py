#Name: Yun-Ting Tsai

alphabets = "abcdefghijklmnopqrstuvwxyz"
word = "coronavirus"
medications = ["remdesivir","hydroxychloroquine","azithromycin","quercetin"]

#1.
for alphabet in alphabets:
    if alphabet in word:
        print(word,"contains",alphabet)

#2.                
for alphabet in alphabets:       
    if alphabet in word:
        for medication in medications:
            if alphabet in medication:
                print(alphabet,"is in",word,"and also in",medication)
