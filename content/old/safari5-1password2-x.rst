Safari5で1Password2.xが動かない件
#################################
:date: 2010-07-02 06:02
:author: ka2n
:category: general
:tags: 1Password, Safari
:slug: safari5-1password2-x

| Safariのビルドナンバーを確認して、以下を書き換えれば動く
|  |image0|
|  [code]
| 
/Applications/1Password.app/Contents/Resources/SupportedBrowsers.plist
|  <key>Safari</key>
|  -<key>MaxBundleVersion</key>
|  --<string>ここをビルドナンバーより大きく</string>
|  [/code]

特別問題は起きていませんが、自己責任でお願いします。

| #追記
|  1Passwordのアプリを使うと元に戻ってしまいますね

.. |image0| image:: http://ktmtt.com/diary/wp-content/uploads/safari.png
   :target: http://ktmtt.com/diary/wp-content/uploads/safari.png
