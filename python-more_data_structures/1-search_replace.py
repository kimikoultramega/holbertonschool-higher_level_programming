#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list: # iteramos sobre my list
        if i == search: # cuando i sea igual a search
            new_list.append(replace) #a gregamos a new_list en el lugar i a replace
        else: # de lo contrario agregamos a new list i
            new_list.append(i)
    return(new_list)
