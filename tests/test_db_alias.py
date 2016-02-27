import os
import pytest
from pgcli.db_alias import DbAlias

@pytest.fixture
def alias_cfg(tmpdir):
    return tmpdir.mkdir('config').join('db_alias.cfg')

@pytest.fixture
def alias_cfg_with_content(alias_cfg):
    content = """[my-db]
dbname: DBSTUFFS
user: super_cool_user
host: amazonaws.com
password: ezpz
port: 1234
dsn: pgsql:host=amazonaws.com;port=1234;dbname=DBSTUFFS;user=super_cool_user;password=ezpz
"""

    alias_cfg.write(content)
    return alias_cfg

def test_empty_alias(alias_cfg):
    alias = DbAlias.find('my-db', alias_cfg.strpath)
    assert alias.is_empty()

def test_alias_not_empty(alias_cfg):
    alias_cfg.write('[my-db]')
    alias = DbAlias.find('my-db', alias_cfg.strpath)
    assert not alias.is_empty()

def test_alias_has_correct_alias_name(alias_cfg):
    alias_cfg.write('[my-db]')
    alias = DbAlias.find('my-db', alias_cfg.strpath)
    assert alias.alias == 'my-db'

def test_alias_has_correct_db_name(alias_cfg_with_content):
    alias = DbAlias.find('my-db', alias_cfg_with_content.strpath)
    assert alias.dbname == 'DBSTUFFS'

def test_alias_has_correct_user(alias_cfg_with_content):
    alias = DbAlias.find('my-db', alias_cfg_with_content.strpath)
    assert alias.user == 'super_cool_user'

def test_alias_has_correct_password(alias_cfg_with_content):
    alias = DbAlias.find('my-db', alias_cfg_with_content.strpath)
    assert alias.password == 'ezpz'

def test_alias_has_correct_host(alias_cfg_with_content):
    alias = DbAlias.find('my-db', alias_cfg_with_content.strpath)
    assert alias.host == 'amazonaws.com'

def test_default_alias_host(alias_cfg):
    alias_cfg.write('[my-db]')
    alias = DbAlias.find('my-db', alias_cfg.strpath)
    assert alias.host == ''

def test_alias_has_correct_port(alias_cfg_with_content):
    alias = DbAlias.find('my-db', alias_cfg_with_content.strpath)
    assert alias.port == '1234'

def test_default_alias_port(alias_cfg):
    alias_cfg.write('[my-db]')
    alias = DbAlias.find('my-db', alias_cfg.strpath)
    assert alias.port == '5432'
