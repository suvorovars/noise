def start_flask():
    from app import app
    app.app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    start_flask()