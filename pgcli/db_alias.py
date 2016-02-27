import ConfigParser
from os.path import expanduser
import os.path
from .config import config_location


class DbAlias(object):

    def __init__(self, params={}):
        self.alias = params.get('alias', None)
        self.user = params.get('user', None)
        self.dbname = params.get('dbname', None)
        self.host = params.get('host', '')
        self.port = params.get('port', '5432')
        self.password = params.get('password', None)

    @classmethod
    def find(cls, alias, alias_file=None):
        alias_file = alias_file or config_location() + 'db_aliases.cfg'

        config = ConfigParser.ConfigParser()
        config.read(alias_file)

        alias_config = {}
        if alias in config.sections():
            alias_config = {'alias': alias}
            alias_config.update(dict(config.items(alias)))

        return cls(alias_config)

    def is_empty(self):
        return self.alias is None
