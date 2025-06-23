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
          title:Text('Little Glee Monster'),
        ),
        body: Center(
          child: Text(
            'アサヒ',
            style: TextStyle(
              fontSize: 24,
              fontWeight: FontWeight.bold,
              color: Colors.yellow,
            ),
          ),
        ),
      ),
    );
  }
}