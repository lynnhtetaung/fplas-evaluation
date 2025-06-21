import 'package:flutter/material.dart';

void main() {
	runApp(MyApp());
}

class MyApp extends StatelessWidget {
	@override
    Widget build(BuildContext context) {
    	return MaterialApp(
        	title: 'Sample App',
            home: Scaffold(
            	appBar: AppBar(
                	title: Text('SampleApp'),
                ),
                body: Center(
                	child: Text(
                    	'This is sample text',
                        style: TextStyle(fontSize: 24),
                    ),
                ),
            ),
        );
        
    }
}