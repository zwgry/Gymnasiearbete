from my_server import app        # importera "app" från huvudpaketet

if __name__ == '__main__':       # startar servern
    app.run(host='localhost', port=8080, debug=True)
