import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title:Text('What is your favorite song?'),
          ),
          body: Center(
          child: TextField(
            decoration: InputDecoration(
              labelText: '好きな曲を入力してください',
              border: OutlineInputBorder(),
            ),
          ),
        ),
      ),
    );
  }
}