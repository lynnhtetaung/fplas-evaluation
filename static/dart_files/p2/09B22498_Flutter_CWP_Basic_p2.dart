import 'package:flutter/material.dart';
void main()=>runApp(MyApp());

class MyApp extends StatelessWidget {
@override
Widget build(BuildContext context) {
 return MaterialApp(
  home: TextFieldExample(),
  );
 }
}

class TextFieldExample extends StatelessWidget{
@override
Widget build(BuildContext context){
  return Scaffold(
  backgroundColor: Color(0xFFFDF3FB),
  body: Center(
   child:Padding(
    padding:const EdgeInsets.all(16.0),
     child :TextField(
      decoration:InputDecoration(
        hintText:'Enter name',
        hintStyle: TextStyle(color: Colors.green),
        enabledBorder:OutlineInputBorder(
         borderSide:BorderSide(color: Colors.green),
        ),
      focusedBorder:OutlineInputBorder(
       borderSide:BorderSide(color: Colors.green, width: 2.0),
        ),
       ),
      ),
     ),
    ),
   );
  }
 }