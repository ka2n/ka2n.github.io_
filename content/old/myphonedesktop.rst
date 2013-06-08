myPhoneDesktop
##############
:date: 2010-02-26 19:09
:author: ka2n
:category: general
:tags: iPhone, Mac
:slug: myphonedesktop

Twitterを眺めていてmyPhoneDesktopというiPhoneアプリケーションを見つけました。パソコンからSMSを送ったり、テキストだとか画像を送れます。PCのアプリケーションから、テキストなり画像なりを送信すると、myPhoneDesktopのサーバに送られて、iPhoneにはPNSでプッシュ通知されます。通知を開くと自動的にiPhone上のmyPhoneDesktopが起ち上がり、情報を取得します。ちなみに母艦とiPhoneが同じネットワーク上にいる必要はありません。デスクトップクライアントは、Snow
Leopard/Leopard, Windows, Linuxに対応。ブラウザー上からでも可能です。

長文を打ったり、ちょっとした画像の受け渡しに便利です。

| `iPhone on your Desktop \| myPhoneDesktop`_
|  `myPhoneDesktop`_\ (iTunesが開きます)

Tips:myPhoneDesktopのクライアントアプリケーションをDockから隠す(Mac)
--------------------------------------------------------------------

myPhoneDesktopのデスクトップクライアントは起動すると、メニューバーに常駐します。なのでDockに表示されるアイコンはなくても困らないので、非表示にしたい。LSUIElementをInfo.plistに加えてみた所、Dockのアイコンは表示されなくなったものの、アプリケーションのウィンドウがXボタンを押しても閉じられなくなってしまいました。

myPhoneDesktopのデスクトップクライアントは<閉じる>動作を普通のアプリケーションで言う<隠す>で実装してるみたい。どうしてもDockに表示したく無い場合は、以下の方法(LSUIElement)でDockから消して、ウィンドウは\ **Command
+ H**\ で消す。という使い方になります。

(myPhoneDesktopのデスクトップクライアントでは使えませんが)大抵のアプリケーションで使える、「Dockからアイコンを消す」方法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

任意のエディタ : myPhoneDesktop.app > Contents > Info.plist

| [code lang="plain"]
|  <key>LSUIElement</key>
|  <string>1</string>
|  [/code]

もしくは

Property List Editor.app : Info.plist

| [code lang="plain"]
|  >Add Item
|  Key : Application is agent (UIElement)
|  Value : チェックボックスをチェックする
|  [/code]

.. _iPhone on your Desktop \| myPhoneDesktop: http://www.myphonedesktop.com/
.. _myPhoneDesktop: http://itunes.apple.com/jp/app/id352226779?mt=8
