import cantera as ct
import numpy as np

g = ct.Solution('gri30.yaml')
species_names = g.species_names
number_of_species = len(species_names)
target_species = g.selected_species = ['CH4']
print(target_species)
reaction_equations = g.reaction_equations() # cria uma lista com todas as equações das reações
number_of_reactions = len(reaction_equations)
#print(number_of_reactions)
#print(number_of_species)
# Supondo que 'g' seja um objeto Kinetics ou Solution
#second_reaction = g.reaction(1)  # A segunda reação (índice 1)
#print(second_reaction)


# Iterando sobre as reações
for i in range(g.n_reactions):
    reaction = g.reaction(i)
    print(f"Reação {i + 1}: {reaction.equation}")


# Iterando sobre as espécies
for j in range(g.n_species):
    species = g.species(j)
    print(f"Espécie {j + 1}: {species.name}")

""""

def calculate_direct_interaction_coefficient(g, target_species, species_names):
    length_number_of_species = len(species_names)
    interaction_coefficients = np.zeros(length_number_of_species)

    for j, species in enumerate(g.species()):
        if species.name != target_species:
            denominator = 0  # Inicia o denominador para cada espécie

            for i, reaction in enumerate(g.reactions()):
                delta_Bi = 1 if (species in reaction.reactants) or (species in reaction.products) else 0

                # Obtém os índices da espécie e da reação
                species_index = g.kinetics_species_index(species.name)

                # Lida com diferentes tipos de reações
                if isinstance(reaction, ct.ThreeBodyReaction):
                    stoichiometric_coefficient = 1 if species in reaction.products else 0
                elif isinstance(reaction, ct.ElementaryReaction):
                    stoichiometric_coefficient = reaction.net_stoich_coeffs[species_index]
                else:
                    stoichiometric_coefficient = 0  # Adicione casos adicionais conforme necessário

                overall_rate = g.net_rates_of_progress[i] * stoichiometric_coefficient
                interaction_coefficients[j] += abs(overall_rate) * delta_Bi

                # Adicione instruções de impressão para depuração
                print(f"Species: {species.name}, Reaction: {reaction.equation}, Stoichiometric Coefficient: {stoichiometric_coefficient}, Overall Rate: {overall_rate}, Delta Bi: {delta_Bi}")
                
                # Adicione instruções de impressão para investigar o denominador
                print(f"Denominator: {denominator}")

                # Adicione instruções de impressão para verificar o delta_Bi
                print(f"Delta Bi: {delta_Bi}")

                # Adicione instruções de impressão para verificar os reactantes e produtos
                print(f"Reactants: {reaction.reactants}")
                print(f"Products: {reaction.products}")

                # Adicione instruções de impressão para verificar o denominador antes da divisão
                print(f"Final Denominator (before division): {denominator}")

                # Acumula o termo no denominador
                denominator += abs(overall_rate)

            # Verifica se o denominador é maior que zero antes de realizar a divisão
            if denominator > 0:
                interaction_coefficients[j] /= denominator

    return interaction_coefficients

# Exemplo de uso
interaction_coefficients = calculate_direct_interaction_coefficient(g, target_species, species_names)
print("Matriz de Coeficientes de Interação:")
print(interaction_coefficients)

"""