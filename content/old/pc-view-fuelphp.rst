スマートフォンとPCで表示するViewを変更 #FuelPHP
###############################################
:date: 2012-01-20 01:22
:author: ka2n
:category: general
:tags: fuelphp, php
:slug: pc-view-fuelphp

最近FuelPHP初めましたっ///

同一のURLでPCとスマートフォンに対応したいですよね。

- CSS3 Media Queriesを使ってクライアントサイドで振り分ける
- UserAgentを見てサーバサイドで振り分ける

なんて方法があると思います。
全部Media Queriesを使ってやろうとすると、スマホ用とPC用とPad用でごっちゃごちゃになっちゃいそうです。
まず、PCとスマホ/Padで分けてから、Media QueriesでスマホとPadで分けるのがいいんじゃないかと個人的には思います。
スマホとPadはタッチデバイス(であることが多い)ですからね。

FuelPHPには、UserAgent周りを扱うAgentクラスがありますのでそれを使います。
あと、Themeクラスなんていうものもあります(これなぜかドキュメントに載っていない)。
この2つを使ってみたいと思います。

作戦

    FuelのControllerクラスを拡張してAppControllerクラスを作る。
    AppController::beforeでUserAgentを判別し、テーマを切り替える。
    レスポンスはThemeクラスを使って構築する。

よし、早速やってみます。

APPPATH/classes/controller/app\_controller.php

.. code-block:: php

    <?php
    class AppController extends Fuel\Core\Controller
    {
        public function before()
        {
            return parent::before();
        }
    }

とりあえずこんな感じでファイルを作成します。ちなみにAppControllerとかネーミングは適当デス。

このクラスをFuelPHPが動くたびに読み込んでくれるように設定します。

APPPATH/bootstrap.php

.. code-block:: php

    <?php
    ...略...

    Autoloader::add_classes(array(
        // Add classes you want to override here
        // Example: 'View' => APPPATH.'classes/view.php',
        'AppController' => APPPATH.'classes/controller/app_controller.php'
    ));

これで、どのクラスからもAppControllerという名前で作成したクラスを呼び出せるようになりました。

次に、AgentをつかってUAを判別する部分を書きます。

APPPATH/classes/controller/app\_controller.php

.. code-block:: php

    <?php

    class AppController extends Fuel\Core\Controller
    {
        public function before()
        {
            return parent::before();
        }

        private function is_smartphone()
        {
            return Agent::is_mobiledevice();
        }

    }

こんな感じに書いてみました。Agentクラスはbrowsecap.iniを読み込んでいるのでそれでUAを判別しています。
今回はPC以外はスマートフォンってことにします。
あと、SoftBankが見当たらないんですがどうすればいいんでしょうか。フューチャーフォン対応はしないので気にしません。
Agent::browser();で"DoCoMo"とか取得できるので、フューチャーフォン対応が必要ならそれを使うことになると思います。
最後に、Themeクラスを使って読み込むViewファイルを切り替えてみます。
このThemeクラスっていうのがよく分からなくて、それっぽい名前なので使ってみるのですが、本来意図された使い方とは違うかもしれません。

Themeクラス自体の使い方はこんな具合です。

APPPATH/classes/controller/hogehoge.php

.. code-block:: php

    <?php
    class Controller_Hogehoge extends Controller
    {
        public function before()
        {
            $this->Theme = Theme::forge(array(
                'active' => 'theme1', // 現在のテーマ
                'fallback' => 'default', // 現在のテーマに目的のViewファイルが無かった時に探すテーマ
                'paths' => array(APPPATH.'views'), // テーマディレクトリの検索パス
                'assets_folder' => 'assets', // assetsのフォルダ名(謎)
                'view_ext' => '.php', // Viewファイルの拡張子
                'require_info_file' => false,
                'info_file_name' => 'theme.info',
            ));

            // info_file_nameとかあることを考えると、WordPressみたいなテーマシステムを組み込むためのもの？
            // forgeの引数に設定を書くと、Themeクラスのデフォルト設定に上書きされる
            // 設定を書かなければデフォルト値が使われるか、APPPATH/config/theme.phpがあればそれが読み込まれる

            return parent::before();
        }

        public function action_welcome()
        {
            return Response::forge($this->Theme->view('welcome/index')); // View->forgeの代わりにTheme::viewを使う
        }
    }

ちなみにViewクラスの置き換えはできますが、ViewModelをすることは今のところ出来ないようです。
上記の呼び出し方の場合、APPPATH/viewsがベースになるので、

-  APPPATH/views/default/
-  APPPATH/views/theme1/
-  APPPATH/views/theme2/

上記のパスにそれぞれのビューのファイルを配置します。

このThemeクラスを先程のAppControllerに組み込んでみました。

APPPATH/classes/controller/app\_controller.php

.. code-block:: php

    <?php

    class AppController extends Fuel\Core\Controller
    {

        public function before()
        {
            $activeTheme = 'default';
            if ($this->is_smartphone()) {
                $activeTheme = 'smartphone';
            }

            $this->Theme = Theme::forge(array(
                'active' => $activeTheme,
                'fallback' => 'default',
                'paths' => array(APPPATH .'views'),
                'view_ext' => '.php'
            ));

            return parent::before();
        }

        private function is_smartphone()
        {
            return Agent::is_mobiledevice();
        }
    }

UAに対応したテーマ名をThemeクラスに設定してあげているだけです。

あとはこんな具合

APPPATH/classes/controller/welcome.php

.. code-block:: php

    <?php
    class Controller_Welcome extends AppController
    {

        public function before()
        {
            return parent::before();
        }

        public function action_index()
        {
            return Response::forge($this->Theme->view('welcome/index'));
        }
    }



APPPATH/views/default/welcome/index.php

.. code-block:: html

    <!DOCTYPE HTML>
    <html lang="ja">
        <head>
            <meta charset="UTF-8">
            <title>PC</title>
        </head>
        <body>
            <h1>このページはPC用です</h1>
        </body>
    </html>

APPPATH/views/smartphone/welcome/index.php

.. code-block:: html

    <!DOCTYPE HTML>
    <html lang="ja">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1,
            maximum-scale=2">
            <title>スマートフォン/Pad</title>
            <style>

                .only_for_pad {
                    display: none;
                }

                .only_for_mobile {
                    display: none;
                }

                @media screen and (max-width: 480px) {
                    .only_for_mobile {
                        display: block;
                    }
                }

                @media only screen and (min-device-width: 768px) and
                (max-device-width: 1024px) {
                    .only_for_pad {
                        display: block;
                    }
                }

            </style>
        </head>
        <body>
            <p>Padとスマホで表示されるページです。</p>
            <p class="only_for_pad">この文章はPad用です。</p>
            <p class="only_for_mobile">この文章はモバイル用です。</p>
        </body>
    </html>


あとがき
--------

試していないですが、Themeクラスを使わずに
Fuel::add\_pathで単純にパスを追加するだけでViewModelで使えて幸せになれるんじゃないかと思います(今更)
