import 'package:flutter/material.dart';

void main() {
	runApp(MyApp());
}

class MyApp extends StatelessWidget {
    @override
    Widget build(BuildContext context) {
    	return MaterialApp(
        	home: Scaffold(
            	appBar: AppBar(title: Text("TextField Example")),
            	body: Padding(
                    padding: EdgeInsets.all(20.0),
                    child: TextField(
                        decoration: InputDecoration(
                        	border: OutlineInputBorder(),
                            labelText: 'Enter name',
                        ),
                    ),
                ),
            ),
        );
    }
}