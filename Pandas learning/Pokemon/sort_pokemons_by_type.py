import pandas as pd

pd.set_option("display.max_columns", 14, "display.width", 400)
data = pd.read_csv("pokemon.csv", index_col=False)

possible_type = []
for pokemon_type in data["Type 1"]:
    if pokemon_type not in possible_type:
        possible_type.append(pokemon_type)


for pokemon_type in possible_type:
    pokemons_with_type = data[((data["Type 1"] == pokemon_type) | (data["Type 2"] == pokemon_type)) & ~(data["Name"].str.contains("Mega"))].copy()
    mean_row = pokemons_with_type[["Total","HP","Attack","Defense","Sp. Atk","Sp. Def","Speed"]].mean(axis=0,numeric_only=True)
    mean_row = mean_row.round(2)
    pokemons_with_type = pokemons_with_type.astype("string")
    mean_row = mean_row.astype("string")
    pokemons_with_type = pd.concat([pokemons_with_type, mean_row.to_frame().T],ignore_index=True)
    pokemons_with_type.iloc[-1,0] = "Mean"
    pokemons_with_type.to_csv("Pokemons sorted by type/{0}.csv".format(pokemon_type), index=False)



