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
          title:Text("押すなよ?"),
        ),
        body: Center(
          child: ElevatedButton(
            onPressed: (){
              print('ほんまに押してどうすんねん');
            },
            child: Text('押すなよ？押したらあかんからな？'),
          ),
        ),
      ),
    );
  }
}