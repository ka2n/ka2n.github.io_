VimperatorからPocketに投稿できるようにした
===========================================
:date: 2014-02-23
:author: ka2n
:slug: firefox-vimperator-pocket
:category: general
:tags: Firefox, Vimperator, Pocket

Pocketを使っているをよく見るのと、Mac用のアプリが良い感じだったのでInstapaperから乗り換えた。
元ReadItLator、デザインとブランディングは大切だなあ。あとユーザーの情報収集のスタイルがツールにマッチしたってのもあるだろう。
自分はVimperatorからPocketに投稿したかったので以下の方法で設定した。
``:clip`` で保存できるようになる。便利。

.vimperatorrcに以下を追加

.. code-block:: vimrc

    command clip echo RIL.addCurrent() !== false ? 'Success' : 'Failed (or already clipped?)'
   
`Pocketの拡張機能`_ をあらかじめFirefoxに入れておく。
   
.. _`Pocketの拡張機能`: https://addons.mozilla.org/en-US/firefox/addon/read-it-later/
