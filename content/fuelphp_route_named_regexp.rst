Named conditional routing in FuelPHP
################################################################
:date: 2013-06-25 23:41
:author: ka2n
:category: general
:tags: php, FuelPHP

FuelPHPでルーティングルールを設定する時, (:segment)や(:num),(:alpha)等を使えます。
また、:name, :hogeなど名前付きのルートを設定することも可能です。

ただし、名前付きのルートは内部で (?P<$1>.+?) になる。名前を指定すると正規表現のルールが決め打ちになってします。
なので正規表現で書いてみる。


/foo/(:num)/bar を名前付きでマッチする例

.. code-block:: plain

    /foo/(?P<name>:num?)/bar


そのままベタで正規表現で書く例

.. code-block:: plain

    /foo/(?P<name>\d{2}?)/bar


マッチした名前のパラメータは $this->param('name')で取り出すことができます。

よくドキュメントを読むと "You can include any regex into your routes" って書いてあるんですね。知らなかった。
