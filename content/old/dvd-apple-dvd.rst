外付けDVDドライブしか無い場合に、Apple DVDプレーヤーを使用する
##############################################################
:date: 2010-06-02 23:44
:author: ka2n
:category: general
:tags: DVD, Mac, Tips
:slug: dvd-apple-dvd

| |image0|
| 
僕のMacBookProはOptibay(のパチもん)を使用して、HDDとSSDが内蔵されていて、SuperDriveを取り出してあります。その取り出したドライブはもちろん、ケースに入れてUSB接続のSuperDriveとして使用できるようにしてあるんですが、「内蔵DVD再生ドライブがない場合には、外付けDVDドライブを接続しても、Apple
DVDプレーヤーが使用できない」という問題がありました。

| 具体的には"**There was an initialization error A valid DVD drive could
not be found.[-70012]**\ "というエラーメッセージが表示される。
|  ※日本語だと"**有効なDVD ドライブが見つかりませんでした。[-70012]**\ "

原因はDVDプレーヤーが起動するとまず、内蔵のDVD再生機を探しに行くことにあるようで、それをすべて外付けのDVD再生機を探しに行くように修正します。

| [code]/System/Library/Frameworks/DVDPlayback.framework/Versions/A/DVDPlayback[/code]
|  バイナリエディタにて"internal"をすべて"external"へと置き換え。

| なんとも無理矢理な方法ですが、これでなんとか使えるようになりました。
| 
ただ、外付けDVDドライブを外した状態だと、相変わらず使用できません(せっかくVIDEO\_TSフォルダで再生できるのに…)。

ちなみにMac用のバイナリエディタは\ `0xED`_\ を使いました。

.. _0xED: http://www.suavetech.com/0xed/0xed.html

.. |image0| image:: http://ktmtt.com/diary/wp-content/uploads/fa28dd70bfb40136d7434787e27728e8.png
   :target: http://ktmtt.com/diary/wp-content/uploads/fa28dd70bfb40136d7434787e27728e8.png
