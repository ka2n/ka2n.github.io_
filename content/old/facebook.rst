デスクトップでもスマートフォンでもFacebookチャットをする
########################################################
:date: 2011-07-07 23:59
:author: ka2n
:category: general
:tags: facebook
:slug: facebook

| 自分の周りでもずいぶんとFacebookが普及してきた感じがします。チャット機能もついているので、そこで会話することもしばしば。
| 
このFacebookチャット、普通のメッセンジャーアプリでも利用出来るんです。

| |image0|
|  `Facebookチャット`_

| XMPPに対応したチャットサーバをFacebookは持っているので、それに対応したクライアントアプリであれば利用できます。
|  具体的には

-  `Pidgin`_ - Windows/Mac/Linux
-  `Adium`_ - Mac
-  `iChat`_ - Mac

などなど。

| 設定情報はここから見ることができます。
|  http://www.facebook.com/sitetour/chat.php

各クライアントですでに、"Facebook"として対応しているものも多いですね。

iChatでやってみた
-----------------

| まずはiChatを起動( `このリンクから起動できます`_ )
|  |image1|

| メニューの"iChat" > "環境設定" ( もしくはCommand - , )
|  |image2|

| 環境設定画面、左下の"+"ボタンをクリック
|  |image3|

| アカウントの種類は"Jabber"を選択する
|  |image4|
|  アカウント名:@chat.facebook.com
|  パスワード:
|  サーバ: chat.facebook.com
|  ポート: 5222
|  「SSLを使用」のチェックボックスは外す
|  「認証にKerberos v5を使用」はそのまま。

完了ボタンを押せば設定完了

|image5|

iPhoneアプリの説明は割愛しますが、"XMPP"とか"Jabber"とかで検索すれば\ `こんなの`_\ が出てきます。上の情報で設定すればOK。

.. _Facebookチャット: http://www.facebook.com/sitetour/chat.php
.. _Pidgin: http://www.pidgin.im/
.. _Adium: http://adium.im/
.. _iChat: http://www.apple.com/macosx/apps/all.html#ichat
.. _このリンクから起動できます: ichat://
.. _こんなの: http://itunes.apple.com/us/app/jabba/id364674890?mt=8

.. |image0| image:: http://ktmtt.com/diary/wp-content/uploads/fc.png
   :target: http://ktmtt.com/diary/wp-content/uploads/fc.png
.. |image1| image:: http://ktmtt.com/diary/wp-content/uploads/ichat.png
   :target: http://ktmtt.com/diary/wp-content/uploads/ichat.png
.. |image2| image:: http://ktmtt.com/diary/wp-content/uploads/0.png
   :target: http://ktmtt.com/diary/wp-content/uploads/0.png
.. |image3| image:: http://ktmtt.com/diary/wp-content/uploads/1-300x265.png
   :target: http://ktmtt.com/diary/wp-content/uploads/1.png
.. |image4| image:: http://ktmtt.com/diary/wp-content/uploads/2.png
   :target: http://ktmtt.com/diary/wp-content/uploads/2.png
.. |image5| image:: http://ktmtt.com/diary/wp-content/uploads/3-300x201.png
   :target: http://ktmtt.com/diary/wp-content/uploads/3.png
