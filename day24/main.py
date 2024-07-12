with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
    #file.close() with ile yazınca dosyayı kapatmaya gerek yok.

with open("my_file.txt", mode="a") as file: #mode "w" tüm yazdıklarımızı silip yazar.
    file.write("\nNew text.")
      
# sadece mode "w", açılan dosya yoksa kendisi oluşturur.      
