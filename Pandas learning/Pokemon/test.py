import pandas as pd

pd.set_option("display.max_columns", 14, "display.width", 400)
data = pd.read_csv("pokemon.csv", index_col=False)

possible_type = []
for type in data["Type 1"]:
    if type not in possible_type:
        possible_type.append(type)


for type in possible_type:
    dic = {}
    pokemons_with_type = data[((data["Type 1"] == type) | (data["Type 2"] == type)) & ~(data["Name"].str.contains("Mega"))].copy()
    print(pokemons_with_type)
    for stat in pokemons_with_type.drop(["#"], axis=1).select_dtypes(include="number"):
        dic[stat] = pokemons_with_type[stat].mean()
    pokemons_with_type.loc["mean"] = pokemons_with_type.mean(numeric_only=True)
    print(pokemons_with_type)
#kurwa mać jebany pandas nie chce działać



