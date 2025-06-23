import 'package:flutter/material.dart';

void main() {
	runApp(MyApp());
}

class MyApp extends StatelessWidget {
	@override
    Widget build(BuildContext context) {
    	return MaterialApp(
        	home: Scaffold(
            	body: Center(
                	child: ElevatedButton(
                        onPressed: () {
                        	print('Button');
                        },
                        child: Text(
                        	'Click me',
                            style: TextStyle(fontSize: 16),
                        ),
                    ),
                ),
            ),
        );
    }
}