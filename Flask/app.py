from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app=app)

'''创建表'''
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, comment='用户ID')
    name = db.Column(db.String(30), comment='用户名')
    num = db.Column(db.Integer, comment='关注数')

    # repr() 方法现实一个可读字符串
    def __repr__(self):
        return str(self.name)

# 得到所有用户
@app.route('/')
def all_users():
    users = User.query.order_by(User.id.asc()).all()
    return render_template('all_users.html', users=users)

# 添加用户
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form.get('name')
        num = request.form.get('num')
        new_user = User(name=name, num=num)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('all_users'))
    return render_template('add_user.html')

# 修改用户
@app.route('/edit_user', methods=['POST', 'GET'])
def edit_user():
    user_id = request.args.get('user_id')
    one_user = User.query.get(user_id)
    print(one_user.id)
    if request.method == 'POST':
        name = request.form.get('name')
        one_user.name = name
        db.session.add(one_user)
        db.session.commit()
        return redirect(url_for('all_users'))
    return render_template('edit_user.html', one_user=one_user)

# 删除单个用户
@app.route('/delete_user')
def delete_user():
    user_id = request.args.get('user_id')
    one_user = User.query.get(user_id)
    db.session.delete(one_user)
    db.session.commit()
    return redirect(url_for('all_users'))

# 批量删除用户
@app.route('/delete_users', methods=['POST'])
def delete_users():
    user_ids = request.form.getlist('user_ids')
    for user_id in user_ids:
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('all_users'))

# 用户详情
@app.route('/user_detail')
def user_detail():
    user_id = request.args.get('user_id')
    one_user = User.query.get(user_id)
    return render_template('user_detail.html', one_user=one_user)

# 提醒登录
@app.route('/login',methods=['POST'])
def login():
    return '请先登录'

if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    app.run(debug=app.config['DEBUG'])
