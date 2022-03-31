import time
import json
from loguru import logger
from service.constants import mensagens
import pandas as pd
import numpy as np
import math

class Bhaskara():

    def _init_(self):
        logger.debug(mensagens.INICIO_LOAD_SERVICO)
        self.load_servico()

    def load_servico(self):

        logger.debug(mensagens.FIM_LOAD_SERVICO)


    def executar_rest(self, texts):
        response = {}

        logger.debug(mensagens.INICIO_SERVICO)

        response = self.bhaskara(texts)

        logger.debug(response)

        return response


    def bhaskara(self, texts):

        a = texts["a"][0]
        logger.debug(a)

        b = texts["b"][0]
        logger.debug(b)
        
        c = texts["c"][0]
        logger.debug(type(c))

        delta=b**2-4*a*c

        logger.debug(delta)

        if (delta < 0):
            resposta = "Não existe raízes possiveis."
            return resposta
        elif (delta == 0):
            response = (-b+math.sqrt(delta))/2*a
            response = str(response)     
            return response
        else:
            x1=-b+math.sqrt(delta)/2*a
            x2=-b-math.sqrt(delta)/2*a   
            
            resposta = "Valor de X1: " + str(round(x1, 2)) + ", e o valor de X2: " + str (round(x2, 2))

        return resposta