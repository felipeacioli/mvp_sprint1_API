from pydantic import BaseModel
from typing import Optional, List
from model.material import Material



class MaterialSchema(BaseModel):
    """ Define como um novo material a ser inserido deve ser representado
    """
    descricao: str = "CIRCUITO INTEGRADO LM 358"
    quantidade: Optional[int] = 35
    preco: Optional[int] = 35
    grupo: str = "Eletrônico"


class MaterialBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no id do material
    """
    id: Optional[int] = 2

class MaterialBuscaDescricaoSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no id do material
    """
    descricao: str = "Teste"

class ListagemMaterialSchema(BaseModel):
    """ Define como uma listagem de materiais será retornada.
    """
    materiais:List[MaterialSchema]


def apresenta_materiais(materiais: List[Material]):
    """ Retorna uma representação do material seguindo o schema definido em
        MaterialViewSchema.
    """
    result = []
    for material in materiais:
        result.append({
            "descricao": material.descricao,
            "quantidade": material.quantidade,
            "preco": material.preco,
            "grupo": material.grupo,
        })

    return {"materiais": result}

class MaterialViewSchema(BaseModel):
    """ Define como um material será retornado: material.
    """
    id: int = 1
    descricao: str = "CIRCUITO INTEGRADO LM 358"
    quantidade: Optional[int] = 35
    preco: Optional[int] = 35
    grupo: str = "Eletrônico"


class MaterialDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    descricao: str

def apresenta_material(material: Material):
    """ Retorna uma representação do material seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": material.id,
        "descricao": material.descricao,
        "quantidade": material.quantidade,
        "preco": material.preco,
        "grupo": material.grupo,
    }
