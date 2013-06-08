Django on dotcloudでローカルと本番で設定を切り替える方法
########################################################
:date: 2011-06-12 13:02
:author: ka2n
:category: general
:tags: Django, dotcloud
:slug: django-on-dotcloud

dotcloudでdjangoを動かしてみたら簡単すぎて鼻血がでそうなんですが、データベースをdotcloud上とローカルの開発環境で切り替えたいのでこんな感じでやっています。

| settings.py
|  [code]
|  import socket
|  if socket.gethostname() == 'ホスト名':
|  PRODUCTION = True
|  else:
|  PRODUCTION = False
|  [/code]

| 若しくはsettings\_local.py,
settings\_dotcloud.pyを作成しておき、settings.pyの終わりの方で
|  [code]
|  import socket
|  if socket.gethostname() == 'ホスト名':
|  from settings\_dotcloud import \*
|  else:
|  from settings\_local import \*
|  [/code]
|  として、上書きするのが良いかもしれません。

ホスト名-> application-service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| dotcloundの場合、socket.gethostname()で取得できるホスト名は"アプリケーション名-サービス名"となるようです。
| 
デプロイするときは.(ドット)で区切りますが、ホスト名は-(ハイフン)に成るようです。
|  [code]
|  ramen.www -> ramen-www
|  [/code]

先々週にジャンゴさんを触りはじめたので、変な部分があればツッコんで欲しいです。
