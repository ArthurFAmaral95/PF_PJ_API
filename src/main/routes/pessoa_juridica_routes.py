from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.main.composer.pessoa_juridica_lister_all_composer import pessoa_juridica_lister_all_composer
from src.main.composer.pessoa_juridica_lister_composer import pessoa_juridica_lister_composer
from src.main.composer.pessoa_juridica_creator_composer import pessoa_juridica_creator_composer
from src.main.composer.pessoa_juridica_balance_getter_composer import pessoa_juridica_balance_getter_composer
from src.main.composer.pessoa_juridica_depositer_composer import pessoa_juridica_depositer_composer
from src.main.composer.pessoa_juridica_withdraw_composer import pessoa_juridica_withdraw_composer
from src.errors.error_handler import handle_errors

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
  try:
    http_request = HttpRequest(body=request.json)
    view = pessoa_juridica_creator_composer()

    http_response = view.handle(http_request=http_request)
    return jsonify(http_response.body), http_response.status_code
  except Exception as exception:
    http_response = handle_errors(exception)
    return jsonify(http_response.body), http_response.status_code

@pessoa_juridica_route_bp.route('/pj/balance/<client_id>', methods=['GET'])
def pessoa_juridica_get_balance(client_id):
  http_request = HttpRequest(param={'client_id': client_id})
  view = pessoa_juridica_balance_getter_composer()

  http_response = view.handle(http_request=http_request)
  return jsonify(http_response.body), http_response.status_code

@pessoa_juridica_route_bp.route('/pj/deposit/<client_id>', methods=['POST'])
def pessoa_juridica_make_deposit(client_id):
  http_request = HttpRequest(body=request.json, param={'client_id': client_id})
  view = pessoa_juridica_depositer_composer()

  http_response = view.handle(http_request=http_request)
  return jsonify(http_response.body), http_response.status_code

@pessoa_juridica_route_bp.route('/pj/withdraw/<client_id>', methods=['POST'])
def pessoa_juridica_make_withdrawal(client_id):
  http_request = HttpRequest(body=request.json, param={'client_id': client_id})
  view = pessoa_juridica_withdraw_composer()

  http_response = view.handle(http_request=http_request)
  return jsonify(http_response.body), http_response.status_code
  