ena.li公開しました
##################
:date: 2011-01-17 20:59
:author: ka2n
:category: general
:slug: ena-li

| |enali|
| http://ena.li/

GoogleAppEngineの練習のためにwebappフレームワークを使って作ってみました。

短縮URL(URL shortener)ってやつです。

名前
----

たまたま.liドメインを取ってみたかったため

使い方
------

このページ(えなりかずきオフィシャルブログ｢えなリズム｣)のURLを短くすると

    http://ena.li/eUwaIA

こんな感じになります。無難に6文字です。別にそこまで短くない。

    http://ena.li/eUwaIA+

という感じで末端に+(プラス)を付与することで、そのURLのアクセス数を見ることが出来るページが表示されます。

http://ena.li/eUwaIA.qr

末端に.qrを付けるとGoogle Chart
APIでのQRコード出力用のURLへリダイレクトされます。即ちQRコードが表示されます。

また、自分の好きな文字をURLに指定することもできます。

    http://ena.li/yahoo

    `http://ena.li/かずき`_

こんなんでもたぶんOK。

http://ena.li/

.. |enali| image:: http://capture.heartrails.com/medium?http://ena.li/
.. _http://ena.li/かずき: http://ena.li/%E3%81%8B%E3%81%9A%E3%81%8D
