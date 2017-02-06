import gettemp
import pressure
from flask import Flask, render_template

temp=gettemp.temp
humidity=gettemp.humidity
p=pressure.Weather()
press=p.messure_pressure

#@app.template_filter('temp')
#def showTemp():
#    temp = gettemp()
#    return temp

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html', temp=temp, press=p, humidity=humidity)

if __name__ == "__main__":
    app.run(host='192.168.1.81')
