from microdot import Microdot

app = Microdot()

@app.route('/')
def index(request):
    return 'Hello, world!'

if __name__ == '__main__':
    app.run(debug=True)