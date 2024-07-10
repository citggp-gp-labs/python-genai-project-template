import csv


def mapper(file) -> dict:
    output = {}

    reader = csv.DictReader(file, delimiter=';')
    for linha in reader:
        ativo = linha['ativo']
        nivel = linha['nivel']
        category_main_name = linha['category_main_name']
        sub_category_name = linha['category_name']
        param_decode = linha['param_decode']

        if len(category_main_name) == 0 or len(sub_category_name) == 0 or ativo == 0:
            continue

        if category_main_name not in output:
            output[category_main_name] = {}
        if sub_category_name not in output[category_main_name]:
            output[category_main_name][sub_category_name] = []

        if nivel == 'subcategoria':
            output[category_main_name][sub_category_name].append(param_decode)
    return output

def mapper_to_str(file) -> dict:
    output = {}

    reader = csv.DictReader(file, delimiter=';')
    for linha in reader:
        ativo = linha['ativo']
        nivel = linha['nivel']
        category_main_name = linha['category_main_name']
        sub_category_name = linha['category_name']
        param_decode = linha['param_decode']

        if len(category_main_name) == 0 or len(sub_category_name) == 0 or ativo == 0:
            continue

        if category_main_name not in output:
            output[category_main_name] = {}
        if sub_category_name not in output[category_main_name]:
            output[category_main_name][sub_category_name] = []

        if nivel == 'subcategoria':
            output[category_main_name][sub_category_name].append(param_decode)
            
    reponse = ""
    
    for category_main_name in list(output):
        reponse += f"Categoria principal: {category_main_name}\n"
        reponse += f"Sub-categorias: "
        for sub_category_name in output[category_main_name]:
            reponse += f"'{sub_category_name}', "
        
        reponse = reponse[:-2]
        reponse += "\n\n"
    
    return reponse