from unittest.mock import Mock

from libpythonpro import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
         'login': 'user_name', 'id': 13154, 'node_id': 'M5777777777777zNTAwMTU0',
         'avatar_url': 'https://avatars1.githubusercontent.com/u/XXXXXXXXXXXX=4',
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('user_name')
    assert 'https://avatars1.githubusercontent.com/u/XXXXXXXXXXXX=4' == url
