import 'package:flutter/material.dart';

void main(){
  runApp(MyApp());
}

class MyApp extends StatefulWidget{
  @override
  State<MyApp> createState() => _MyAppStateInternal();
}

class _MyAppStateInternal extends State<MyApp>{
  String? _selectedValue = 'A';
  
  @override
  Widget build(BuildContext context){
    return MaterialApp(
      home: Scaffold(
        body: Center(
          child: DropdownButton<String>(
            value: _selectedValue,
            items: <String>['A','B','C'].map((String value){
              return DropdownMenuItem<String>(
                value: value,
                child: Text(value),
              );
            }).toList(),
            onChanged: (String? newValue){
              setState((){
                _selectedValue = newValue;
              });
            },
          ),
        ),
      ),
    );
  }
}