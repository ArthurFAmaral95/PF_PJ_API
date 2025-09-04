from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.main.composer.pessoa_juridica_lister_all_composer import pessoa_juridica_lister_all_composer
from src.main.composer.pessoa_juridica_lister_composer import pessoa_juridica_lister_composer
from src.main.composer.pessoa_juridica_creator_composer import pessoa_juridica_creator_composer

pessoa_juridica_route_bp = Blueprint('pessoa_juridica_routes', __name__)

@pessoa_juridica_route_bp.route('/pj', methods=['GET'])
def list_all_pj():
  http_request = HttpRequest()
  view = pessoa_juridica_lister_all_composer()

  http_response = view.handle(http_request=http_request)

  return jsonify(http_response.body), http_response.status_code

@pessoa_juridica_route_bp.route('/pj/<client_id>', methods=['GET'])
def list_pessoa_juridica(client_id):
  http_request = HttpRequest(param={'client_id': client_id})
  view = pessoa_juridica_lister_composer()

  http_response = view.handle(http_request=http_request)
  return jsonify(http_response.body), http_response.status_code

@pessoa_juridica_route_bp.route('/pj', methods=['POST'])
def create_pessoa_juridica():
  http_request = HttpRequest(body=request.json)
  view = pessoa_juridica_creator_composer()

  http_response = view.handle(http_request=http_request)
  return jsonify(http_response.body), http_response.status_code
  