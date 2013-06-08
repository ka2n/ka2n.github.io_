スマートフォンとPCで表示するViewを変更 #FuelPHP
###############################################
:date: 2012-01-20 01:22
:author: ka2n
:category: general
:tags: fuelphp, php
:slug: pc-view-fuelphp

最近FuelPHP初めましたっ///

同一のURLでPCとスマートフォンに対応したいですよね。

| CSS3 Media Queriesを使ってクライアントサイドで振り分ける
|  UserAgentを見てサーバサイドで振り分ける
|  なんて方法があると思います。
|  全部Media
Queriesを使ってやろうとすると、スマホ用とPC用とPad用でごっちゃごちゃになっちゃいそうです。まず、PCとスマホ/Padで分けてから、Media
QueriesでスマホとPadで分けるのがいいんじゃないかと個人的には思います。スマホとPadはタッチデバイス(であることが多い)ですからね。

| FuelPHPには、UserAgent周りを扱うAgentクラスがありますのでそれを使います。
| 
あと、Themeクラスなんていうものもあります(これなぜかドキュメントに載っていない)
。この2つを使ってみたいと思います。

作戦

| FuelのControllerクラスを拡張してAppControllerクラスを作る。
|  AppController::beforeでUserAgentを判別し、テーマを切り替える。
|  レスポンスはThemeクラスを使って構築する。

よし、早速やってみます。

| [code lang="php"
title="APPPATH/classes/controller/app\_controller.php"]<?php
|  class AppController extends Fuel\\Core\\Controller
|  {
|  public function before()
|  {
|  return parent::before();
|  }
|  }[/code]

とりあえずこんな感じでファイルを作成します。ちなみにAppControllerとかネーミングは適当デス。

このクラスをFuelPHPが動くたびに読み込んでくれるように設定します。

| [code lang="php" title="APPPATH/bootstrap.php" firstline="11"]
|  Autoloader::add\_classes(array(
|  // Add classes you want to override here
|  // Example: 'View' => APPPATH.'classes/view.php',
|  'AppController' => APPPATH.'classes/controller/\_app\_controller.php'
|  ));
|  [/code]

これで、どのクラスからもAppControllerという名前で作成したクラスを呼び出せるようになりました。

| 次に、AgentをつかってUAを判別する部分を書きます。
|  [code lang="php"
title="APPPATH/classes/controller/app\_controller.php"]
|  <?php
|  class AppController extends Fuel\\Core\\Controller
|  {
|  public function before()
|  {
|  return parent::before();
|  }

| private function is\_smartphone()
|  {
|  return Agent::is\_mobiledevice();
|  }

| }
|  [/code]

| こんな感じに書いてみました。Agentクラスはbrowsecap.iniを読み込んでいるのでそれでUAを判別しています。
|  今回はPC以外はスマートフォンってことにします。
| 
あと、SoftBankが見当たらないんですがどうすればいいんでしょうか。フューチャーフォン対応はしないので気にしません。
| 
Agent::browser();で"DoCoMo"とか取得できるので、フューチャーフォン対応が必要ならそれを使うことになると思います。

| 最後に、Themeクラスを使って読み込むViewファイルを切り替えてみます。
| 
このThemeクラスっていうのがよく分からなくて、それっぽい名前なので使ってみるのですが、本来意図された使い方とは違うかもしれません。

Themeクラス自体の使い方はこんな具合です。

| [code lang="php" title="APPPATH/classes/controller/hogehoge.php"]
|  <?php

