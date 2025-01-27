#!/usr/bin/python3

def uniq_add(my_list=[]):
    # suma_unicos = 0

    # for elemento in my_list:
    #     if isinstance(elemento, int):
    #             if my_list.count(elemento) == 1:
    #                 suma_unicos += elemento
    #     else:
    #          pass
    # return suma_unicos
    #!/usr/bin/python3
    sum_elements = 0
    my_list = set(my_list)
    my_list = list(my_list)
    for element in my_list:
        sum_elements += element
    return (sum_elements)
