# 1.Գրել ծրագիր, որը․
#    - կունենա անուններից կազմված list,
#    - հերթով կտպի այն անունները, որոնց երկարությունը 5-ից մեծ չէ,
#    - ամեն անունը տպելուց հետո հաջորդ անունը կտպի 2 վայրկյան հետո

# import time
# name = ['ani','aram','armen','gor','karlen','karen']
# for name in name:
#     if len(name) <= 5:
#         time.sleep(2)
#         print(name)


# 2. Գրել ֆունկցիա, որը․
#    - կունենա մեկ արգումենտ, որը կլինի դրական ամբողջ թիվ,
#    - եթե թվի թվանշանների քանակը զույգ է, կստուգի արդյոք թվի առաջին կեսի թվանշանների գումարը հավասար է երկրորդ կեսի թվանշանների գումարին, թե ոչ,
#    - եթե թվի թվանշանների քանակը կենտ է, կստուգի նախորդ պայմանի ճշտությունը, ապա կստուգի նաև մեջտեղի թվանշանի զույգ և կենտ լինելը,
#      եթե զույգ է, կտպի True, եթե կենտ՝ False,
#    օրինակ՝ 1238 -> False, քանի որ 1+2 != 3+8
#            1845 -> True, քանի որ 1+8 = 4+5
#            18545 -> False, քանի որ 1+8 = 4+5 և 5-կենտ է,
#            48257 -> True, քանի որ 4+8 = 5+7 և 2-զույգ է։

#

# def check_number(number):
#
#     if not isinstance(number, int) or number <= 0:
#         print("Խնդրում ենք մուտքագրել դրական ամբողջ թիվ։")
#         return None
#
#     num_str = str(number)
#     length = len(num_str)
#
#     def sum_digits(s):
#         return sum(int(digit) for digit in s)
#
#     if length % 2 == 0:
#         half_length = length // 2
#         first_half_sum = sum_digits(num_str[:half_length])
#         second_half_sum = sum_digits(num_str[half_length:])
#         return first_half_sum == second_half_sum
#     else:
#         half_length = length // 2
#         first_half_sum = sum_digits(num_str[:half_length])
#         second_half_sum = sum_digits(num_str[half_length + 1:])
#         middle_digit = int(num_str[half_length])
#
#         sums_equal = (first_half_sum == second_half_sum)
#
#         if sums_equal:
#             return middle_digit % 2 == 0
#         else:
#             return False
#
# print(check_number(1238))
# print(check_number(1845))
# print(check_number(18545))
# print(check_number(48257))
# 3․ Գրել պարային զույգեր կազմելու ծրագիր, որը․
#    - կունենա երկու անունների list, list-երի երկարությունները կարող են տարբեր լինել,
#    օրինակ՝ girls = ['Gohar', 'Ani', 'Tatev']
#            boys = ['Gor', 'Vahe', 'Vardan', 'Karen', 'Ashot']
#    - պատահականության սկզբունքով կտպի պարային զույգեր list-երից
#      փոքրագույն երկարություն ունեցողի քանակությամբ (անունները չպետք է կրկնվեն),
#    տվյալ օրինակի դեպքում կտպի՝ Gohar - Ashot
#                                Ani - Gor
#                                Tatev - Karen։

# girls = ['Gohar', 'Ani', 'Tatev']
# boys = ['Gor', 'Vahe', 'Vardan', 'Karen', 'Ashot']
#
# def dance_group(girl,boys):
#     erkarutyun =
#

