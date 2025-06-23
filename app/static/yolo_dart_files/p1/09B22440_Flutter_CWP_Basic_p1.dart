import 'package:flutter/material.dart';

void main(){
	runApp(MyApp());
}

class MyApp extends StatelessWidget{
	@override
    Widget build(BuildContext context) {
    	return MaterialApp(
        	home: Scaffold(
            	appBar: AppBar(
                	title: Text('Flutter Sample'),
                ),
                body: Center(
                	child: Text(
                    	'This is sample text',
                        style: TextStyle(fontSize: 30, color: Colors.red,),
                    ),
                ),
            ),
        );
    }
}