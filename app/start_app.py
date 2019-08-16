from sanic import Sanic
from sanic.response import json
from sanic_openapi import swagger_blueprint, doc

import default_setting
from models.create_db import create_tables
from resources.users import user_bp


app = Sanic('my_sanic_app')
app.config.from_object(default_setting)

app.blueprint(swagger_blueprint)
app.blueprint(user_bp)


@app.route("/")
@doc.exclude(True)
async def test(request):
    return json({"hello": "docker"})

if __name__ == "__main__":
    create_tables()
    app.run(host="0.0.0.0", port=8010, debug=True)
