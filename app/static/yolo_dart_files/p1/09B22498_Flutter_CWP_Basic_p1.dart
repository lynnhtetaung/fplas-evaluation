import 'package:flutter/material.dart';

void main () {
 runApp(MyApp());
}

 class MyApp extends StatelessWidget {
 @override
 Widget build(BuildContext context) {
  return MaterialApp(
   home: Scaffold(
    backgroundColor: Color(0xFFFFF0F5),
    body: Center(
      child: Text(
      'This is sample text',
      style: TextStyle(
       color: Colors.red,
        fontSize: 20.0,
        ),
       ),
      ),
     ),
    );
 }
 }