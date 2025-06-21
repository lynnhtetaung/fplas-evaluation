import 'package:flutter/material.dart';

void main(){
	runApp(const MyApp());
}

class MyApp extends StatelessWidget{
	const MyApp({super.key});
    
    @override
    Widget build(BuildContext context){
    	const String appTitle = 'Flutter layout demo';
        return MaterialApp(
        	title: appTitle,
            home: Scaffold(
            	body: Padding(
                	padding: EdgeInsets.all(16.0),
                    child: TextField(
                    	decoration: InputDecoration(
                        	labelText: 'Enter name',
                            border: OutlineInputBorder(),
                        ),
                    ),
                ),
            ),
        );
    }
}