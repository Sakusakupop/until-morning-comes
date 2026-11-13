# Until Morning Comes

Unity で作っているゲームのプロジェクトです。

## 作業を始める

1. Unity Hub で Unity `6000.3.20f1` をインストールします。  
2. Unity Hub から、このリポジトリの `until-morning-comes` フォルダを開きます。  
   `Assets`、`Packages`、`ProjectSettings` が入っているフォルダです。  
3. 初回起動時は Unity が必要なパッケージを読み込みます。読み込みが終わるまで待ちます。  

Unity のバージョンは [ProjectVersion.txt](until-morning-comes/ProjectSettings/ProjectVersion.txt) に記録されています。  

## シーンを再生する

1. Unity の Project ウィンドウで `Assets/Scenes/SampleScene.unity` を開きます。  
2. 画面上部の再生ボタンを押すと、シーンを実行できます。  

このシーンはビルド時に使うシーンにも登録されています。

## フォルダの役割

- `until-morning-comes/Assets`：シーン、画像、音声など、ゲームで使うファイルを置きます。
- `until-morning-comes/Packages`：Unity で使う追加機能を管理します。  `manifest.json` は使う機能、`packages-lock.json` は実際に使うバージョンを記録します。どちらも Git で管理します。
- `until-morning-comes/ProjectSettings`：Unity のバージョンやプロジェクト設定を保存します。  
- `.editorconfig`：C# の書き方や改行など、エディターの設定を揃えます。  

※ ここは随時更新します。

## ファイルを変更するとき

Assets 内のファイルには、同じ名前に `.meta` が付いたファイルが一緒に作られます。  
Unity がファイルを見分け、シーンなどとのつながりを保つために使うので、Assets のファイルを移動・削除するときは `.meta` も一緒に扱ってください。  
**Unity の Project ウィンドウから操作すると安全です。**  

`Library`、`Temp`、`Logs` などは Unity が作り直せる作業用ファイルです。  
Git には登録しません。必要な除外設定は `until-morning-comes/.gitignore` にあります。  

## C# の書き方

C# のインデント、改行、名前の付け方は、リポジトリ直下の `.editorconfig` に合わせます。  
対応しているエディターでは、入力中の書式案内や警告にこの設定が使われます。  
