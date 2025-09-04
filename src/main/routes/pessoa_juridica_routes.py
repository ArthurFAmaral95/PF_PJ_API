from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.main.composer.pessoa_juridica_lister_all_composer import pessoa_juridica_lister_all_composer

pessoa_juridica_route_bp = Blueprint('pessoa_juridica_routes', __name__)

@pessoa_juridica_route_bp.route('/pj', methods=['GET'])
def list_all_pf():
  http_request = HttpRequest()
  view = pessoa_juridica_lister_all_composer()

  http_response = view.handle(http_request=http_request)

  return jsonify(http_response.body), http_response.status_code
