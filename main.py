def ma'lum_harf_soni(matn):
    ma'lum_harf = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    soni = 0
    for harf in matn:
        if harf in ma'lum_harf:
            soni += 1
    return soni

matn = input("Matn kiriting: ")
print("Ma'lum harf soni:", ma'lum_harf_soni(matn))
