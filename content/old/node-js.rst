すごい遅れ馳せながらnode.jsはじめました
#######################################
:date: 2012-02-03 15:12
:author: ka2n
:category: general
:tags: nodejs
:slug: node-js

マジで乗り遅れている。

| おら
|  [code title="console"]
|  $ brew install node
|  [/code]

| Socket.IOとかいうライブラリを使うとWebSocketとかできるのか。
|  ちなみにWebSocket的なのはGAEのChannel
APIでやったことがある(気がする)。

Expressというのを入れるとルーティングもやってくれるみたい。

| パッケージ管理はnpmを使うらしい。
|  [code title="console"]
|  $ brew install npm
|  Error: No available formula for npm
|  npm can be installed thusly by following the instructions at
|  http://npmjs.org/

| To do it in one line, use this command:
|  curl http://npmjs.org/install.sh \| sh
|  [/code]
|  ほう、そうか
|  [code title="console"]
|  $ curl http://npmjs.org/install.sh \| sh
|  -- 中略 --
|  All clean!
|  /usr/local/bin/npm -> /usr/local/lib/node\_modules/npm/bin/npm-cli.js
|  npm@1.1.0-3 /usr/local/lib/node\_modules/npm
|  It worked
|  [/code]
|  おー/usr/localに入った。おｋおｋ。

| [code title="console"]
|  $ npm install socket.io
|  [/code]
|  これでSocket.IOも入った。

| Socket.IOを使ったアプリケーションのひな形はSocket.IOのページに書いてある。
|  http://socket.io/
|  [code title="console"]
|  var io = require('socket.io').listen(80);
|  io.sockets.on('connection', function (socket) {
|  socket.emit('news', { hello: 'world' });
|  socket.on('my other event', function (data) {
|  console.log(data);
|  });
|  });
|  [/code]
|  emitでイベントを起こして、onでイベントを受け取るらしい。

| あと、Objective-Cのモジュール
|  http://code.google.com/p/unitt/wiki/UnittWebSocketClient
|  これ使ってみよう。

データベースはmongoでいいかな。

これで簡単な投票システムでも作ってみる。できたら追記しよっと(いつやるかは決めてない)。
