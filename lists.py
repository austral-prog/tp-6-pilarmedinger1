
def remove_elements(list_to_remove_elements):
    indices_a_remover = [0, 4, 5]
    nueva_lista = [elemento for i, elemento in enumerate(list_to_remove_elements) if i not in indices_a_remover]
    return nueva_lista

def add_elements(list_to_add_elements):
    nueva_lista = ['Pink'] + list_to_add_elements + ['Yellow']
    return nueva_lista


def is_empty(list_to_check):
    return len(list_to_check) == 0


def check_lists(lista1, lista2):
    if len(lista1) >= 3 and len(lista2) >= 3:
        return lista1[2] == lista2[2]
    return False

def list_of_lists(list_of_lists_to_modify):
    nueva_lista = []
    nueva_lista.append(list_of_lists_to_modify[0][:2])
    nueva_lista.append(list_of_lists_to_modify[1][1:4])
    nueva_lista.append(list_of_lists_to_modify[2][-2:])
    return nueva_lista
