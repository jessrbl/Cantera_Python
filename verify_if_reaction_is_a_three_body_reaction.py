import cantera as ct

# Carregando o arquivo de solução
g = ct.Solution('gri30.yaml')

ct.ThirdBody
# Obtendo a primeira reação

reaction = g.reaction(2)
print(f"Reaction: {reaction}")

# Verificando o tipo de reação
reaction_type = reaction.reaction_type 
print(f"Reaction type: {reaction_type}")

# Verificando se é uma reação de terceiro corpo
if reaction_type == 'three-body-Arrhenius':
    print(f"  This is a Three-Body Reaction.")
    third_body_name = reaction.third_body_name
    default = ct.ThirdBody.default_efficiency
    print(default)
    print(f"  Name of the third body: {third_body_name}")

else:
    print("  This is not a Three-Body Reaction.")