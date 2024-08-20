# LLM ローカル環境セットアップ

## 目次

- [はじめに](#はじめに)
- [前提条件](#前提条件)
- [インストール](#インストール)
- [使用方法](#使用方法)
- [設定](#設定)
- [トラブルシューティング](#トラブルシューティング)
- [今後の課題](#今後の課題)
- [参考文献](#参考文献)

## はじめに

日経ソフトウェア9月号 特集1 ローカルLLM入門 の記事を実際に試した結果を記録するものです。

このドキュメントでは、ローカル環境でLarge Language Model（LLM）をセットアップし、実行するための手順と考慮すべき事項を説明します。

本学習の目的は、LLMのローカル環境でのデプロイメントと管理に関する実践的な経験を積むことです。

## Part1 LLMをローカル環境で動かす方法

- LLMのファイル https://huggingface.co/models

### LLM選定のポイント

- .gguf形式 : ファイル形式、使われることが多い
- パラメータ数 : ニューラルネットワークの状態を示す値の数
- 量子化ビット数 : パラメータの値の量子化サイズ　大きいほど精度が高いがサイズが増える

### LLMプラットフォーム

- Jan
  - https://jan.ai/

### Fugaku-LLM

- https://huggingface.co/mmnga/Fugaku-LLM-13B-instruct-gguf

### LLM server

- pythonプログラムはWSL2上で実行
- LLM serverはホスト側で起動 IPは0.0.0.0

```bash
pip install openai
```

#### Fugaku-LLM-13B-instruct-Q3_K_S.gguf での実行結果

##### 1回目

```text
プログラミン言語を2つに分類すると、インタープリタ言語とコンパイル言語に分けられます。インタープリタ言語は、ソースコードを実行時に機械語に変換します。コンパイル言語は、ソースコードを実行前に機械語に変換します。Pythonはインタプリタ言語であり、Javaはコンパイル言語です。<EOD|LLM-jp>
```

##### 2回目

```text
プログラミンング言語には、インタプリタ型言語とコンパイル型言語の2種類があります。
- インタプリタ型言語：インタープリタ型言語：実行時にインタプリタによって一行ずつコードが実行される。インタプリタはソースコードからデータを機械語に翻訳する。Java、Python、Rubyなどが有名。
- コンパイル型言語：ソースコードを実行する前に、コンパイラによってコードが機械語に翻訳される。CやC++などが有名。
一般的に、コンパイルされた言語はインタプリタ型言語よりもパフォーマンスが高く、複雑なコードを書くことができる。しかし、コンパイルプロセスはインタプリタプロセスよりも多くのリソースを必要とする。<EOD|LLM-jp>
```

##### 3回目(temperature=0.0)

```text
プログラミンング言語を2つのカテゴリーに分類すると、コンパイラ型言語とインタプリタ型言語に分けることができます。
# コンパイラ型言語
# - Java
# - C++
# - Rust
# - Go
# インタプリタ型言語
# - Python
# - Ruby
# - JavaScript
# - PHP
# さらに、スクリプト言語やローレベル言語など、その他のカテゴリーに分類されるプログラミング言語もあります。

これらの分類は、プログラミング言語が実行される方法に基づいています。コンパイラ型言語は、ソースコードを（通常は）アセンブリに変換するコンパイラでコンパイルされます。一方、インタプリタ型言語はソースコードを一行ずつ実行し、その場で結果を表示する。

もう一つの分類法は、開発者のコミュニティによって開発された標準やライブラリに基づいている。例えば、C++やJavaはオブジェクト指向言語であり、RustやGoは関数型言語である。PythonやRubyはインタプリタ型言語であり、JavaScriptやPHPはスクリプト言語である。

プログラミング言語を分類する方法は他にもたくさんあります。どのような分類法を用いるにせよ、重要なのは、それぞれの言語がどのように使われ、どのような特徴を持っているかを理解することです。<EOD|LLM-jp>
```

##### 4回目(temperature=0.0)

```text
プログラミンング言語を2つのカテゴリーに分類すると、コンパイラ型言語とインタプリタ型言語に分けることができます。
# コンパイラ型言語
# - Java
# - C++
# - Rust
# - Go
# インタプリタ型言語
# - Python
# - Ruby
# - JavaScript
# - PHP
# さらに、スクリプト言語やローレベル言語など、その他のカテゴリーに分類されるプログラミング言語もあります。

これらの分類は、プログラミング言語が実行される方法に基づいています。コンパイラ型言語は、ソースコードを（通常は）アセンブリに変換するコンパイラでコンパイルされます。一方、インタプリタ型言語はソースコードを一行ずつ実行し、その場で結果を表示する。

もう一つの分類法は、開発者のコミュニティによって開発された標準やライブラリに基づいている。例えば、C++やJavaはオブジェクト指向言語であり、RustやGoは関数型言語である。PythonやRubyはインタプリタ型言語であり、JavaScriptやPHPはスクリプト言語である。

プログラミング言語を分類する方法は他にもたくさんあります。どのような分類法を用いるにせよ、重要なのは、それぞれの言語がどのように使われ、どのような特徴を持っているかを理解することです。<EOD|LLM-jp>
```

### チャットAIのWebサイトを構築

```bash
pip install chainlit
```

```bash
chainlit run server_test2.py 
```

## Part2 ラズパイ５でLLMを動かす

### TinyLlama

- https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/blob/main/tinyllama-1.1b-chat-v1.0.Q8_0.gguf

### llama-cpp-python

```bash
pip install llama-cpp-python
```

## 前提条件

開始する前に、以下のものがマシンにインストールされ、設定されていることを確認してください:
- [ ] **Python 3.11.1以上**: LLMを実行するためのプログラミング言語。
- [ ] **GPU（推奨）**: 大規模な計算リソースを必要とするモデルを扱う場合に推奨されます。
- [ ] **Docker**: コンテナ化されたデプロイメントに必要です（該当する場合）。
- [ ] **Git**: リポジトリをクローンするためのバージョン管理システム。
- [ ] **WSL2**: Windowsで

## インストール
### ステップ 1: リポジトリをクローン
```bash
git clone <repository-url>
cd <repository-directory>

python -m venv llm_env
source llm_env/bin/activate  # Windowsの場合は `llm_env\Scripts\activate`
