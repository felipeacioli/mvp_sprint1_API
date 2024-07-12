from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base


class Material(Base):
    __tablename__ = 'material'

    id = Column("id_material", Integer, primary_key=True)
    descricao = Column(String(140), unique=True)
    quantidade = Column(Integer)
    preco = Column(Integer)
    grupo = Column(String(140), unique=False)
    data_insercao = Column(DateTime, default=datetime.now())

    

    def __init__(self, descricao:str, quantidade:int, preco:int, grupo:str, 
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Material

        Arguments:
            descricao: descrição do material.
            quantidade: quantidade dos suprimentos em estoque
            preco: preco do produto
            grupo: categoria a qual o material pertence
            data_insercao: data de quando o maaterial foi inserido à base
        """
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco = preco
        self.grupo = grupo
        self.data_insercao = data_insercao 

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao