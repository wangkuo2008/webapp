from flask import *
app = Flask(__name__) #ここは気にしなくて大丈夫です。

#最初に行う処理
@app.route('/') #http://localhost:5000
def home():
	#周辺店舗表示画面へ遷移
	#周辺店舗の情報などを取得する処理を書いてください


    return render_template('home.html') 

#検索ボタンを押したら行う処理
@app.route('/login',methods=['GET', 'POST']) #URLの指定。今回はhttp://localhost:5000/login
def login():
	#ログイン画面へ遷移
	#このままでOK
	return render_template('index.html')

@app.route('/mypage',methods=['GET', 'POST'])
def mypage():
	#マイページへ遷移
	#ログイン認証の処理を行います。
	
	return render_template('mypage.html')

@app.route('/graph',methods=['GET', 'POST'])
def graph():
	#グラフ表示画面へ遷移
	#グラフデータを取得してください


	return render_template('graph.html')

@app.route('/store',methods=['GET', 'POST'])
def store():
	#店舗詳細画面へ遷移
	#店舗情報などを取得してください


	return render_template('store.html')

@app.route('/create_account',methods=['GET', 'POST'])
def create_account():
	#新規店舗登録画面へ遷移
	#ここは何も書かなくてOK
	return render_template('create_account.html')

@app.route('/new_user_login',methods=['GET', 'POST'])
def new_user_login():
	#新規会員登録後ログイン画面へ遷移
	#新規会員情報をデータベースに保存してください
	return render_template('login.html')

@app.route('/commodity',methods=['GET', 'POST'])
def commodity():
	#商品詳細表示ページへ遷移
	#商品情報を取得する処理書いてください


	return render_template('commodity.html')

@app.route('/discount_commodity',methods=['GET', 'POST'])
def discount_commodity():
	#割引商品登録後、マイページへ遷移
	#割引商品をデータベースに保存してください
	return render_template('mypage.html')

@app.route('/stock',methods=['GET', 'POST'])
def stock():
	#在庫入力画面へ遷移
	#ここは何もしなくて大丈夫です
	return render_template('stock.html')

@app.route('/stock_save',methods=['GET', 'POST'])
def stock_save():
	#在庫登録後、マイページへ遷移
	#在庫情報を登録する処理を記述してください


	return render_template('mypage.html')

## ここは気にしなくて大丈夫です。
if __name__ == "__main__":
    app.run(debug=True)