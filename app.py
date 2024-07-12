from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Material
from logger import logger
from schemas import *
from flask_cors import CORS


info = Info(title="API para cadastrar materiais e fazer controle de estoque", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Documentação em Swagger.")
material_tag = Tag(name="Material", description="Adição, visualização e remoção de materiais à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi/swagger#')


@app.post('/material', tags=[material_tag],
          responses={"200": MaterialViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_material(form: MaterialSchema):
    """Adiciona um novo Material à base de dados

    Retorna uma representação dos materias e comentários associados.
    """
    material = Material(
        descricao=form.descricao,
        quantidade=form.quantidade,
        preco=form.preco,
        grupo=form.grupo)
        #data_insercao=form.data_insercao)
    logger.warning(f"Adicionando material que foi especificado como: '{material.descricao}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando material
        session.add(material)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado material que foi especificado como: '{material.descricao}'")
        return apresenta_material(material), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Material com a mesma descrição já salvo na base :/"
        logger.warning(f"Erro ao adicionar material '{material.descricao}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar material '{material.descricao}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/materiais', tags=[material_tag],
         responses={"200": ListagemMaterialSchema, "404": ErrorSchema})
def get_materiais():
    """Faz a busca por todos os materiais cadastrados

    Retorna uma representação da listagem de materias.
    """
    logger.debug(f"Coletando materiais ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    materiais = session.query(Material).all()

    if not materiais:
        # se não há material cadastrado
        return {"materiais": []}, 200
    else:
        logger.debug(f"%d Suprimentos econtrados" % len(materiais))
        # retorna a representação de material
        print(materiais)
        return apresenta_materiais(materiais), 200


@app.get('/material', tags=[material_tag],
         responses={"200": MaterialViewSchema, "404": ErrorSchema})
def get_material(query: MaterialBuscaSchema):
    """Faz a busca por um Material a partir do id do material

    Retorna uma representação dos materias.
    """
    material_id = query.id
    logger.debug(f"Coletando dados sobre material #{material_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    material = session.query(Material).filter(Material.id == material_id).first()

    if not material:
        # se o produto não foi encontrado
        error_msg = "Material não encontrado na base :/"
        logger.warning(f"Erro ao buscar material '{material_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Material econtrado: '{material.descricao}'")
        # retorna a representação de material
        return apresenta_material(material), 200


@app.delete('/material', tags=[material_tag],
            responses={"200": MaterialDelSchema, "404": ErrorSchema})
def del_produto(query: MaterialBuscaDescricaoSchema):
    """Deleta um material a partir da descrição do material informado

    Retorna uma mensagem de confirmação da remoção.
    """
    material_descricao = unquote(unquote(query.descricao))
    print(material_descricao)
    logger.debug(f"Deletando dados sobre o material #{material_descricao}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Material).filter(Material.descricao == material_descricao).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado material #{material_descricao}")
        return {"mesage": "Material removido", "id": material_descricao}
    else:
        # se o material não foi encontrado
        error_msg = "Material não encontrado na base :/"
        logger.warning(f"Erro ao deletar material #'{material_descricao}', {error_msg}")
        return {"mesage": error_msg}, 404