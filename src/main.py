from website import create_app
 
app = create_app()

if __name__ == '__main__': #it makes sure to run the app when it is opened but now when imported or etc.
    app.run(debug=True)

