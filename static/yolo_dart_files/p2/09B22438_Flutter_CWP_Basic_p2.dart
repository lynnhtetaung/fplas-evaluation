import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return MaterialApp(
      home: TextFieldExample(),
     );
  }
}

class TextFieldExample extends StatelessWidget {
  @override
  Widget build(BuildContext context){
  return Scaffold(
    backgroundColor: Color(0xFFFCF5FC),
    body: Center(
      child: Container(
        width: 200,
        child: TextField(
           decoration: InputDecoration(
             hintText: 'Enter name',
             enabledBorder: OutlineInputBorder(
               borderSide: BorderSide(color:Colors.green.shade300),
               ),
               focusedBorder: OutlineInputBorder(
                 borderSide: BorderSide(color: Colors.green),
                ),
              ),
            ),
          );
  }
}