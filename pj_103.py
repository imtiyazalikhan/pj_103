from typing import Sized
import pandas as pd
import plotly.express as px

df = pd.read_csv(r"E:\imtiyaz's project folder\data.csv")
fig = px.line(df, x="date", y="cases",color="country",)
                  
fig.show()
