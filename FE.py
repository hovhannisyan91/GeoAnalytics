
import dash
import dash_core_components as dcc
import dash_html_components as html


app=dash.Dash()

app.css.append_css({"external_url": 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

app.layout=html.Div([


	])	

if __name__=='__main__':
		app.run_server(debug=True)


