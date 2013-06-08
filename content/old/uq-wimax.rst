UQ WiMAXの通信環境をみんなで共有する
####################################
:date: 2010-04-16 12:08
:author: ka2n
:category: general
:tags: Mac, Tips, WiMAX
:slug: uq-wimax

先日UQ
WiMAXのMVMOのDIS(ダイワボウ情報システム)のプロバイダに登録しました。自分の行動する範囲ではほぼ全域で繋がり、しかも4〜6Mbpsとそこそこの速度が出ます。母艦(Mac
OSX Snow Leopard
10.6.3)に差したWMX-U02からインターネットに接続されています。そのネットワークを合宿や勉強会でみんなでシェアできたらいいな。と思いやってみた。

インターネット共有を使う
~~~~~~~~~~~~~~~~~~~~~~~~

どうやら標準の機能で共有できるみたいです。

#. システム環境設定→共有→インターネット共有をクリック(チェックボックスはそのまま)
#. 共有する接続経路には"I-O DATA WMX-U Series WiMAX Adapter"を選択。
#. 相手のコンピュータが使用するポートに"AirMac"を選択。
#. AirMacオプションを適当に設定。
#. インターネット共有にチェックを入れる。
#. WiMAXのユーティリティで既に接続してあった場合は、一度切断してからもう一度つなぎ直す。
#. 他の機器から母艦が作っているWiFiのネットワークに参加する。
#. 接続を確認！

5と6の順番を間違えると、つながらなかったので注意です。

|image0|\ |image1|\ |image2|

.. |image0| image:: http://ktmtt.com/diary/wp-content/uploads/sharepref-300x256.png
   :target: http://ktmtt.com/diary/wp-content/uploads/sharepref.png
.. |image1| image:: http://ktmtt.com/diary/wp-content/uploads/internetshare-300x251.png
   :target: http://ktmtt.com/diary/wp-content/uploads/internetshare.png
.. |image2| image:: http://ktmtt.com/diary/wp-content/uploads/airmacoption-300x187.png
   :target: http://ktmtt.com/diary/wp-content/uploads/airmacoption.png
