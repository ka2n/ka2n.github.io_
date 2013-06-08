Kindle paperwhite 5.3をJailbreakしてみた
########################################
:date: 2013-01-03 20:58
:author: ka2n
:category: general
:tags: kindle
:slug: kindle-paperwhite-5-3-jailbreak

僕も買いました。Amazon Kindle paperwhite.
いやーバックライト便利。ワンクリック購入便利。ここの所iPhone5 + Kindle
paperwhiteの組み合わせが一番しっくりきます。

koboハックは案外盛り上がっていて楽しそうですが、既に一番使っているのはkindle.
ハックできたら楽しいだろうなぁ、、そんな夢を見ました。

.. raw:: html

   <div class="caution" style="background: #F2DEDE; color: #b94a48; border: #EED3D7 1px solid; font-size: 0.8em; padding: 0.3em;">

| 以下夢につき、同じ事を試すことであなたのkindleが\ **ただの板**\ になってしまう可能性があります。文鎮化した場合は本当にどうしようもなくなるようです.
|  その際にまな板以外の使い方が見つかっておりませんのでご注意下さい。

.. raw:: html

   </div>

| 現在対応しているファームウェアのバージョンは5.3.1までのようです。
|  バージョンの確認は、ホームから 右上のメニュー > 設定 >
もう一度右上のメニュー > 端末情報
から見ることができます。自分は購入時5.3.0、先程5.3.1にアップデートしました。(やり方は\ `こっち`_\ に書きました)

http://www.mobileread.com/forums/showthread.php?t=198446

#. 上記URLで公開されている kpw\_jb.zip
   をダウンロードしてくる。こいつはjailbreak用のスクリプト以外にもレスキュー用のファイルやらなんやらが含まれていてよしなにやってくれるみたい。(jailbreak.sh見れば大きな流れがわかるよ) 展開しREADME.txtにそって手順を踏んでいきます。
#. kindleをUSBでPCにつなぐ。ファイルシステムにマウントされるので直下にjailbreak.sh"
   と "MOBI8\_DEBUG"をコピーする。
#. jailbreak.mobiは直下ではなくdocuments以下に置く。(これが細工されたmobiファイルでjailbreak.shを呼ぶのかな??)
#. kindleをアンマウントする。
#. ホーム画面に"Paperwhite
   Jailbreak"とマヤ文明の絵みたいな表紙が書かれたパーソナルドキュメントがあるのでそれを開く
    |kindle jailbreal|
#. すると下の画面になるので、文字をタップ
    |image1|
#. 表示されているとおりに左上を2秒ほど長押し
    |image2|
#. あとはおまかせ、、
    `|image3|
   `_\ `|image4|
   `_\ |image5|
#. 丁寧にログまで残してくれるんですね。あっさり完了。
    |image6|
    |image7|

文鎮化した際はどうしようもないようなので、その時は観念しましょう。

.. _こっち: http://ktmtt.com/diary/2012-kindle-paperwhite-firmware-update.html
.. _|image8|
: http://ktmtt.com/diary/wp-content/uploads/ff15cbae21d03e1b9fb739830db4f39c.png
.. _|image9|
: http://ktmtt.com/diary/wp-content/uploads/ab4d8a5d3ba2182253f295b7de29f41c.png

.. |kindle jailbreal| image:: http://ktmtt.com/diary/wp-content/uploads/22e2b5cc8d152fff9a3ba6f6a9c4b214-222x300.png
   :target: http://ktmtt.com/diary/wp-content/uploads/22e2b5cc8d152fff9a3ba6f6a9c4b214.png
.. |image1| image:: http://ktmtt.com/diary/wp-content/uploads/db2b16b36269374d5e52441a4f62538e-222x300.png
   :target: http://ktmtt.com/diary/wp-content/uploads/db2b16b36269374d5e52441a4f62538e.png
.. |image2| image:: http://ktmtt.com/diary/wp-content/uploads/8b9ba847f0d35b7e69bca4ed920c0974-222x300.png
   :target: http://ktmtt.com/diary/wp-content/uploads/8b9ba847f0d35b7e69bca4ed920c0974.png
.. |image3| image:: http://ktmtt.com/diary/wp-content/uploads/ff15cbae21d03e1b9fb739830db4f39c-222x300.png
.. |image4| image:: http://ktmtt.com/diary/wp-content/uploads/ab4d8a5d3ba2182253f295b7de29f41c-222x300.png
.. |image5| image:: http://ktmtt.com/diary/wp-content/uploads/72f02428f02127c6315bf8de95bfde51-222x300.png
   :target: http://ktmtt.com/diary/wp-content/uploads/72f02428f02127c6315bf8de95bfde51.png
.. |image6| image:: http://ktmtt.com/diary/wp-content/uploads/38be4d412c6a6f8f1b88e9efb6f05b02-222x300.png
   :target: http://ktmtt.com/diary/wp-content/uploads/38be4d412c6a6f8f1b88e9efb6f05b02.png
.. |image7| image:: http://ktmtt.com/diary/wp-content/uploads/4e1deab25f47a7c3709a0855bb1ed593-222x300.png
   :target: http://ktmtt.com/diary/wp-content/uploads/4e1deab25f47a7c3709a0855bb1ed593.png
.. |image8| image:: http://ktmtt.com/diary/wp-content/uploads/ff15cbae21d03e1b9fb739830db4f39c-222x300.png
.. |image9| image:: http://ktmtt.com/diary/wp-content/uploads/ab4d8a5d3ba2182253f295b7de29f41c-222x300.png
