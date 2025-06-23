import 'package:flutter/material.dart';

void main(){
  runApp(MyApp());
}

class MyApp extends StatefulWidget{
  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp>{
  bool _isChecked = false;
  
  @override
  Widget build(BuildContext context){
    return MaterialApp(
      home: Scaffold(
        body: Center(
          child: CheckboxListTile(
            title: Text('Check me'),
            value: _isChecked,
            onChanged: (bool? value){
              setState((){
                _isChecked = value ?? false;
              });
            },
            controlAffinity: ListTileControlAffinity.leading,
            activeColor: Colors.blue,
            checkColor: Colors.red,
          ),
        ),
      ),
    );
  }
}