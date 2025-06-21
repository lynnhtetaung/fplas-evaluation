import 'package:flutter/material.dart';

void main (){
 runApp(MyApp());
}

class MyApp extends StatelessWidget {
@override
Widget build(BuildContext context){
 return MaterialApp(
   home: Scaffold( 
      backgroundColor: Color(0xFFFDF6FD),
      body: Center(
        child: ElevatedButton(
          onPressed :() {
          
          },
          style : ElevatedButton.styleFrom(
            backgroundColor: Colors.white,
            foregroundColor: Colors.purple,
            elevation: 4,
            shape: StadiumBorder(),
            padding: EdgeInsets.symmetric(horizontal:32,vertical:16),
            textStyle: TextStyle(
              fontSize: 18,
              fontWeight: FontWeight.bold,
              ),
             ),
             child: Text('Click me'),
          ),
         ),
        ),
       );
      }
     }