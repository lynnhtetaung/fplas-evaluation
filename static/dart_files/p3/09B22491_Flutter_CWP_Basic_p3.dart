import 'package:flutter/material.dart';

void main() {
	runApp(MyApp());
}

class MyApp extends StatelessWidget {
	@override
    Widget build(BuildContext context) {
    	return MaterialApp(
        	title: 'ElevatedButton Example',
            home: Scaffold(
            	appBar: AppBar(
                	title: Text('ElevatedButton Example'),
                    ),
                    body: Center(
                    	child: ElevatedButton(
                        	onPressed: () {
                            	print('ボタンが押されました');
                            },
                            child: Text('Click me'),
                        ),
                    ),
                ),
           );
    }
}