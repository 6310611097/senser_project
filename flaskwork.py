from flask import Flask, render_template
app = Flask(__name__)

db = [
    {
        "temp": "", # "" = the input_data, "temperature", to {{post.temp}} in template 
        "humi": "", # "" = the input_data, "Humidity", to {{post.humi}} in template 
        "light": "", # "" = the input_data, "Light Intensive", to {{post.light}} in template 
    }
]

@app.route("/")
def homepage(): # funtion to render page.html 
    return render_template("page.html", posts= db)

if __name__ == '__main__':
    app.run(debug= True) # for instant reloading website