OAuthがわからない oauth_adapter.js
##################################
:date: 2011-08-16 15:20
:author: ka2n
:category: general
:tags: titanium
:slug: oauth-oauth_adapter-js

Titanium
mobileでOAuthを使ったアプリケーションをつくろうとおもって、oauth\_adapter.jsを使ってみようと思ったんだけど、r14からRequestTokenを取得するときに、パラメータが追加できなくなってる。

oauth\_callbackが指定できないんだよなー
oauth\_callback=oobを指定して、ブラウザ上でPINを表示させたい。
Twitterとかはパラメータがあったとしても無視で、なくても大丈夫そうなんだけど、自分が使ったライブラリはoauth\_callbackが無いとエラーになってしまう。

仕様上はどちらが正しいのだろうか。

#追記
http://oauth.net/core/1.0a/#anchor9

を見ると、デスクトップアプリケーションなどでcallbackのURLが設定できない場合は、oauth\_callbackにoob
(out-of-bandの意)を指定する必要があるようだ。
