import time
# Գրել ֆունկցիա, որը․
#    - կստանա արգումենտ մեքենայի արագությունը մղոն/ժ,
#    - կվերադարձնի մեքենայի արագությունը կմ/ժ և մ/վ տեսքով։

# def mile_km(mph):
#     km = mph * 1.60934
#
#
# print(mile_km(1))

#
#
# miph = int(input("Enter miph: "))
# kph = miph / 0.6214
# print("Speed:", miph, "miph = ", kph, "kph")
#
# miph = int(input("Enter miph: "))
# mps = miph * 0.44704
# print ("Speed:", miph, "miph = ", mps, "mph")
#
# def miph_to_kph(miph):
#    return miph / 0.6214
# print("speed_in_miph = ", int(miph_to_kph(25)))
#
# def miph_to_mps(miph):
#    return miph * 0.44704
# print("speed_in_mps = ", int(miph_to_mps(25)))


# 2. Գրել ֆունկցիա, որը․
#    - կհաշվի 1-ից 100_000_000 միջակայքում գտնվող 3-ի բաժանվող թվերի քանակը,
#    - կտպի այդ ֆունկցիայի կատարման ժամանակը վայրկյաններով։
# def div_by_3(end):
#     return len(range(3, end+1, 3))
#     return end // 3
#
#
# t = time.time()
#
# result = div_by_3(1_000_000_000_000)
# print(f"3i bajanvoxner: {result}")
#
# print(time.time() - t, "seconds")

# 3․ Գրել ծրագիր, որը․
# #    - կունենա թվերից բաղկացած list,
# #    - list-ը կբաժանի 2 list-երի այնպես,
# #      որ առաջին list-ում կլինեն նախնական list-ի առաջին, երրորդ, հինգերորդ և այլն էլեմենտները,
# #      իսկ երկրորդ list-ում՝ երկրորդ, չորորդ, վեցերորդ և այլն էլեմենտները,
# #    - կհաշվի և tuple-ով կտպի այդ list-երի միջին թվաբանականները,
# #    օրինակ՝ list_1 = [50, 60, 60, 45, 70]
# #    պետք է ստացվի՝ (60, 52.5):
# list_1 = [50, 60, 60, 45, 70]
# lst1 = list_1[::2]
# lst2 = list_1[1::2]
# c = tuple(sum(col)/ len(col) for col in [lst1, lst2])
# print(lst1)
# print(lst2)
# print(c)