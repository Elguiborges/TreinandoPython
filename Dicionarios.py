# Fazendo uma lista comum
info = ["Guilherme","Borges","São Paulo"]

# Fazendo uma lista com dicionário
matricula = {"nome":"Guilherme",
             "sobrenome":"Borges",
             "endereço":[{"logradouro":"Av Brig Faria Lima, 301",
                          "bairro":"Pinheiros",
                          "cidade":"São Paulo",
                          "país":"Brasil"}]}

print ("O endereço completo é:",matricula["endereço"])
print ("O bairro é:", matricula["endereço"][0]["bairro"])

print (matricula.keys()) # Retorna apenas as chaves do dicionário
print (matricula.values()) # Retorna apenas os valores do dicionário
print (matricula.items()) # Retorna chaves e valores