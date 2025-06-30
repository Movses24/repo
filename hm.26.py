# 1․ Գրել ֆունկցիա, որը․
#    - որպես արգումենտ կընդունի շրջանագծի շառավիղը (r) և սեկտորի անկյունը (alpha) ռադիաններով արտահայտված,
#    - կհաշվի և կտպի համապատասխան շառավղով և անկյունով սեկտորի մակերեսը,
#    - բանաձևը՝ S = (pi * r ** 2) * alpha / 360, բանաձևի մեջ alpha-ն արտահայտված է աստիճաններով։
# import math
#
# def circle_sector(r, alpha):
#
#     if not isinstance(r, (int, float)) or r <= 0:
#         print('The number must be Int')
#         return None
#
#     if not isinstance(alpha, (int,float)) <= 0:
#         print('the numbers must be Int')
#     return None
#
# S = (math.pi * r ** 2) * alpha / 360
# alpha_degrees = alpha * 180 / math.pi
#
# print(circle_sector())


# 2 Գրել ֆունկցիա, որը․
#    - կստանա արգումենտ արաբական բնական թիվ (0-ից մեծ),
#    - կվերադրձնի այդ թիվը հռոմեական տեսքով,
#    հռոմեական թվերի համարժեքները՝ I-1, V-5, X-10, L-50, C-100, D-500, M-1000,
#    օրինակ՝ 15 -> XV,
#            72 -> LXXII,
#            9 -> IX:

# def convert_to_roman(num):
#
#     if not isinstance(num, int) or num <= 0:
#         return "error :the number not integer"
#
#
#     roman_numerals = {
#         1000: 'M',
#         900: 'CM',
#         500: 'D',
#         400: 'CD',
#         100: 'C',
#         90: 'XC',
#         50: 'L',
#         40: 'XL',
#         10: 'X',
#         9: 'IX',
#         5: 'V',
#         4: 'IV',
#         1: 'I'
#     }
#
#     roman_nums = ""
#
#     for x, y in roman_numerals.items():
#         if num >= x:
#             roman_nums += y
#             num -= x
#     return roman_nums



# print(convert_to_roman())

# 3․
