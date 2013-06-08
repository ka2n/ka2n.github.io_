Twenty Tenの子テーマのカスタムヘッダーを無効にする方法 
#######################################################
:date: 2011-07-10 01:48
:author: ka2n
:category: general
:tags: Tips, wordpress
:slug: twenty-ten

WordPressのデフォルトテーマであるTwenty
Ten。新しいテーマを作るときはこいつを継承して"子テーマ"として作成するのがヨサゲなようです。

| Twenty
Tenにはヘッダーに大きなアイキャッチ画像があります。カスタムヘッダー機能を使えばテーマの編集なしにWordPressの管理画面から変更する事ができます。
|  |Twenty Ten|

| ただヘッダーにアイキャッチ画像が必要ない場合もあるので、こんな感じで実際の出力から消すことができます。\ `ヘッダーの画像を消す
\| ちょっとメモしときます。 http://tortoise.workarea.jp/?p=158
`_
|  |image1|

| こんな具合で消すわけですが、管理画面には依然としてメニューとその先の画面が残ります。
|  |image2|
|  気持ちが悪いので消しましょう。

| WordPress3.1から\ **remove\_custom\_image\_header**\ という関数が追加されているようなのでこれを使用します。
|  `http://codex.wordpress.org/Custom\_Headers
`_

| 参考までにTwenty
Tenのfunctions.phpでカスタムヘッダー機能を追加している部分
|  [code language="php"]
|  // Add a way for the custom header to be styled in the admin panel
that controls
|  // custom headers. See twentyten\_admin\_header\_style(), below.
|  add\_custom\_image\_header( '', 'twentyten\_admin\_header\_style' );
|  [/code]

| こいつを子テーマのfunctions.phpで無効にしてやりましょう。
|  [code language="php"]
|  if ( !function\_exists( 'child\_theme\_init' ) ) {
|  function child\_theme\_init() {
|  remove\_custom\_image\_header();
|  }
|  }
|  add\_action('init', 'child\_theme\_init');
|  [/code]
|  こんな感じです。

| initに新たに定義したchild\_theme\_init関数をフックして呼び出される様にします。
| 
子テーマから親テーマの機能を変更する際にはafter\_setup\_themeにフックする場合が多いみたいですが、こっちだと上手くいきませんでした。
|  テーマの設定は
|  子テーマのfunctions.php -> 親テーマのfunctions.php ->
after\_setup\_theme -> init
| 
の順番で呼ばれます。今回無効にしたかったadd\_custom\_image\_headerはTwenty
Tenのfunctions.phpの中で定義されている\ **twentyten\_setup**\ という関数の中に書かれています。

| そして、以下のようにフックされています。
|  [code language="php"]
|  /\*\* Tell WordPress to run twentyten\_setup() when the
'after\_setup\_theme' hook is run. \*/
|  add\_action( 'after\_setup\_theme', 'twentyten\_setup' );
|  [/code]
|  after\_setup\_themeにフックされています。

| 子テーマのfunctions.php ->
親テーマのfunctions.phpという順番で読み込まれますので、実行順は..
|  子テーマのafter\_setup\_themeへフックされた関数 ->
親テーマのafter\_setup\_themeへフックされた関数
| 
となり、子テーマのafter\_setup\_themeでremove\_custom\_image\_headerを呼びだそうが、その後にadd\_custom\_image\_headerが設定されてしまうので、カスタムヘッダーを無効にすることができませんでした。そこで更に後に呼び出されるinitにフックしたというわけです。

| |image3|
|  これで管理画面からも消えました。

.. _`ヘッダーの画像を消す \| ちょっとメモしときます。 http://tortoise.workarea.jp/?p=158
`: http://tortoise.workarea.jp/?p=158
.. _`http://codex.wordpress.org/Custom\_Headers
`: http://codex.wordpress.org/Custom_Headers

.. |Twenty Ten| image:: http://ktmtt.com/diary/wp-content/uploads/tt-300x172.png
   :target: http://ktmtt.com/diary/wp-content/uploads/tt.png
.. |image1| image:: http://ktmtt.com/diary/wp-content/uploads/tt2-300x170.png
   :target: http://ktmtt.com/diary/wp-content/uploads/tt2.png
.. |image2| image:: http://ktmtt.com/diary/wp-content/uploads/ch-300x134.png
   :target: http://ktmtt.com/diary/wp-content/uploads/ch.png
.. |image3| image:: http://ktmtt.com/diary/wp-content/uploads/ch21.png
   :target: http://ktmtt.com/diary/wp-content/uploads/ch21.png
