import pandas as pd

pd.set_option("display.max_columns", 14, "display.width", 400)
data = pd.read_csv("pokemon.csv", index_col=False)

possible_type = []
for type in data["Type 1"]:
    if type not in possible_type:
        possible_type.append(type)


for type in possible_type:
    pokemons_with_type = data[((data["Type 1"] == type) | (data["Type 2"] == type)) & ~(data["Name"].str.contains("Mega"))].copy()
    mean_row = pokemons_with_type[["Total","HP","Attack","Defense","Sp. Atk","Sp. Def","Speed"]].mean(axis=0,numeric_only=True)
    pokemons_with_type = pd.concat([pokemons_with_type, mean_row.to_frame().T],ignore_index=True)
    print(pokemons_with_type)
    pokemons_with_type.to_csv("Pokemons sorted by type/{0}.csv".format(type),index=False)



