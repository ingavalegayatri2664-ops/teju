from flask import Flask 
app= Flask('__2nd_Practical__')
@app.route('/')
def home():
    return"Hello from cloud pass!"

if __name__ =='__main__':
    app.run()

