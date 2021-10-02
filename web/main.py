"""
网站

@author  : zhouhuajian
@version : v1.0
"""

from flask import Flask, render_template, request, session

# Flask Web应用
web = Flask(__name__)
web.env = 'development'
web.debug = True
# 密钥 用于session加密
web.secret_key = '!@#$%^&*()'


@web.route('/')
def index():
    """首页"""
    return render_template('index.html')


@web.route('/api/login', methods=['POST'])
def api_login():
    """登录接口"""
    # 结果
    result = {'status': 1, 'code': 0, 'message': '登录成功', 'data': {}}
    # 用户名、密码
    user = request.values.get('user').strip()
    pwd = request.values.get('pwd').strip()
    # 账号为空 （一般前端会有判断）
    if user == '':
        result['status'] = 0
        result['code'] = 1001
        result['message'] = '请输入账号'
        return result
    # 密码为空 （一般前端会有判断）
    if pwd == '':
        result['status'] = 0
        result['code'] = 1002
        result['message'] = '请输入密码'
        return result
    # 账号或密码不正确
    # 假设只有一个用户zhouhuajian 密码123456
    if user != 'zhouhuajian' or pwd != '123456':
        result['status'] = 0
        result['code'] = 1003
        result['message'] = '账号或密码不正确'
        # result['message'] = '账号或密码不正确！'
        return result
    # 登录成功，使用SESSION记录用户ID
    session['uid'] = 1
    return result


@web.route('/api/logout', methods=['POST'])
def api_logout():
    """登出接口"""
    # 结果
    result = {'status': 1, 'code': 0, 'message': '退出成功', 'data': {}}
    # 删除SESSION
    session.pop('uid', None)
    return result


@web.route('/api/get_user_info', methods=['GET', 'POST'])
def api_get_user_info():
    """获取用户信息接口"""
    # 结果
    result = {'status': 1, 'code': 0, 'message': '', 'data': {}}
    uid = session.get('uid')
    if uid is None:
        result['status'] = 0
        result['code'] = 1000
        result['message'] = '请先登录'
        return result
    # 假设只有一个用户zhouhuajian
    user_info = {
        'uid': uid,
        'username': 'zhouhuajian',
        'realname': '周华健',
        'gender': 0,  # 0男，1女
        'is_vip': 1,  # 是否是VIP
    }
    result['data'] = user_info
    return result


@web.route('/api/create_article', methods=['POST'])
def api_create_article():
    """创建文章接口"""
    # 结果
    result = {'status': 1, 'code': 0, 'message': '创建成功', 'data': {}}
    # 检查登录
    if not _check_login():
        result['status'] = 0,
        result['code'] = 1000,
        result['message'] = '请先登录'
        return result
    title = request.values.get('title').strip()
    content = request.values.get('content').strip()
    # 标题为空 （一般前端会有判断）
    if title == '':
        result['status'] = 0
        result['code'] = 1100
        result['message'] = '请输入标题'
        return result
    # 标题最多10个字
    if len(title) > 10:
        result['status'] = 0
        result['code'] = 1101
        result['message'] = '标题最多10个字'
        return result
    # 内容为空 （一般前端会有判断）
    if content == '':
        result['status'] = 0
        result['code'] = 1102
        result['message'] = '请输入内容'
        return result
    # 假设创建了一篇文章
    result['data']['article_id'] = 1
    return result


@web.route('/api/del_article', methods=['POST'])
def api_del_article():
    """删除文章接口"""
    # 结果
    result = {'status': 1, 'code': 0, 'message': '删除成功', 'data': {}}
    # 检查登录
    if not _check_login():
        result['status'] = 0
        result['code'] = 1000
        result['message'] = '请先登录'
        return result
    article_id = request.values.get('article_id').strip()
    # 文章ID位空
    if not article_id:
        result['status'] = 0
        result['code'] = 1110
        result['message'] = '请提供需要删除的文章ID'
        return result
    # 假设只有一篇文章
    if article_id != '1':
        result['status'] = 0
        result['code'] = 1111
        result['message'] = '文章不存在'
        return result
    # 假设删除成功
    return result


def _check_login():
    """检查是否登录"""
    return bool(session.get('uid'))


if __name__ == "__main__":
    web.run()