| class Controller\_Hogehoge extends Controller
|  {

| public function before()
|  {
|  $this->Theme = Theme::forge(array(
|  'active' => 'theme1', // 現在のテーマ
|  'fallback' => 'default', //
現在のテーマに目的のViewファイルが無かった時に探すテーマ
|  'paths' => array(APPPATH.'views'), // テーマディレクトリの検索パス
|  'assets\_folder' => 'assets', // assetsのフォルダ名(謎)
|  'view\_ext' => '.php', // Viewファイルの拡張子
|  'require\_info\_file' => false, // 謎
|  'info\_file\_name' => 'theme.info', // 謎
|  ));
|  //
info\_file\_nameとかあることを考えると、WordPressみたいなテーマシステムを組み込むためのもの？
|  //
forgeの引数に設定を書くと、Themeクラスのデフォルト設定に上書きされる
|  //
設定を書かなければデフォルト値が使われるか、APPPATH/config/theme.phpがあればそれが読み込まれる

| return parent::before();
|  }

| public function action\_welcome()
|  {
|  return Response::forge($this->Theme->view('welcome/index')); //
View->forgeの代わりにTheme::viewを使う
|  }
|  }
|  [/code]

| ちなみにViewクラスの置き換えはできますが、ViewModelをすることは今のところ出来ないようです。
|  上記の呼び出し方の場合、APPPATH/viewsがベースになるので、

-  APPPATH/views/default/
-  APPPATH/views/theme1/
-  APPPATH/views/theme2/

上記のパスにそれぞれのビューのファイルを配置します。

| このThemeクラスを先程のAppControllerに組み込んでみました。
|  [code lang="php"
title="APPPATH/classes/controller/app\_controller.php"]
|  <?php

| class AppController extends Fuel\\Core\\Controller
|  {
|  public function before()
|  {

| $activeTheme = 'default';
|  if($this->is\_smartphone()) {
|  $activeTheme = 'smartphone';
|  }

| $this->Theme = Theme::forge(array(
|  'active' => $activeTheme,
|  'fallback' => 'default',
|  'paths' => array(APPPATH .'views'),
|  'view\_ext' => '.php'
|  ));

| return parent::before();
|  }

| private function is\_smartphone()
|  {
|  return Agent::is\_mobiledevice();
|  }
|  }

| [/code]
|  UAに対応したテーマ名をThemeクラスに設定してあげているだけです。

あとはこんな具合

| [code lang="php" title="APPPATH/classes/controller/welcome.php"]
|  <?php
|  class Controller\_Welcome extends AppController
|  {

| public function before()
|  {
|  return parent::before();
|  }

| public function action\_index()
|  {
|  return Response::forge($this->Theme->view('welcome/index'));
|  }
|  }
|  [/code]

| [code lang="html" title="APPPATH/views/default/welcome/index.php"]
|  <!DOCTYPE HTML>
|  <html lang="ja">
|  <head>
|  <meta charset="UTF-8">
|  <title>PC</title>
|  </head>
|  <body>
|  <h1>このページはPC用です</h1>
|  </body>
|  </html>
|  [/code]

| [code lang="html" title="APPPATH/views/smartphone/welcome/index.php"]
|  <!DOCTYPE HTML>
|  <html lang="ja">
|  <head>
|  <meta charset="UTF-8">
|  <meta name="viewport" content="width=device-width, initial-scale=1,
maximum-scale=2">
|  <title>スマートフォン/Pad</title>
|  <style>

| .only\_for\_pad {
|  display: none;
|  }

| .only\_for\_mobile {
|  display: none;
|  }

| @media screen and (max-width: 480px) {
|  .only\_for\_mobile {
|  display: block;
|  }
|  }

| @media only screen and (min-device-width: 768px) and
(max-device-width: 1024px) {
|  .only\_for\_pad {
|  display: block;
|  }
|  }

| </style>
|  </head>
|  <body>
|  <p>Padとスマホで表示されるページです。</p>
|  <p class="only\_for\_pad">この文章はPad用です。</p>
|  <p class="only\_for\_mobile">この文章はモバイル用です。</p>
|  </body>
|  </html>
|  [/code]

実際に動かしてみました。

[gallery link="file"]

あとがき
--------

試していないですが、Themeクラスを使わずに
Fuel::add\_pathで単純にパスを追加するだけでViewModelで使えて幸せになれるんじゃないかと思います(今更)
