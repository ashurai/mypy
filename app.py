from connexion.resolver import RestyResolver
import connexion

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='swagger/')
    app.add_api('api_conf.yml', swagger_ui= True, resolver=RestyResolver('api'))
    app.run(port=9080, debug=True)