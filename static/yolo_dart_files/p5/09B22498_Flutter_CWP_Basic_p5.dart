import 'package:flutter/material.dart';
 void main(){
  runApp(MyApp());
 }
 
 class MyApp extends StatefulWidget{
 @override
 _MyAppState createState() => _MyAppState();
 }
 
 class _MyAppState extends State<MyApp>{
  String selectedValue ='Apple';
   final List<String> items =['Apple','Banana','Orange'];
   
   @override
  Widget build(BuildContext context){
  return MaterialApp(
    home:Scaffold(
     backgroundColor:Color(0xFFFDF6FD),
     body:Center(
     child:Container(
     padding:EdgeInsets.symmetric(horizontal:12,vertical:4),
     decoration:BoxDecoration(
     border:Border.all(color:Colors.red),
     borderRadius:BorderRadius.circular(8),
     color:Colors.white,
     ),
     child:DropdownButtonHideUnderline(
     
     child:DropdownButton<String>(
       value:selectedValue,
       icon:Icon(Icons.arrow_drop_down),
       onChanged:(String? newValue){
       setState((){
       selectedValue=newValue!;
       });
       },
    items:items.map<DropdownMenuItem<String>>((String value){
      return DropdownMenuItem<String>(
       value: value,
       child:Text(value),
       );
    }).toList(),
       ),
       ),
      ),
     ),
    ),
   );
  }
 }