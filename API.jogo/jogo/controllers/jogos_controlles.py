from flask import jsonify, request
from models.jogos_models import banco_jogos, Jogo

class JogoController:
    
    @staticmethod
    def cadastrar_jogo():
        dados = request.get_json()
        
        campos_obrigatorios = ["titulo", "genero", "desenvolvedor", "plataforma"]
        if not dados or not all(campo in dados for campo in campos_obrigatorios):
            return jsonify({"erro": "Todos os campos (titulo, genero, desenvolvedor, plataforma) são obrigatórios"}), 400

        novo_jogo = Jogo(
            titulo=dados["titulo"],
            genero=dados["genero"],
            desenvolvedor=dados["desenvolvedor"],
            plataforma=dados["plataforma"]
        )
        
        banco_jogos.append(novo_jogo)
        return jsonify({
            "mensagem": "Jogo cadastrado com sucesso!",
            "jogo": novo_jogo.to_dict()
        }), 201

    @staticmethod
    def listar_todos():
        jogos_dict = [jogo.to_dict() for jogo in banco_jogos]
        return jsonify(jogos_dict), 200

    @staticmethod
    def buscar_por_id(id_jogo):
        jogo = next((j for j in banco_jogos if j.id == id_jogo), None)
        
        if jogo:
            return jsonify(jogo.to_dict()), 200
        else:
            return jsonify({"erro": f"Jogo com ID {id_jogo} não foi encontrado."}), 404

    @staticmethod
    def atualizar_por_id(id_jogo):
        dados = request.get_json()
        jogo = next((j for j in banco_jogos if j.id == id_jogo), None)
        
        if not jogo:
            return jsonify({"erro": f"Jogo com ID {id_jogo} não foi alterado pois não foi encontrado."}), 404

        jogo.titulo = dados.get("titulo", jogo.titulo)
        jogo.genero = dados.get("genero", jogo.genero)
        jogo.desenvolvedor = dados.get("desenvolvedor", jogo.desenvolvedor)
        jogo.plataforma = dados.get("plataforma", jogo.plataforma)

        return jsonify({
            "mensagem": f"Jogo com ID {id_jogo} alterado com sucesso!",
            "jogo": jogo.to_dict()
        }), 200

    @staticmethod
    def excluir_por_id(id_jogo):
        # Procura o jogo na lista
        jogo = next((j for j in banco_jogos if j.id == id_jogo), None)
        
        if not jogo:
            return jsonify({"erro": f"Jogo com ID {id_jogo} não foi encontrado para exclusão."}), 404

        banco_jogos.remove(jogo)
        
        return jsonify({
            "mensagem": f"Jogo com ID {id_jogo} excluído com sucesso!"
        }), 200