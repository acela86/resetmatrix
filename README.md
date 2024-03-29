# resetmatrix

本スクリプトは、新しいLEDパネルの一部で発生する「まったく表示されない」あるいは「表示が崩れる」事象について対策を行うものです。

事象の詳細については参考ページ1をご覧ください。

# 動作環境

本スクリプトは、**Adafruit RGB Matrix + Real Time Clock HAT for Raspberry Pi**を搭載したRaspberry Piでの使用を前提としています。 LEDパネルとの接続に他の基板を使用している場合は、配線が異なるためスクリプトの修正が必要となります。

また、LEDパネルの制御ライブラリとして`rpi-rgb-led-matrix`を使用しているものとします（本スクリプトの実行には必要ありません）。

# 対象となるLEDパネル

**HUB75規格に準拠した縦32ドットのLEDパネル**のうち、写真のように**FM6126A**という型番のICが裏面に実装されているものが対象となります。**2018年10月以降の製造品**に使用されていることが多いようです。

![FM6126A](https://user-images.githubusercontent.com/46576737/58851127-77b6e200-865f-11e9-9b95-0f9b3cb7c561.jpg)

縦64ドットのLEDパネルについては、事象の発生有無を含めて未検証です。

# 事象の原因

LEDパネルの制御に使用されるICが汎用シフトレジスタから専用品（FM6126A）に変更され、適切な初期化処理が必要となったためです。

専用品にはLEDパネルに特化した機能（明るさ制御機能・ちらつき防止機能など）が追加されて「賢く」なっていますが、使用前にこれらの機能の設定を行う必要が生じました。従来のプログラムではこの点が考慮されておらず、事象発生の原因となっていました。

# 対策の内容

FM6126Aの初期化処理として、明るさの設定値を所定のレジスタに書き込みます。
公式データシート（参考ページ3）にはレジスタ定義の詳細が載っていないため、設定値については対策発案者（参考ページ1・2）によるものを使用しています。

# 使用準備

1. 本レポジトリをクローンします。

2. クローンしたディレクトリ内で以下のコマンドを実行し、スクリプトに実行権限を付与します。
```bash
chmod u+x *.py
```

# 使用方法

クローンしたディレクトリ内で以下のコマンドを実行します。
電源を切ると設定がリセットされてしまうので、Raspberry Piの起動時に毎回必ず実行してください。

```bash
sudo ./resetmatrix.py width
```

`width`にはLEDパネルの横幅を指定します。 E233系の側面行先LEDの場合は`128`となります。

コマンドの実行が完了したら従来通り使用できます。

# 問い合わせ

Twitterアカウント（[@acela86](https://twitter.com/acela86)）にリプライまたはDMをいただければ対応します。

なお、本ソフトウェアと直接関係のない基本的な事項（ファイル操作など）についてはお答えできない場合があります。

# 免責事項

本ソフトウェアの使用により生じたいかなる損害に関して、作者は一切の責任を負いません。

# ライセンス

本スクリプトは [GNU General Public License Version 2.0](http://www.gnu.org/licenses/gpl-2.0.txt) の下で公開されています。詳細はLICENSEをご覧ください。 (This software is released under the GNU General Public License Version 2.0, see LICENSE.)

# 参考ページ

1. [rpi-rgb-led-matrixレポジトリで報告されたIssue（英語）](https://github.com/hzeller/rpi-rgb-led-matrix/issues/746)

2. [対策発案者のブログ（英語）](http://bobdavis321.blogspot.com/2019/02/p3-64x32-hub75e-led-matrix-panels-with.html)

3. [公式データシート（中国語）](http://www.superchip.cn/Private/ProductFiles/636709864216932389822770434.pdf)