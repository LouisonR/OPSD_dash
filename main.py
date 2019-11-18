from server import app

if __name__ == '__main__':
    print('Flask starting server...')
    app.run_server(
        host='127.0.0.1',
        port=8000,
        debug=True
    )
