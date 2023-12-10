from client_application.client_application import ClientApplication
from tests.tests import WebServiceTest
from web_service.web_service import WebService


if __name__ == '__main__':
    """ ws = WebService('users', 5)
    print(ws.get_data()) """

    test_web_service = WebServiceTest()
    test_web_service.test_web_service()

    app = ClientApplication()
    app.launch()
