import 'package:flutter/material.dart';

void main() {
	runApp(MyApp());
}

class MyApp extends StatelessWidget{
	@override
    Widget build(BuildContext context){
    	return MaterialApp(
        	title: 'Flutter Demo',
            theme: ThemeData(
            	primarySwatch: Colors.blue,
            ),
            home: MyHomePage(),
         );
    }
}

class MyHomePage extends StatelessWidget {
	@override
    Widget build(BuildContext context) {
    	return Scaffold(
        	appBar: AppBar(
            	title: Text('Text表示サンプル'),
            ),
            body: Center(
            	child: Text(
                	'This is sample Text',
                    style: TextStyle(fontSize: 24,
                    color: Colors.red,
                    ),
                 ),
            ),
        );
    }
}