from app import create_app

app = create_app()


@app.route('/hello/')
def hi():
    headers = {
        'content-type': 'text/plain',
        'location': 'http://www.bing.com'
    }
    # response = make_response('<html></html>', 301)
    # response.headers = headers
    # return response
    return 'hello', 301, headers
    # 本质上就是返回一个元组，第一个是返回的内容，第二个是状态码，第三个是headers
    # flask会自动重组上面的部分


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
