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
                	child: Container(
                    	width: 250, height: 50,
                        margin: EdgeInsets.all(10),
                        padding: EdgeInsets.all(15),
                        decoration: BoxDecoration(
                            border: Border.all(
                            	color: Colors.green,
                                width: 1,
                            ),
                            borderRadius: BorderRadius.circular(5),
                        ),
                        child: Text(
                        	'Enter name',
                            style: TextStyle(
                            	fontSize: 16,
                                color: Colors.green
                            ),
                        ),
                    ),
                ),
            ),
        );
    }
}