#!/usr/bin/env python

"""
modificado
"""

from lib.core.data import logger
from lib.core.exception import SqlmapUnsupportedFeatureException
from plugins.generic.enumeration import Enumeration as GenericEnumeration

class Enumeration(GenericEnumeration):
    def getCurrentUser(self):
        warnMsg = "no SQLite não é possível enumerar o usuário atual"
        logger.warning(warnMsg)

    def getCurrentDb(self):
        warnMsg = "no SQLite não é possível obter o nome do banco de dados atual"
        logger.warning(warnMsg)

    def isDba(self, user=None):
        warnMsg = "no SQLite o usuário atual tem todos os privilégios"
        logger.warning(warnMsg)

        return True

    def getUsers(self):
        warnMsg = "no SQLite não é possível enumerar os usuários"
        logger.warning(warnMsg)

        return []

    def getPasswordHashes(self):
        warnMsg = "no SQLite não é possível enumerar os hashes de senha do usuário"
        logger.warning(warnMsg)

        return {}

    def getPrivileges(self, *args, **kwargs):
        warnMsg = "no SQLite não é possível enumerar os privilégios do usuário"
        logger.warning(warnMsg)

        return {}

    def getDbs(self):
        warnMsg = "no SQLite não é possível enumerar bancos de dados (usarem apenas '--tables')"
        logger.warning(warnMsg)

        return []

    def searchDb(self):
        warnMsg = "no SQLite não é possível pesquisar bancos de dados"
        logger.warning(warnMsg)

        return []

    def searchColumn(self):
        errMsg = "no SQLite não é possível pesquisar colunas"
        raise SqlmapUnsupportedFeatureException(errMsg)

    def getHostname(self):
        warnMsg = "no SQLite não é possível enumerar o hostname"
        logger.warning(warnMsg)

    def getStatements(self):
        warnMsg = "no SQLite não é possível enumerar as instruções SQL"
        logger.warning(warnMsg)

        return []
