import pandas as pd
from sqlite_to_pyscript import Person


df_dict = {
    'id_num': [9999],
    'first': ['Ben'],
    'last': ['Carver'],
    'age': [21]
}

df = pd.DataFrame(df_dict)
df.set_index('id_num', inplace=True)


for key in df.itertuples():
    new_person = Person(key[0], key[1], key[2], key[3])
    new_person.insert_person()

