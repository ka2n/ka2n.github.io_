OSXとUbuntu10.04でデュアルブート
################################
:date: 2010-04-30 17:46
:author: ka2n
:category: general
:tags: MacBookPro, Ubuntu
:slug: osx-ubuntu10-04

Ubuntuの新しいLTSである10.04がそろそろリリースされます。SSDに入れると起動がチョッ速らしいので、試しに入れてみました。

|image0|

BootCampAssistantを使ってパーティションをリサイズして、新しくWindows用のBootCampパーティションを作り、その中にUbuntu
10.04 Betaを入れました。

|image1|

| 特別問題が起こることもなくインストール完了。\ `このページ`_\ にはrEFItを入れて、パーティションテーブルを修正しろと書いてあったんですが、その必要はありませんでした。
|  インストール後のMacBookPro用の設定方法は
|  https://help.ubuntu.com/community/MacBookPro
| 
に書いてあるので、ここから自分のモデル、MacBookPro5,5の項に書いてある通りに設定します。
|  ただ、

    sudo add-apt-repository ppa:mactel-support && apt-get update

| をした後、source.listに追加されるレポジトリのURLが間違っているので修正します。suport→support
|  そして以下のコマンドを実行して、レポジトリの公開鍵を保存します。

    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
    2B97B7B8

nvidiaのドライバーを入れればCompizも動くし、タッチパッドも一応使えます。輝度調節もバッチリ。無線LANもちゃんと動きます。なかなか快適。

|image2|

まぁ、iCalとiTunesとマルチタッチがUbuntuで使えないのでOSXは捨てられません。

.. _このページ: https://help.ubuntu.com/community/MactelSupportTeam/AppleIntelInstallation

.. |image0| image:: http://ktmtt.com/diary/wp-content/uploads/Screenshot-300x187.png
   :target: http://ktmtt.com/diary/wp-content/uploads/Screenshot.png
.. |image1| image:: http://ktmtt.com/diary/wp-content/uploads/bootcamp.png
   :target: http://ktmtt.com/diary/wp-content/uploads/bootcamp.png
.. |image2| image:: http://ktmtt.com/diary/wp-content/uploads/Screenshot-1-300x187.png
   :target: http://ktmtt.com/diary/wp-content/uploads/Screenshot-1.png
