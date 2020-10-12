from unittest.mock import Mock

import pytest

from libpythonpro import github_api


@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars1.githubusercontent.com/u/XXXXXXXXXXXX=4'
    resp_mock.json.return_value = {
         'login': 'user_name', 'id': 13154, 'node_id': 'M5777777777777zNTAwMTU0',
         'avatar_url': url
    }
    resp_original = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.requests.get = resp_original


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('renzo')
    assert avatar_url == url


def test_buscar_avatar_url():
    url = github_api.buscar_avatar('renzon')
    assert 'https://avatars3.githubusercontent.com/u/3457115?v=4' == url
