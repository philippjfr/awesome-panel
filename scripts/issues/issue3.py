import pandas as pd
import plotly.express as px

import panel as pn

data = {
    "Day": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",],
    "Orders": [15539, 21345, 18483, 24003, 23489, 24092, 12034],
}
dataframe = pd.DataFrame(data)
app = pn.Column(dataframe, sizing_mode="stretch_width", background="gray")
app.servable()
