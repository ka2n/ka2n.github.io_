「TitaniumのコードをGUIなしでエディタからすばやくbuildする」をやってみた
########################################################################
:date: 2010-11-26 13:50
:author: ka2n
:category: general
:slug: titanium-gui-build

| `TitaniumのコードをGUIなしでエディタからすばやくbuildする -
はこべにっき#`_
|  http://d.hatena.ne.jp/hakobe932/20101125/1290694032

これは便利そうなのでやってみる。

| https://gist.github.com/715378
|  からbuild.plを頂いてきて、

[code]$ perl ./buil.pl[/code]

ふむふむ、perlをまったくもっていじった事が無く、依存関係で入ったperlが動いてくれたんだけど、なにかのモジュールが足りないのかな。

| [code]Can't locate AnyEvent.pm in @INC (@INC contains:
/opt/local/lib/perl5/site\_perl/5.8.9/darwin-2level
/opt/local/lib/perl5/site\_perl/5.8.9 /opt/local/lib/perl5/site\_perl
/opt/local/lib/perl5/vendor\_perl/5.8.9/darwin-2level
/opt/local/lib/perl5/vendor\_perl/5.8.9
/opt/local/lib/perl5/vendor\_perl
/opt/local/lib/perl5/5.8.9/darwin-2level /opt/local/lib/perl5/5.8.9 .)
at build.pl line 4.
|  BEGIN failed--compilation aborted at build.pl line 4.
|  [/code]

一番重要であるだろうAnyEvent.pmがないっぽい。よく分からないけどCPANをそもそもいれてないな。

| [code]$sudo /opt/local/bin/cpan
|  .
|  (中略)
|  .
|  cpan[1] install AnyEvent[/code]

足りないようで

[code]cpan[2] install AnyEvent::HTTPD[/code]

よく分からないけど、YAMLが無いよっておっしゃるので

[code]cpan[2] install YAML[/code]

これだけ入れたら動きました。

[code]$ perl PROJECTROOT/build.pl[/code]

| を実行するとhttp://localhost:9090でサーバが動いてくれるので、
|  .vimrcに

[code]nnoremap <unique> <silent> <Leader>ti :call system('curl
http://localhost:9090/run &')<CR>[/code]

を追記して完了。

.. _TitaniumのコードをGUIなしでエディタからすばやくbuildする - はこべにっき#: http://d.hatena.ne.jp/hakobe932/20101125/1290694032
