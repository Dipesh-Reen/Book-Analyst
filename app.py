from flask import Flask, request, jsonify
from google_api_connection import get_volumes, get_volume_info

app = Flask(__name__)

@app.get("/volumes")
def all_volumes():
    return get_volumes(request.args['q'])

@app.get("/volumes/<volume_id>")
def volume_info(volume_id: str) -> str:
    return get_volume_info(volume_id=volume_id)['volumeInfo']

