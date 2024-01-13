# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, separator=','):
    _list1=participants_first_group.split(separator)
    _list2 = participants_second_group.split(separator)
    common_list=set(_list1).intersection(_list2)
    list(common_list).sort()
    return list(common_list)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group,participants_second_group,'|'))