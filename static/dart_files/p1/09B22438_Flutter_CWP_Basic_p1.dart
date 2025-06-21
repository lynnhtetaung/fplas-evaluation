import 'package:flutter/material.dart';
void main() {
   runApp(MyApp());
}

class MyApp extends StatelessWidget{
  @override
  Widget build(BuildContext context){
  return MaterialApp(
    home:Center(
    child:Text(
    'This is sample text',
    style:TextStyle(
    color: Color.red,
    fontSize: 16,
    ),
   ),
   ),
   ),
   );
  }
}