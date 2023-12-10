def weight_conversion():
    berat = int(input("Masukkan berat anda > "))
    satuan = input("Dalam satuan apa berat yang anda masukkan? (K untuk KG, L untuk LBS)>")

    if satuan.lower() == 'k':
        converted_weight = round(berat * 2.20462, 2)
        print(f"Berat anda dikonversi menjadi pound adalah {converted_weight} lbs")
    elif satuan.lower() == 'l':
        converted_weight = round(berat / 2.20462, 2)
        print(f"Berat anda dikonversi menjadi kilogram adalah {converted_weight} kg")
    else:
        print("Satuan yang dimasukkan tidak valid. Silakan masukkan 'K' untuk KG atau 'L' untuk LBS.")

# Call the function to run the weight conversion
weight_conversion()
