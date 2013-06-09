PowerBookG4Ti 550Mhzが発掘されたのでDebianを入れた
##################################################
:date: 2010-05-04 21:35
:author: ka2n
:category: general
:tags: Debian, Linux
:slug: powerbookg4ti-550mhz-debian

自宅にサーバを建てることになって、黒柴とかSheevaPlugとか物色してたんですが、お財布が寂しい感じなので、家を捜索してPowerBook
G4 Titanium 550Mhz(Onyx)を発掘しました。こいつをサーバにしました。

初めは、FreeBSD/ppcに挑戦したんですが、fdiskが無いようでディスクのパーティショニングが面倒なので保留。
debian-504-powerpc-netinst.iso(180MB)をCDに焼いて、内蔵CD-ROMドライブからC起動します。勝手にOpenFirmwareからブートローダが呼び出されるので'install
G4'でインストーラーを起動します。(plain
optionってそのままコマンドに続けて書けばいいの？)

パーティショニング→コア部分のインストール→その他の部分のインストール(tasksel)。…のはずなんですが、内蔵CD-ROMドライブが腐っていたらしく(文字通り腐食?)taskselにたどり着くか着かないかぐらいのところでエラーになります。インストーラーがCDを見失ってくれます。USB接続のドライブで試しましたがこちらも途中で見失う。USBメモリも同様。FireWireなら確実なんだろうけど、ケーブルが見当たらない…ので仕方なく他のインストーラーで試します。

netinstよりさらに軽量のdebian-504-powerpc-businesscard.iso(40MB)でなんとかインストールが完了。あとちょっとで失敗するところだった。なんかドライブがガチャガチャ音がしはじめてたし。インストール後はaptitudeさんに頼んでアップデートしたり、SSHやらなにやら入れておきました。lennyではPowerpc-utilsがうまく動かないためにディスプレイを閉じても煌々とバックライトが点灯したままで、非常に勿体無いんですがどうにもならず、lennyからsqueezeにアップデート。するとうまく省電力機能が働いてディスプレイがちゃんと消えるようになりました。あとはトンネル掘れるようにSSH入れて、DynDNSにお世話になったりして、無事構築が完了。めでたしめでたし。


http://old.nabble.com/yaboot-failure-on-external-drive-td28061025.html

http://www.debian.org/releases/3.1/powerpc/ch05s01.html.ja#boot-newworld
