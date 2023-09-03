import json
import yaml
import pandas as pd
from arcticdb import Arctic

with open('typeIDs.yaml', 'r', encoding='utf-8') as file:
    data = yaml.safe_load(file)

with open('output.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, separators=(',', ': '))

df = pd.read_json(json.dumps(data))


rows_to_print = [2, 17]
df_TypeID = (df.iloc[rows_to_print])

print(df_TypeID)

ac = Arctic("lmdb://C:\ArcticDB")

lib = ac["market_data"]
lib.write("type_id",df_TypeID)