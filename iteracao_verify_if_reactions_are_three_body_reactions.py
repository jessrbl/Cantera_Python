import cantera as ct

# Carregando o arquivo de solução
g = ct.Solution('gri30.yaml')


for i in range(g.n_reactions):
    reaction = g.reaction(i)
    reaction_type = reaction.reaction_type 
    print(f"Reação {i + 1}: {reaction.equation}, Tipo: {reaction_type}")

    if reaction_type == 'three-body-Arrhenius':
        print(f"This is a Three-Body Reaction")
    elif reaction_type == 'Arrhenius':
        print(f"This is an Arrhenius Reaction") 
    else:
        print("This is a falloff-troe Reaction")       


