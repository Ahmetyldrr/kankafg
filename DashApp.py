
from dash import Dash, dcc, html,dash_table
from dash.dependencies import Input, Output
from datetime import datetime
from datetime import date
from BetFikstur import Fikstür
import pandas as pd

s='2022-06-17'
e='2022-06-18'


df1 = Fikstür(s,e)

df = df1[['date','dateTime','league.country.name','league.name','stageName',
'localTeam.name','visitorTeam.name','localTeamPosition','visitorTeamPosition',
'prediction','bestOddProbability','predictionOddValue','localTeamScore',
'visitorTeamScore','minute','timeStatus','odd1','oddx','odd2','odd1x',
'odd12','oddx2','oddGoal','oddNoGoal','oddOver25','oddUnder25']]

app = Dash(__name__)

server = app.server

app.layout = html.Div([
    dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=date(2015, 1, 1),
        max_date_allowed=date(2025, 1, 1),
        initial_visible_month=datetime.today(),
        end_date=datetime.today()
    ),
 
     dash_table.DataTable(
        id='tbl',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),  # the contents of the table
       # editable=True,              # allow editing of data inside all cells
        filter_action="native",     # allow filtering of data by user ('native') or not ('none')
        sort_action="native",       # enables data to be sorted per-column by user or not ('none')
        sort_mode="single",         # sort across 'multi' or 'single' columns
        column_selectable="multi",  # allow users to select 'multi' or 'single' columns
        row_selectable="multi",     # allow users to select 'multi' or 'single' rows
        row_deletable=True,         # choose if user can delete a row (True) or not (False)
        selected_columns=[],        # ids of columns that user selects
        selected_rows=[],           # indices of rows that user selects
        page_action="native",       # all data is passed to the table up-front or not ('none')
        page_current=0,             # page number that user is on
        page_size=15,                # number of rows visible per page
         
    )
])



@app.callback(
    Output('tbl', 'data'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'))

def update_data(start_date, end_date):
   
    df = Fikstür(start_date,end_date)

    return df.to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)