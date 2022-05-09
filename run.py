from venv import create
from blogsite import create_app

#This is where you pass unique configuration arguments, however it has default config values
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)