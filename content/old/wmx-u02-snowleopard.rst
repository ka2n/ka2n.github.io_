WMX-U02がSnowLeopardで使えない…かと思ったら使えた件
####################################################
:date: 2010-04-12 06:00
:author: ka2n
:category: general
:tags: Mac, WiMAX
:slug: wmx-u02-snowleopard

WiMAXを使ってみたくて、オークションでWMX-U02(WMX-U01のDTI縛りの物)を買ってきたんですが、なかなか繋がらない。環境はMacOSX
10.6.3。旧ファーム(4.6.1.0-21597)だとデバイスは認識されるが、その後ユーティリティで認識されない。最新ファーム(4.6.1.9-23717)だとデバイス自体が認識されない。(HardwareGrowlerで見たところ接続したり切断されたりを繰り返す)。

|image0|

んで、試行錯誤の末認識できたので解決法。

| [code lang="plain"]<strong>system.log</strong>
|  10/04/09 21:41:55 com.apple.kextd[10] Can't load
/System/Library/Extensions/WMX-U\_kthp.kext - no code for running
kernel's architecture.
|  10/04/09 21:41:55 com.apple.kextd[10] Failed to load
/System/Library/Extensions/WMX-U\_kthp.kext - (libkern/kext) requested
architecture/executable not found.
|  10/04/09 21:50:10 com.apple.kextd[10] Can't load
/System/Library/Extensions/WMX-U\_storage.kext - no code for running
kernel's architecture.
|  10/04/09 22:12:33 com.apple.kextd[10] Failed to load
/System/Library/Extensions/WMX-U\_storage.kext - (libkern/kext)
requested architecture/executable not found.
|  10/04/09 21:53:35 com.apple.kextcache[594]
/System/Library/Extensions/WMX-U\_kthp.kext doesn't support architecture
x86\_64; omitting from prelinked kernel.
|  10/04/09 21:53:35 com.apple.kextcache[594]
/System/Library/Extensions/WMX-U\_storage.kext doesn't support
architecture x86\_64; omitting from prelinked kernel.
|  [/code]

とエラーが出て、インストールされているはずのドライバの読み込みに失敗している模様。カーネルを64bitで動かしているからみたいですね…

仕方ないので32bitで起動し直します。(\ `64bit 32bit snowleopard - Google
検索`_)

`|image1|
`_\ |image2|

成功！！

| 旧ファームで成功したので、3/17の最新ファームにWindows機でアップデートしてみて確認。
|  |image3|

| うん。IODATAさんにはWMX-Uシリーズの64bit対応ドライバも作っていただきたい。
| 
ちなみに、未だ契約しておりませんのでインターネッツには飛び出せません(笑)

.. _64bit 32bit snowleopard - Google 検索: http://www.google.co.jp/search?hl=ja&q=64bit+32bit+snowleopard
.. _|image4|
: http://ktmtt.com/diary/wp-content/uploads/diswimax.png

.. |image0| image:: http://ktmtt.com/diary/wp-content/uploads/wmxud.png
   :target: http://ktmtt.com/diary/wp-content/uploads/wmxud.png
.. |image1| image:: http://ktmtt.com/diary/wp-content/uploads/diswimax-300x255.png
.. |image2| image:: http://ktmtt.com/diary/wp-content/uploads/32bitoldfirm-300x192.png
   :target: http://ktmtt.com/diary/wp-content/uploads/32bitoldfirm.png
.. |image3| image:: http://ktmtt.com/diary/wp-content/uploads/32bitnewfirm-300x191.png
   :target: http://ktmtt.com/diary/wp-content/uploads/32bitnewfirm.png
.. |image4| image:: http://ktmtt.com/diary/wp-content/uploads/diswimax-300x255.png
