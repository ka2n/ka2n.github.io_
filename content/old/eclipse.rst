Eclipseの日本語化
#################
:date: 2010-06-05 16:12
:author: ka2n
:category: general
:tags: Eclipse, Mac, Tips
:slug: eclipse

|image0|

無理してw英語で使っていても、やっぱり日本人、母国語でのUIを見るとなんだかほっとしてしまいます。

Eclipseを日本語化するにはPleiadesという知る人ぞ知るプラグインがありますね。

    プラグインフォルダにダウンロードしてきたPleiadesを入れて、eclipse.iniに追記して起動…あれ、英語のままだ…今度はホームフォルダに.eclipse/を作ってその中に、ん、あれ、おかしいぞ

という感じで、今まで、なかなかスムーズには日本語化できませんでした(俺だけ?)
こういう時だけはちょっと、All in oneで簡単に日本語化できるWindowsを羨ましいと思いますよね。

最近、Eclipseを新規にインストールする機会があったんですが、新しい方法を発見。今までのやり方とはちょっとだけ違う。なんとWindows用のPleiades
All in Oneを使用します。これを使用して、MacのEclipse 3.5
Galileoを日本語UIにします。

やり方
------

まず、おもむろに\ `Pleadesのダウンロードページ`_\ から\ **Eclipse 3.5 Galileo Pleades All in One**\ をダウンロードしてきます。中のPleadesを使用するだけなので、パッケージはC,C++用ので良いでしょう。

|image1|

ファイルを解凍後、
pleiades-e3.5-cpp\_xxxxxx/eclipse/dropins/MergeDocフォルダを/Applications/eclipse/dropins/ にコピーします。

|image2|

次にeclipse.iniの編集をします。
OSX用のEclipseのeclipse.iniの場所はEclipse.appのパッケージの中にあります。

具体的には、Eclipse.appを右クリックして「パッケージの内容を表示」> Contents > MacOS > eclipse.ini

|image3|

変更前

.. code-block:: text

    -startup
    ../../../plugins/org.eclipse.equinox.launcher_1.3.0.v20120522-1813.jar
    --launcher.library
    ../../../plugins/org.eclipse.equinox.launcher.cocoa.macosx.x86_64_1.1.200.v20120522-1813
    -showsplash
    org.eclipse.platform
    --launcher.XXMaxPermSize
    256m
    --launcher.defaultAction
    openFile
    -vmargs
    -Xms40m
    -Xmx512m
    -Xdock:icon=../Resources/Eclipse.icns
    -XstartOnFirstThread
    -Dorg.eclipse.swt.internal.carbon.smallFonts


最終行に(たぶん場所はどこでもいいかと思おもいます)

.. code-block:: text

    -javaagent:../../../dropins/MergeDoc/eclipse/plugins/jp.sourceforge.mergedoc.pleiades/pleiades.jar

を追記します。

変更後のeclipse.ini

.. code-block:: text

    -startup
    ../../../plugins/org.eclipse.equinox.launcher_1.3.0.v20120522-1813.jar
    --launcher.library
    ../../../plugins/org.eclipse.equinox.launcher.cocoa.macosx.x86_64_1.1.200.v20120522-1813
    -showsplash
    org.eclipse.platform
    --launcher.XXMaxPermSize
    256m
    --launcher.defaultAction
    openFile
    -vmargs
    -Xms40m
    -Xmx512m
    -Xdock:icon=../Resources/Eclipse.icns
    -XstartOnFirstThread
    -Dorg.eclipse.swt.internal.carbon.smallFonts
    -javaagent:../../../dropins/MergeDoc/eclipse/plugins/jp.sourceforge.mergedoc.pleiades/pleiades.jar

これで完了！Eclipseを起動してみて下さい。スプラッシュ画面が変わって、日本語で使えるはずです。
本当に簡単とは言えないんだけど、なんだかちょっとだけ簡単になった気がする！(単に1発で成功したからな気がする可能性大)

参考:
http://labs.uechoco.com/blog/2009/04/mac-eclipse-install-pleiades-japanese.html

.. _Pleadesのダウンロードページ: http://mergedoc.sourceforge.jp/

.. |image0| image:: http://ktmtt.com/diary/wp-content/uploads/7dd4c3f74f006b34bb1d70d7adebd54e.jpg
   :target: http://ktmtt.com/diary/wp-content/uploads/7dd4c3f74f006b34bb1d70d7adebd54e.jpg
.. |image1| image:: http://ktmtt.com/diary/wp-content/uploads/45e81c34fdfa826a47ccf139bbeb9b89.png
   :target: http://ktmtt.com/diary/wp-content/uploads/45e81c34fdfa826a47ccf139bbeb9b89.png
.. |image2| image:: http://ktmtt.com/diary/wp-content/uploads/be931dadb26198dede89dd53e6d63028-300x182.png
   :target: http://ktmtt.com/diary/wp-content/uploads/be931dadb26198dede89dd53e6d63028.png
.. |image3| image:: http://ktmtt.com/diary/wp-content/uploads/0d6d56aec3bcf4cb2ee00ccde379edfd.png
   :target: http://ktmtt.com/diary/wp-content/uploads/0d6d56aec3bcf4cb2ee00ccde379edfd.png
