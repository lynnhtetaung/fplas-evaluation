import 'package:flutter/material.dart';

void main(){
 runApp(MyApp());
 }
 
 class MyApp extends StatefulWidget{
 @override
 _MyAppState createState() => _MyAppState();
 }

class _MyAppState extends State<MyApp>{
 bool isChecked = true;
 
 @override
 Widget build(BuildContext context){
  return MaterialApp(
    home: Scaffold(
      backgroundColor:Color(0xFFFDF6FD),
      body:Center(
        child : Checkbox(
         value: isChecked,
         onChanged: (bool? newValue){
           setState((){
            isChecked = newValue ?? false;
           });
          },
          activeColor:Colors.blue,
          ),
         ),
        ),
       );
      }
     }