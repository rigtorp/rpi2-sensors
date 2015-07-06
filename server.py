import sqlite3
from flask import Flask, g, render_template_string
app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('sensors.db')
    return db

index_tmpl = """
<!doctype html>
<title>Sensors</title>
<body>
<h1>Senors</h1>
<dl>
<dt>Outside Temperature</dt>
<dd>{{ sensors['ot'] }}</dd>
<dt>Outside Humidity</dt>
<dd>{{ sensors['oh'] }}</dd>
<dt>Inside Temperature</dt>
<dd>{{ sensors['it'] }}</dd>
<dt>Inside Humidity</dt>
<dd>{{ sensors['ih'] }}</dd>
<dt>Barometric Pressure</dt>
<dd>{{ sensors['bp'] }}</dd>
<dt>Time</dt>
<dd>{{ ts }} UTC</dd>
</dl>
"""

@app.route('/')
def index():
    db = get_db()
    sensors = db.execute('SELECT * FROM measurements GROUP BY sensor')
    sensors = [x for x in sensors]
    ts = sensors[0][0]
    sensors = dict([(x[1], x[2]) for x in sensors])
    return render_template_string(index_tmpl, sensors=sensors, ts=ts)

if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0')
