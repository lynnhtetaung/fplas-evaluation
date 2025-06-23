import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  @override
  state<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  bool isChecked = true;
  
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.pink[50],
        body: Center(
          child: Checkbox(
            value: isChecked,
            onChanged: (bool? value){
              setState((){
                isChecked = value ?? false;
              });
            },
           ),
          ),
         ),
        );
  }
}