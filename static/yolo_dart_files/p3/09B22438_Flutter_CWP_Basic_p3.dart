import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Color(0xFFF8F0FF),
        body: Center(
          child: ElevatedButton(
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.white,
              foregroundColor: Colors.purple,
              shape: StandiumBorder(),
              elevation: 4,
              shadowColor: Colors.grey,
              padding: EdgeInsets.symmetric(horizontal: 30, vertical: 15),
             ),
             onPressed:(){},
             child: Text(
               'Click me',
               style: TextStyle(fontSize: 18),
               ),
              ),
             ),
            ),
           );
         }
      }
  }
}