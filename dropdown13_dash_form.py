import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,
                external_stylesheets = external_stylesheets)

server = app.server

app.layout = html.Div([
    html.H1('Title'),

    html.Div([
        dcc.Markdown("""        
            * **Data displayed is current as of May 2020**
            * **Contact us if with questions and data needs (see contact form at page bottom).**
            """, style={'paddingBottom': 15,
                        'display': 'inline-block'}),

    ]),

    html.Div([

        dcc.Dropdown(id='country_dd',
                     options=[
                         {'label': 'Austria', 'value': 'austria'},
                         {'label': 'Germany', 'value': 'germany'},
                         {'label': 'Italy', 'value': 'italy'},
                         {'label': 'Slovenia', 'value': 'slovenia'}
                     ],
                     value='austria'),

        html.Div(id='country_dd_output'),

    ], style={'width': '200px',
              'float': 'center',
              'display': 'block'}),

    html.Form([
            html.H6('Contact form'),
            html.P('We only respond to company or university email addresses - no Gmail etc.', style={'paddingTop': 5}),
            dcc.Input(id='name', type='text', placeholder='Name', required=True),
            dcc.Input(id='email', type='email', placeholder='Email', required=True),
            dcc.Input(id='org', type='email', placeholder='Organization', required=True),
            html.P('What best describes your organization?', style={'paddingTop': 5}),
            dcc.Dropdown(id='contact_type_dd', options=[
                {'label': 'Government', 'value': 'government'},
                {'label': 'Tourism office', 'value': 'dmo'},
                {'label': 'Tourism consulting', 'value': 'consultant'},
                {'label': 'Academia - faculty', 'value': 'faculty'},
                {'label': 'Academia - student', 'value': 'student'}
            ]),
            html.P('What are you looking for? Was suchen Sie?', style={'paddingTop': 5}),
            dcc.Textarea(id='interest',
                         value='Please write here. English or Deutsch works for us!!! \nBriefly tell us what you are looking for.',
                         style={'display': 'inline-block',
                                'width': '100%',
                                'height': 300}),
            html.Button('Submit', id='contact_button', n_clicks=0)
        ], style={'paddingTop': 15,
                  'display': 'inline-block',
                  'float': 'left'})
])

# country dropdown
@app.callback(Output('country_dd_output', 'children'),
              [Input('country_dd', 'value')])
def update_level_dd(value):
    return 'You selected {}'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)
