from flask import Blueprint
from controllers.jogos_controlles import JogoController

jogo_bp = Blueprint('jogo_bp', __name__)

jogo_bp.route('/jogos', methods=['POST'])(JogoController.cadastrar_jogo)

jogo_bp.route('/jogos', methods=['GET'])(JogoController.listar_todos)

jogo_bp.route('/jogos/<int:id_jogo>', methods=['GET'])(JogoController.buscar_por_id)

jogo_bp.route('/jogos/<int:id_jogo>', methods=['PUT'])(JogoController.atualizar_por_id)