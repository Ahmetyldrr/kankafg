
from dash import Dash, dcc, html,dash_table
from dash.dependencies import Input, Output
from datetime import datetime,timedelta
import dash_bootstrap_components as dbc
from datetime import date
from BetFikstur import Fikstür

presentday = datetime.today()
yarın = presentday + timedelta(1)
s=datetime.now().strftime('%Y-%m-%d')
e=yarın.strftime('%Y-%m-%d')

df = Fikstür(s,e)

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],)

server = app.server

app.layout = html.Div([





    dcc.DatePickerRange(

        id='my-date-picker-range',
        min_date_allowed=date(2015, 1, 1),
        max_date_allowed=date(2025, 1, 1),
        initial_visible_month=datetime.today().strftime("%Y-%m-%d"),
        start_date=s,
        end_date=e


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
        selected_columns=[],        # ids of columns that user selects
        selected_rows=[],           # indices of rows that user selects
        page_action="native",       # all data is passed to the table up-front or not ('none')
        page_current=0,             # page number that user is on
        page_size=100,

        
    
      style_cell = {
                'font_size': '13px',
                'text_align': 'left'
            },
        
            style_data={
        'color': 'black',
        'backgroundColor': 'white'
    },
    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(220, 220, 230)',
        },

        
    ],
    style_header={

        'backgroundColor': 'rgb(210, 210, 210)',
        'color': 'black',
        'fontWeight': 'bold'
    }
         
    ),
     
 
   



])


@app.callback(
    Output('tbl', 'data'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'),
    prevent_initial_call=True,
  
   )

def update_data(start_date, end_date):

    df = Fikstür(start_date,end_date)
    
    return df.to_dict('records')

if __name__ == '__main__':
    app.run_server(debug=True)
