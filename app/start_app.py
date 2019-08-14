from sanic import Sanic
from sanic.response import json

import default_setting
from models.create_db import create_tables

app = Sanic('my_sanic_app')
app.config.from_object(default_setting)

@app.route("/")
async def test(request):
    return json({"hello": "docker"})

if __name__ == "__main__":
    create_tables()
    app.run(host="0.0.0.0", port=8010, debug=True)
