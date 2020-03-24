from iolwrapper import IOL
from iolwrapper.authtentication import IolAuthentication
from iolwrapper.http_handler import HttpHandler


def test_sandbox_selection():
    iol_api = IOL(HttpHandler, IolAuthentication)

    assert iol_api.is_sandbox == True

    iol_api = IOL(HttpHandler, IolAuthentication, is_sandbox=False)
    assert iol_api.is_sandbox == False


def test_url_selection():
    iol_api = IOL(HttpHandler, IolAuthentication)
    assert iol_api._http_handler.base_url_api == 'https://api-sandbox.invertironline.com'

    iol_api = IOL(HttpHandler, IolAuthentication, is_sandbox=False)
    assert iol_api._http_handler.base_url_api == 'https://api.invertironline.com'
