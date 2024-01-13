import cantera as ct 

g = ct.Solution('gri30.yaml')


for i in range(g.n_reactions):
    reaction = g.reaction(i)
    reaction_type = reaction.reaction_type 
    kfi = g.forward_rate_constants[i]
    kri = g.reverse_rate_constants[i]

    print(f' kfi {i + 1}: {kfi}, Tipo: {reaction_type}')
    print(f' kri {i + 1}: {kfi}, Tipo: {reaction_type}')