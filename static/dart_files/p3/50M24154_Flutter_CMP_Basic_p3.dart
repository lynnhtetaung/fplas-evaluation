import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    const title = 'Exercise 3 - Vertical ListView';

    return MaterialApp(
      title: title,
      home: Container(
        decoration: BoxDecoration(
          border: Border.all(
            color: Colors.black, // 外枠の色
            width: 10.0, // 外枠の幅
          ),
        ),
        child: Scaffold(
          appBar: AppBar(
            title: const Text(title),
            backgroundColor: Colors.blue,
            titleTextStyle: const TextStyle(
              color: Colors.white, // AppBarのタイトル色
              fontWeight: FontWeight.bold, // AppBarのタイトルの太さ
              fontSize: 30, // AppBarのタイトルのサイズ
            ),
          ),
          body: Center(
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 20.0), // 左右の余白のみ設定
              child: ListView(
                shrinkWrap: true, // 必要なスペースだけ使用
                children: <Widget>[
                  Container(
                    height: 150,
                    width: 150,
                    color: Colors.red,
                    alignment: Alignment.center,
                  ),
                  const SizedBox(height: 0), // 各コンテナの間隔
                  Container(
                    height: 150,
                    width: 150,
                    color: Colors.white,
                    alignment: Alignment.center,
                  ),
                  const SizedBox(height: 0), // 各コンテナの間隔
                  Container(
                    height: 150,
                    width: 150,
                    color: Colors.blue,
                    alignment: Alignment.center,
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
