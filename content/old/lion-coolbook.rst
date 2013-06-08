LionでCoolBookを使うためのたった一つの方法
##########################################
:date: 2011-07-29 11:13
:author: ka2n
:category: general
:tags: CoolBook, Lion
:slug: lion-coolbook

煽りタイトル万歳

Mac OS X 10.7
Lionがリリースされて早速アップグレードした方はたくさん居らっしゃるでしょうが、モバイラー必須のソフトウェアであるところのCoolBook(ver2.22)がLionでは動かない事に落胆している方もそれなりに居らっしゃる事でしょう。

ということで、LionでもCoolBookを使う方法があったので書きました。OSの中の重要なファイルをいじるので、\ **失敗すれば最悪OS再インストールなどが必要になります。責任は一切取れませんのでよろしくお願いします。**

手順は以下の通り

#. CoolBookをインストール
#. /System/Library/Extensionsの中にある、AppleIntelCPUPowerManagementClient.kextとAppleIntelCPUPowerManagement.kextをバックアップ
#. 上記の2つのkextを削除
#. `SleepEnabler for Lion 10.7.0
   Lates`_??からSleepEnabler.kext.10.7.x.zipをダウンロード、展開してSleepEnabler.kextを手に入れます
#. SleepEnabler.kextを/System/Library/Extensions/内に入れて、パーミッションなどを設定する(
   やり方が分からない場合は `kexthelper`_\ を使ってください )
#. 再起動

これでCoolBookが戻ってきます。注意点としては、i5 /
i7は依然非対応ですので、性能いい機械をを使ってる人は我慢してください。

|image0|

$近いうちにCoolBook
ver3.0がリリースされるみたいなので、その時には戻せるように万全にバックアップはとっておくと良いと思います。(アップグレードには$5かかるみたいですけど)

CoolBook万歳!! これで外でも3時間以上...勝てる!

`http://www.coolbook.se/CoolBook.html??`_

.. _SleepEnabler for Lion 10.7.0 Lates: http://blog.nawcom.com/?p=806
.. _kexthelper: http://cheetha.net/
.. _`http://www.coolbook.se/CoolBook.html??`: http://www.coolbook.se/CoolBook.html%20

.. |image0| image:: http://ktmtt.com/diary/wp-content/uploads/coolbook-300x147.png
   :target: http://ktmtt.com/diary/wp-content/uploads/coolbook.png
