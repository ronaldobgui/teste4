from flask import Flask, request
app = Flask(__name__)

@app.get('/search')
def hello():
  input = request.args.get('input');
  return f'Buscando por: "{input}"'

app.run()