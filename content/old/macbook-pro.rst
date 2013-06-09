MacBook Proを買ってやったこと
#############################
:date: 2010-03-02 02:33
:author: ka2n
:category: general
:tags: Mac, Tips
:slug: macbook-pro

年明けにMacBook
Proのいちばんお手頃なやつを買ったので、セットアップしたときのメモです。

| Macbook Pro
|  2.26 GHz Intel Core 2 Duo
|  4 GB 1067 MHz DDR3
|  US keyboard

Shift+2でアットマーク打ちたいんだぜ！

#. 開封
#. 起動
#. とりあえずリストア
#. ソフトのインストール
#. 設定変更


--------------

1.開封
~~~~~~

まず裸になります。つぎに(ry

2.起動
~~~~~~

右上の電源ボタンをポチッとな、と。一応動作確認的な感じ。

3.とりあえずリストア
~~~~~~~~~~~~~~~~~~~~

最初の状態だといらない言語とか入っていて、自分には不要なのでついてきたリカバリーディスクで自分の好きな構成でいれなおします。iPhotoはいるけどiMovieとかいらないので。あと、Xcodeが見当たらなかったのであとからネットから入れました。

4.ソフトのインストール
~~~~~~~~~~~~~~~~~~~~~~

`1Password`_
    パスワード管理ツール。前の環境でも入れていて便利だったので。Google
    Chromeに対応していないので必要なときはSafariを起動しなきゃいけない。設定ファイルをDropBoxで同期しているフォルダに移して元の場所にシンボリックリンクをはってあります。
`Alarm Clock`_
    たまに使う目覚まし時計。
`BetterTouchTool`_
    MacBook
    Proはマルチタッチで操作ができるので便利です。そこに自分で決めたジェスチャを追加出来る。4本指スワイプでSpacesの切り替えとか。3本指スワイプでブラウザでのタブ移動とか。
`ClamXav`_
    アンチウィルスソフト
`CotEditor`_
    テキストエディタです。シンプルで使い易い。
`Cyberduck`_
    そこまで使い易いとは思わないけど、FTPとかSFTPとかWebDAVとかに接続するときに使用。
`Dropbox`_
    書類とか特定の設定ファイルをここに入れて同期してます。Ubuntuだと元ファイルからシンボリックリンクをはれば良かったのだけど、OSXだと同期されないようなので元ファイルを同期するフォルダに入れて、本来の場所にシンボリックリンクをはって使っています。
`Firefox`_
    FireBugとかScrapBookとか便利なので、たまに使う。
`Google Chrome`_
    メインブラウザ。Vimlike
    Smoozieeをちょっと改造して入れて使ってます。その他には大して拡張は入れてない。
`Google Quick Search Box`_
    QucikSilverの代わり。Spotlightは使わないでこっちを使用しています。Twitterにもつぶやけるし。
`Google 日本語入力`_
    ATOKとか持ってないので使っています。
    若干専門用語的なものでも変換出来るので嬉しい。
`iPhoneTunnel`_
    iPhoneにSSHとかSFTPでつないでCyberduckでファイル転送したりします。
`MacPorts`_
    みんな入れてるから入れてみた。apt-get install
    xxx的な事ができるぞ！でもやたらとPython入れる気がするんだけど気のせい？
    slを入れたくらい。
`MacVim-kaoriya`_
    ターミナルから直にVim使いたいんだけど、imなんたらの挙動が気にくわないのでgvim的なMacVimを使っています。Vim使い出したのは、それっぽくてカッコいいから。
`MindNode`_
    そーんなに使わないけど、シンプルなマインドマップ作成アプリ。すっきりしてて良いです。
`Nocturne`_
    なんか画面がすごいことになります。暗くても目に優しい。OS標準で似たような事ができたと思ったけど、たいていそのショートカットを忘れるので、アプリを使用。
`OnyX`_
    設定＆メンテナンスツール
`OOo`_
    OpenOffice.orgです。Go ooの方を使用。
`The Unarchiver`_
    アーカイバ。もう一回入れたら溶け込んじゃって使ってることを気づかないくらい重宝してます。
`VirtualBox`_
    最初はプログラミングは仮想環境のUbuntuでやろうと思ってたので入れました。今はWindowsでタイプウェルをやるためのソフトと化しています。
`VoodooPad`_
    使い込んではないけど、なかなか便利なメモアプリケーション。
`XAMPP`_
    ローカルにWordpress入れたりXOOPSで遊んだりPHP書いて試したり遊ぶためにインストール。
`夜フクロウ`_
    Twitterクライアント
`0xED`_
    バイナリエディタ。とりあえずインストール。ResEditとかまた使ってたいな。
`32 - or 64 Kernel Startup Mode Selector`_
    そのままだと、32bitでOSが動いてるらしいので64bitで動くように設定を変えるユーティリティ。まぁ気分です。
`AppCleaner`_
    ファイルのアンインストール時に離れた場所にある設定ファイルも一緒に捨ててくれます。
`DelayedLauncher`_
    ログイン項目に登録しておいて、ちょっと遅れてアプリを起動させてくれます。
`Disk Inventory X`_
    ディスクの使用容量を視覚的に表示。
`dolipo`_
    プロクシソフトのGUI版
`MiniBatteryLogger`_
    バッテリー容量の推移を記録してくれる。ただ、起動時に写真を撮ったようなカシャっとした音が鳴るのが嫌。
`SMARTReporter`_
    ディスクのS.M.A.R.T.情報を監視してなにかあったときに警告してくれる。らしい。
`AppleJack`_
    なにかあって通常起動しなくなったときに、シングルユーザーモードでメンテナンスをしてくれる。
`Growl`_
    いろいろ通知してくれる。TwitterのTL更新とかSkypeのチャットとかいろいろ知らせてくれる。iTunesで曲が変わったとき(Google
    Quick Serch Boxのプラグイン経由)にも教えてくれます。
`Secrets`_
    若干OnyXと機能は被ってるけど、アプリやOSの隠された設定を変更出来るユーティリティ。
`Perican`_
    QuickTimeでいろんな形式の動画を見るために使用。けどVLC使っちゃうからあんまり重宝していない。
`StartupSound.prefPane`_
    起動音いらないのでこれで消しています。聞きたくなったらたまに解除。
`Deep Sleep`_
    シャットダウンするよりDeepSleepしたほうが作業にすぐ戻れるのでおすすめ。
`CoolBook`_ (2010/3/31追加)
    CPUの電圧を下げたり、クロック周波数の動き方を設定できるアプリ。同じクロック周波数でも電圧を下げて、省エネ省エネ。
    `**CoolBookでの現在の設定を公開しました。**`_
`SymbolicLinker`_ (2010/3/31追加)
    シンボリックリンクを作成する機能をFinderに追加するプラグイン。
`SmartSleep.prefPane`_ (2010/3/31追加)
    通常のスリープのまま放ったらかしにしておくと、電池が勿体無いので、一定時間スリープをし続けるとDeep
    Sleepに移行するようにしてくれる。

5.設定変更
~~~~~~~~~~

ここは特に人それぞれなので自分の忘備録として

Caps LockをCtrlに置換
    システム環境設定 > キーボード > 修飾キー　でCapsLockキーをCtrlキーに変更
Dockは左へ
    画面が狭いので
Exposeの設定
    画面のコーナーへの機能の割り当て > ??左上:デスクトップ
    右上:全てのウィンドウ 左下:Spaces 右下:スクリーンセーバー
Spacesの設定
    縦3 ×
    横3に。上段を作業に、中段をブラウジングとiTunes,Skypeなど、下段は基本開けておいて必要があればそこも使う。
セキュリティ
    安全な仮想メモリを使用のチェックを外す。こうしておかないとDeepSleepから戻ってこれなくなった気がする。
トラックパッド
    どれもだいたい8割くらいに設定。マルチタッチの設定はBetterTouchToolでするので変更しない。3本指は有効になっていなかったら有効にする。
Terminal.appの設定
    ProでMonaco 12pt.
    アンチエイリアス、179,54のウィンドウサイズに。システム環境設定 >
    アカウント > (アカウント名のところでCtrl + クリック)
    詳細オプションで、「ログインシェル」を/bin/zshに変更。(なんかよくわかんないけどとんがった人たちがzshに変えてるから！）??MacPortとかのコマンドが使えなくなったのでzshの設定でパスを通す。

BetterTouchToolの設定
~~~~~~~~~~~~~~~~~~~~~

`BetterTouchTool(SecondBar & BetterTouchTool Blog)`_

-  Global
    Five Finger Tap: Show DashBoard
    Four Finger Click:Show Spaces
    Four Finger Swipe Left: Ctrl+ ← (Spacesで左移動)
    Four Finger Swipe Right: Ctrl + → (Spacesで右移動)
-  Google Chrome
    Three Finger Swipe Left: Command + Option + ← (タブの左移動)
    Three Finger Swipe Right: Command + Option + → (タブの右移動)
    Two Finger TipTap Middle: Command + W (タブを閉じる)

こんな感じで2ヶ月強使ってます。

.. _1Password: http://agilewebsolutions.com/products/1Password
.. _Alarm Clock: http://www.robbiehanson.com/
.. _BetterTouchTool: #bettertouchtool
.. _ClamXav: http://www.clamxav.com/
.. _CotEditor: http://www.aynimac.com/p_blog/
.. _Cyberduck: http://cyberduck.ch/
.. _Dropbox: https://www.dropbox.com/
.. _Firefox: http://mozilla.jp/firefox/
.. _Google Chrome: http://www.google.com/chrome/?hl=ja
.. _Google Quick Search Box: http://code.google.com/p/qsb-mac/
.. _Google 日本語入力: http://www.google.co.jp/intl/ja/ime/index-mac.html
.. _iPhoneTunnel: http://web.me.com/novi.mad/page2/page2.html
.. _MacPorts: http://www.macports.org/
.. _MacVim-kaoriya: http://code.google.com/p/macvim-kaoriya/
.. _MindNode: http://www.mindnode.com/
.. _Nocturne: http://docs.blacktree.com/nocturne/nocturne
.. _OnyX: http://www.titanium.free.fr/
.. _OOo: http://go-oo.org/
.. _The Unarchiver: http://wakaba.c3.cx/s/apps/unarchiver.html
.. _VirtualBox: http://www.virtualbox.org/
.. _VoodooPad: http://flyingmeat.com/voodoopad/
.. _XAMPP: http://www.apachefriends.org/jp/xampp-macosx.html
.. _夜フクロウ: http://sites.google.com/site/yorufukurou/
.. _0xED: http://www.suavetech.com/0xed/0xed.html
.. _32 - or 64 Kernel Startup Mode Selector: http://www.ahatfullofsky.comuv.com/English/Programs/SMS/SMS.html
.. _AppCleaner: http://www.freemacsoft.net/AppCleaner/
.. _DelayedLauncher: http://www.taoeffect.com/blog/2008/12/delayedlauncher-coming-to-an-espionage-near-you/
.. _Disk Inventory X: http://www.derlien.com/
.. _dolipo: http://drikin.com/dolipo/
.. _MiniBatteryLogger: http://www.emeraldion.it/software/macosx/minibatterylogger.html
.. _SMARTReporter: http://www.corecode.at/smartreporter/
.. _AppleJack: http://applejack.sourceforge.net/
.. _Growl: http://growl.info/
.. _Secrets: http://secrets.blacktree.com/
.. _Perican: http://perian.org/
.. _StartupSound.prefPane: http://www5e.biglobe.ne.jp/~arcana/
.. _Deep Sleep: http://www.axoniclabs.com/DeepSleep/
.. _CoolBook: http://www.coolbook.se/
.. _**CoolBookでの現在の設定を公開しました。**: http://ktmtt.com/diary/2010-coolbook-settings-for-macbookpro5-5.html
.. _SymbolicLinker: http://seiryu.home.comcast.net/~seiryu/symboliclinker.html
.. _SmartSleep.prefPane: http://www.jinx.de/SmartSleep.html
.. _BetterTouchTool(SecondBar & BetterTouchTool Blog): http://blog.boastr.net/
