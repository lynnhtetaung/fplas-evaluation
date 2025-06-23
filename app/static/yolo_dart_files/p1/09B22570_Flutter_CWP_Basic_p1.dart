import 'package:flutter/material.dart';

void main() {
	runApp(MyApp());
}

class MyApp extends StatelessWidget {
	@override
    Widget build(BuildContext context) {
    	return MaterialApp(
        	home: Scaffold(
            	backgroundColor: Colors.pink[50],
                body: Center(
                	child: Text(
                    	'This is sample text',
                        style: TextStyle(
                        	color: Colors.red,
                            fontSize: 20,
                        ),
                     ),
                 ),
             ),
         );
    }
}