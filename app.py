import os

from flask import Flask, request


def make_app():
    app = Flask(__name__)

    @app.route('/div')
    def div():
        divisor = request.args.get('divisor', type=int)
        dividend = request.args.get('dividend', type=int)

        return str(divisor/dividend)

    return app

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app = make_app()

    app.run(host='0.0.0.0', port=port)
