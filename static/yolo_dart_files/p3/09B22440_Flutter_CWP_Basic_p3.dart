import 'package:flutter/material.dart';

void main(){
	runApp(MyApp());
}

class MyApp extends StatelessWidget{
	@override
    Widget build(BuildContext context){
    	return MaterialApp(
        	home: ElevatedButtonExample(),
        );
    }
}

class ElevatedButtonExample extends StatelessWidget{
	@override
    Widget build(BuildContext context){
    	return Scaffold(
        	backgroundColor: Color(0xFFF9F0F7),
            body: Center(
            	child: ElevatedButton(
            		onPressed: (){
                	},
                	style: ElevatedButton.styleFrom(
                		backgroundColor: Color(0xFFEDE6F6),
                    	foregroundColor: Color(0xFF6F3DD2),
                    	shape: RoundedRectangleBorder(
                    		borderRadius: BorderRadius.circular(30.0),
                    	),
                    	padding: EdgeInsets.symmetric(horizontal: 30, vertical: 16),
                    	elevation: 4,
                	),
                	child: Text('Click me'),
                ),
            ),
        );
    }
}