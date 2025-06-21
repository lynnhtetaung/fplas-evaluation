import 'package:flutter/material.dart';

void main() {
	runApp(MyApp());
}

class MyApp extends StatelessWidget {
	@override
    Widget build(BuildContext context) {
    	return MaterialApp(
        	home: Scaffold(
            	appBar: AppBar(
                	title: Text('TextField Sample'),
                ),
                body: Center(
                	child: ConstrainedBox(
                    	constraints: BoxConstraints(
                        	maxWidth: 300,
                        ),
                        child: TextField(
                        	decoration: InputDecoration(
                            	border: OutlineInputBorder(),
                                labelText: 'Enter text',
                            ),
                        ),
                    ),
                ),
            ),
        );
    }
}