import pandas as pd
import os

best_stats = {'Total':(None,0), 'HP':(None,0), 'Attack':(None,0), 'Defense':(None,0), 'Sp. Atk':(None,0), 'Sp. Def':(None,0), 'Speed':(None,0)}

pd.set_option("display.max_columns", 14, "display.width", 400, "display.max_rows", 140)

for type_file in os.listdir("Pokemons sorted by type"):
    pokemons_with_type = pd.read_csv("Pokemons sorted by type/" + type_file, dtype="string")
    pokemons_with_type = pokemons_with_type.fillna("")
    pokemon_type = type_file[:-4]
    print(pokemon_type,":", sep="")
    print(pokemons_with_type.to_string(index=False), "\n\n")
    mean = pokemons_with_type.tail(1)
    for stat, best in best_stats.items():
        if float(mean[stat]) > best[1]:
            best_stats[stat] = (pokemon_type, float(mean[stat]))

print("Best stats:")
for stat, best in best_stats.items():
    print(stat+":",best)

