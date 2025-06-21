import 'package:flutter/material.dart';

void main() {
	runApp(MyApp());
}

class MyApp extends StatelessWidget{
	@override
    Widget build (BuildContext context) {
    	return MaterialApp(
        	home: Scaffold(
            	appBar: AppBar(
                	title: Text('TextField sample')),
                body: padding(
                	padding: const EdgeInsets.all(16.0),
                    child: TextField(
                    	decoration: InputDecoration(
                        labelText: '文字を入力してください',
                        border: OutlineInputBorder(),
            			),
                	),
            	),
            ),
        );
    }
}